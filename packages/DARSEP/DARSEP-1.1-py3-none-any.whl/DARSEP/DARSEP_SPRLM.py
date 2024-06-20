import sys
from tqdm import tqdm
import random
import torch
import datetime
import pandas as pd
import numpy as np
from torch.utils.data import DataLoader,Dataset,random_split
import torch.nn.functional as F
import torch.optim as optim
from collections import defaultdict, deque
from .sequence_env_m_p import Seq_env, Mutate
from .mcts_alphaZero_mutate_expand_m_p_gfp import MCTSMutater
from .p_v_net_3 import PolicyValueNet

sequence_fitness_data_dir = './seqs_fitness.txt'
aa_alphabet = "ACDEFGHIJKLMNPQRSTVWXY-"

def seq2onehot(sequence, alphabet):
    feat = np.zeros((len(sequence), len(alphabet)))
    for i in range(len(sequence)):
        feat[i, alphabet.index(sequence[i])] = 1
    return feat

class sequenceFitnessDataset(Dataset):
    def __init__(self, sequences, fitnessess):
        self.sequences = sequences
        self.fitnessess = fitnessess

    def __getitem__(self, index):
        seq, target = self.sequences[index], self.fitnessess[index]
        return seq, target

    def __len__(self):
        return len(self.sequences)

def amino_acid_encode(sequence_fitness_data_dir):
    file = open(sequence_fitness_data_dir, "r")
    line = file.readlines()
    seq_list = []
    fitness_list = []
    for i in range(1, len(line)):
        tmp = line[i].strip().split("\t")
        seq_list.append(tmp[0])
        fitness_list.append(float(tmp[1]))
  
    seq_feat = np.array([seq2onehot(seq, aa_alphabet) for seq in seq_list])
    seq_onehots = torch.from_numpy(seq_feat).to(torch.float32)
    fitnessess = torch.from_numpy(np.array(fitness_list))
    fitnessess = fitnessess.to(torch.float32)
    
    return seq_onehots, fitnessess

def fitnessPredict():
    
    epochs = 10
    losses = []
    
    seq_onehots, fitnessess = amino_acid_encode(sequence_fitness_data_dir)
    seqFitnessDataset = sequenceFitnessDataset(seq_onehots, fitnessess)
    trainDataloader = DataLoader(seqFitnessDataset,shuffle=True)
    
    model = FitnessPredictorModel().to('cuda')
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(epochs):
        print("Epoch " + str(epoch))
        for i, batch in tqdm(enumerate(trainDataloader), total=len(trainDataloader), desc="Training Batches"):
            seq = batch[0]
            seq = seq.permute(0,2,1).to('cuda')
            fitness = batch[1].to('cuda')
            optimizer.zero_grad()

            predicts = model(seq).squeeze()
            loss = F.mse_loss(predicts, fitness)
            loss.backward()
            optimizer.step()
        print("loss:{}".format(loss))
        losses.append(loss.item())
    
    return losses, model

class FitnessPredictorModel(torch.nn.Module):
     def __init__(self):
        super(FitnessPredictorModel, self).__init__()    
        
        self.conv1 = torch.nn.Conv1d(23, 64, kernel_size=5) 
        self.conv2 = torch.nn.Conv1d(64, 48, kernel_size=5, padding=1)
        self.conv3 = torch.nn.Conv1d(48, 32, kernel_size=5, padding=1)
    
        self.maxpool1 = torch.nn.MaxPool1d(kernel_size=1, stride=1)
        self.maxpool2 = torch.nn.MaxPool1d(kernel_size=1, stride=1)
        
        self.val_fc1 = torch.nn.Linear(6880, 100)# * alphabet_len
        self.val_fc2 = torch.nn.Linear(100, 100)  # * alphabet_len
        self.dropout = torch.nn.Dropout(p=0.25)
        self.val_fc3 = torch.nn.Linear(100, 1)
    
     def forward(self, input):
        x = F.relu(self.conv1(input))
        x = F.relu(self.conv2(x))
        x = F.relu(self.maxpool1(x))

        x = F.relu(self.conv3(x))
        x_act = F.relu(self.maxpool2(x))
        
        
        x_score_1 = x_act.view(x_act.shape[0], -1)
        
        x_score_2 = F.relu(self.val_fc1(x_score_1))
        x_score_2 = F.relu(self.val_fc2(x_score_2))
        x_score_2 = self.dropout(x_score_2)
        x_score_3 = self.val_fc3(x_score_2)

        return x_score_3   
    
