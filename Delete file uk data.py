# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:41:13 2022

@author: DELL
"""
"""
import os
import glob

path = "G:\\UK\\patches\\Combined"
for file in glob.glob(path):
    os.remove(file)

"""
"""
import os
path = "G:\\UK\\patches\\Copy\\Combined copy"
for file in os.listdir(path): 
    if '_19.jpg' in file:
        os.remove(os.path.join(path, file))
      
        
      
##s1 - 1(1, 5, 8), 4(1, 5, 9), 8(1, 5, 9), 12(1, 5, 9), 15 (1, 5, 8)
##s2 - 1(1,2), 5(1, 6, 11), 9(1, 6, 10), 13(1, 6, 10), 16(1, 4, 6)
##s3 - 1(1, 2), 5(1, 6, 11), 10(1,7, 12), 15(1,7, 12), 19(1, 2) 
##s4 - 1(1), 5(1, 6, 10), 10(1, 6, 11), 14(1, 6, 11), 18(1, 3, 4)
##s5 - 1(1,2,3), 5(1, 6, 10), 10(1, 6, 11), 14(1, 6, 11), 18(1, 3, 4)
##s6 - 1(1,3,4), 5(1, 6, 11), 10(1,7, 12), 14(1, 6, 11), 18(1,2,3)
##s7 - 1(1), 6(1, 6, 10), 11(1, 6, 10), 16(1, 6, 10), 20(1)
##s8 - 1(1,2), 5(1, 6, 10), 10(1, 6, 10), 15(1, 5, 9), 19(1,2,3)
##s9 - 1(1, 3, 4), 5(1, 6, 11), 10(1, 6, 11), 14(1, 6, 10), 18(1,2,3)


#1,5,10,15,20

"""


# importing required packages
from pathlib import Path
import shutil
import os
 
# defining source and destination
# paths
src = 'G:\\UK\\patches\\Copy\\generated_cond\\CCGC\\Directionality\\KDE\\'
trg = 'G:\\UK\\patches\\Copy\\generated_cond\\9\\Directionality\\'
 
files=os.listdir(src)
 
# iterating over all the files in
# the source directory
for fname in files:
    if 'S9' in fname:
     
    # copying the files to the
    # destination directory
     shutil.copy2(os.path.join(src,fname), trg)
     

"""  

import pandas as pd
from matplotlib import pyplot as plt
import os
from os import path
from os import listdir

import openpyxl

File = 'Overall'

df = pd.read_excel("G:\\UK\\patches\\Copy\\generated_cond\\CCGC\\Overallgc.xlsx")
df = df[df['Label'].str.contains('S1')]
print(df)
df.to_excel("G:\\UK\\patches\\Copy\\generated_cond\\1\\overall.xlsx")  
     
"""  
