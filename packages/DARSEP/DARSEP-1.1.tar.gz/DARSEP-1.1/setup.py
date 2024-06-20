import setuptools
from setuptools import setup, find_packages

setup(
    name='DARSEP',
    version='1.1',
    packages=find_packages(),
    package_data={
        '': ['*.pth','*.txt', 'cov2_wt.fasta', 'rbd.fasta'],  # 这将包含所有目录下的.pth文件
    },
    url='https://github.com/zjhubio/DARSEP',
    license='NONE',
    author='lizhong',
    author_email='lizhong@zjhu.edu.cn',
    description='Variation and evolution analysis of SARS-CoV-2 using self-game sequence optimization'
)