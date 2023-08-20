# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:38:20 2022

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from os import listdir
import seaborn as sns
"""
df = pd.read_excel(r'J:\Jp\Metrics excel\testing\512\bg.xlsx')
print(df)
x = df.X
y = df['yfid50k_full']
plt.plot(x, y)
plt.xlabel("Epochs")  # add X-axis label
plt.ylabel("Y-axis")  # add Y-axis label
plt.title("Any suitable title")
plt.show()

"""

folder = 'J:/Jp/Metrics excel/testing/256/'
files = [f for f in listdir(folder)]
files = os.listdir(folder)

#Individual plots
"""
is50k = []
is50k_std = []
ppl2_wend = []
kid50k = []
pr50k3 = []
fid50k = []
x = []
Aug = []
for file in files:
    
    if file.endswith('.xlsx'):
        Aug.append(file[:-8])
        df = pd.read_excel(os.path.join(folder, file))
        x.append(df.X)
        is50 = df.yis50k_mean
        is50k.append(is50)
        is50_st = df.yis50k_std
        is50k_std.append(is50_st)
        ppl2_wen = df.yppl2_wend
        ppl2_wend.append(ppl2_wen)
        kid50 = df.ykid50k_full
        kid50k.append(kid50)
        pr50k = df.ypr50k3_full_precision
        pr50k3.append(pr50k)
        fid50 = df.yfid50k_full
        fid50k.append(fid50)
def plot(score, ylim, ylabel, infolder):
    for i in range(len(x)):
        plt.figure()
        plt.plot(x[i],score[i], **{'marker': 'o'})
        #plt.errorbar(x[i],score[i], yerr = is50k_std[i], **{'marker': 'o'})
        plt.xlim(0, 1000)
        plt.ylim(0, ylim)
        plt.xlabel("Iteration", fontsize=18)  # add X-axis label
        plt.ylabel(ylabel, fontsize=18) 
        plt.title(Aug[i], fontsize=24)
        plt.savefig(folder + infolder + Aug[i] + '.png', dpi = 1200)
        plt.show()
        # Show/save figure as desired.

#plot(is50k, 3, "IS", "is50k/")
#plot(ppl2_wend, 50, "PPL2_WEND", "ppl2_wend/")
#plot(kid50k, 0.7, "KID", "kid50k/")
plot(fid50k, 550, "FID", "fid50k/")
#plot(pr50k3, 0.8, "PR", "pr50k3/")    

"""

#KEEP FOR RANGES
"""
plot(is50k, 3, "IS", "is50k/")
plot(ppl2_wend, 50, "PPL2_WEND", "is50k/")
plot(kid50k, 0.7, "KID", "is50k/")
plot(fid50k, 520, "FID", "is50k/")
plot(pr50k3, 0.8, "PR", "pr50k3/")    
"""
   
#For altogether

for file in files:
    if file.endswith('.xlsx'):
        
        df = pd.read_excel(os.path.join(folder, file))
        x = df.X
        is50k = df.yis50k_mean
        is50_std = df.yis50k_std
        ppl2_wend = df.yppl2_wend
        kid50k = df.ykid50k_full
        pr50k3 = df.ypr50k3_full_precision
        fid50k = df.yfid50k_full
        plt.plot(x, is50k, label = file[:-8], **{'marker': 'o'})
        plt.xlabel("Iteration", fontsize=18)  # add X-axis label
        plt.ylabel('IS', fontsize=18) 
plt.xlim(0, 1000)
plt.ylim(0, 3)
plt.legend(bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig(folder + 'is50k.png', dpi = 1200)
plt.show()

 


        