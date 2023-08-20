# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 14:28:54 2022

@author: DELL
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 
import os
from os import path
from pathlib import Path
from os import listdir

folder2 = "G:\\UK\\patches\\Copy\\Generated\\Generated\\"
folder = "G:\\UK\\patches\\Copy\\Generated\\Directionality\\Excel\\"
files = [f for f in listdir(folder)]
files2 = [f for f in listdir(folder2)]
rcombineddata = pd.DataFrame()
#dest = 'C:\\Users\\DELL\\Desktop\\Re2\\Mike\\epoch1000\\Directionality\\frac\\'
nam = []
# loop over the list of csv files
for file in files:
       
        #name = file.replace('Directionality', '')
        name = file.replace('.xls', '.png')
        nam.append(name)

 
n2 = []
for f in files2:
    n2.append(f)

l = np.setdiff1d(n2,nam)
print(l)
"""
import shutil
src_files = os.listdir(folder2)
for file_name in files2:
    if file_name in l:
        full_file_name = os.path.join(folder2, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
            """