class seqOptimizeGame():
    def __init__(self, init_seq, alphabet, model, trust_radius, init_model=None): #init_model=None
        self.seq_len = len(init_seq)
        self.vocab_size = len(alphabet)
        self.n_in_row = 4
        self.learn_rate = 2e-3
        self.lr_multiplier = 1.0 
        self.temp = 1.0
        self.n_playout = 200
        self.c_puct = 10
        self.buffer_size = 10000
        self.batch_size = 32 
        self.data_buffer = deque(maxlen=self.buffer_size)
        self.play_batch_size = 1
        self.epochs = 5 
        self.kl_targ = 0.02
        self.check_freq = 50
        self.game_batch_num = 1500
        self.best_win_ratio = 0.0
        self.pure_mcts_playout_num = 1000
        self.buffer_no_extend = False
        self.generated_seqs = []
        self.fit_list = []
        self.p_dict = {}
        self.m_p_dict = {}
        self.retrain_flag = False
        self.part = 2
        
        self.seq_env = Seq_env(self.seq_len,alphabet,model,init_seq,trust_radius)
        self.mutate = Mutate(self.seq_env)
        self.policy_value_net = PolicyValueNet(self.seq_len,self.vocab_size,use_gpu=True)
        self.mcts_player = MCTSMutater(self.policy_value_net.policy_value_fn,c_puct=self.c_puct,n_playout=self.n_playout,is_selfplay=1)

    def collect_selfplay_data(self, n_games=1):
        counts = len(self.generated_seqs)
        self.buffer_no_extend = False
        for i in range(n_games):
            play_data, seq_and_fit, p_dict = self.mutate.start_mutating(self.mcts_player,temp=self.temp)    #winner,
            play_data = list(play_data)[:]
            self.episode_len = len(play_data)
            self.p_dict = p_dict
            self.m_p_dict.update(self.p_dict)
            if self.episode_len == 0:
                self.buffer_no_extend = True
            else:
                self.data_buffer.extend(play_data)
                for seq, fit in seq_and_fit:  #alphafold_d
                    if seq not in self.generated_seqs:
                        self.generated_seqs.append(seq)
                        self.fit_list.append(fit)
                        if seq not in self.m_p_dict.keys():
                            self.m_p_dict[seq] = fit
                    
                        if len(self.generated_seqs)%10==0 and len(self.generated_seqs)>counts and self.part<=10:
                            self.retrain_flag=True
                       

    def policy_update(self):
        mini_batch = random.sample(self.data_buffer, self.batch_size)
        state_batch = [data[0] for data in mini_batch]
        mcts_probs_batch = [data[1] for data in mini_batch]
        winner_batch = [data[2].cpu() for data in mini_batch]
        old_probs, old_v = self.policy_value_net.policy_value(state_batch)
        for i in range(self.epochs):
            loss, entropy = self.policy_value_net.train_step(state_batch,mcts_probs_batch,winner_batch,self.learn_rate*self.lr_multiplier)
            new_probs, new_v = self.policy_value_net.policy_value(state_batch)
            kl = np.mean(np.sum(old_probs * (np.log(old_probs + 1e-10) - np.log(new_probs + 1e-10)),axis=1))
            if kl > self.kl_targ * 4: 
                break
        
        if kl > self.kl_targ * 2 and self.lr_multiplier > 0.1:
            self.lr_multiplier /= 1.5
        elif kl < self.kl_targ / 2 and self.lr_multiplier < 10:
            self.lr_multiplier *= 1.5
        

        explained_var_old = (1 - np.var(np.array(winner_batch) - old_v.flatten()) / np.var(np.array(winner_batch)))
        explained_var_new = (1 - np.var(np.array(winner_batch) - new_v.flatten()) / np.var(np.array(winner_batch)))
        print(("kl:{:.5f}," 
               "lr_multiplier:{:.3f},"
               "loss:{},"
               "entropy:{},"
               "explained_var_old:{:.3f},"
               "explained_var_new:{:.3f}"
               ).format(kl,self.lr_multiplier,loss,entropy,explained_var_old,explained_var_new))
        return loss, entropy


    def playGame(self):
        starttime = datetime.datetime.now() 

        try:
            for i in range(self.game_batch_num):
                self.collect_selfplay_data(self.play_batch_size)
                print("batch i:{}, episode_len:{}".format(i+1, self.episode_len))
                
                if self.retrain_flag and self.part<=10:
                    print('train predictor again')
                    _, update_model = fitnessPredict()            
                    self.seq_env.model = update_model
                    self.seq_env.model.eval()
                    self.part = self.part+1
                    self.retrain_flag = False
                    
                if len(self.m_p_dict.keys()) >= 4000:
                    for key, value in self.m_p_dict.items():
                        self.m_p_dict[key] = value.cpu()
                    m_p_fitness = np.array(list(self.m_p_dict.values()))
                    m_p_seqs = np.array(list(self.m_p_dict.keys()))
                    df_m_p = pd.DataFrame({"sequence": m_p_seqs, "pred_fit": m_p_fitness})
                    df_m_p.to_csv("./generated_sequence.csv",index=False)
                    endtime = datetime.datetime.now() 
                    print('time cost：',(endtime-starttime).seconds)
                    sys.exit(0)
                    
                if len(self.data_buffer) > self.batch_size and self.buffer_no_extend == False:
                    loss, entropy = self.policy_update()
                    
        except KeyboardInterrupt:
            print('\n\rquit')

def selfPlay():
    init_seq = "RVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNF"
    model = FitnessPredictorModel()
    model.load_state_dict(torch.load("SPRLM_params.pth"))
    model = model.to('cuda')
    game = seqOptimizeGame(init_seq, aa_alphabet, model, trust_radius=100,)
    game.playGame()

if __name__ == "__main__":
    selfPlay()