import os
import pandas as pd
import pybedtools
import numpy as np
import subprocess
import fnmatch

bam_dir = '/home/samzhao/F_seq/ChIP_seq_benchmark/Simulated_Data/BamFiles/'
for bam_file in os.scandir(bam_dir):
    if fnmatch.fnmatch(bam_file.path, '*_Input_*.bam'):
        control_file = bam_file.path
        file_name_ls = bam_file.path.split('_')
        signal_file = '_'.join(bam_file.path.split('_')[0:-2] + bam_file.path.split('_')[-1:])
        exp_num = bam_file.path.split('_')[-1].split('.')[0]
        name = 'Fseq2_' + exp_num
        subprocess.run(f"fseq2 callpeak {signal_file} -control_file {control_file} -l 50 -t 8.0 -f 166 -fc 160 -o ./Fseq2_output -name {name} -cpus 1 -v -p_thr False", shell=True)
        
