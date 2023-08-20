# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:51:39 2022

@author: Priya
"""

import pandas as pd
from matplotlib import pyplot as plt
import os
import numpy as np
#file_path = (r"H:\testing\metric-kid50k_full.jsonl")

folder = 'J:\\Jp\\bg\\testing\\'
files = os.listdir(folder)
x = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720, 760, 800, 840, 880, 920, 960, 1000, 1400]

def scorefunction(file):
        df = pd.read_json(os.path.join(folder, file), lines = True)
        score = df['results'].apply(pd.Series)
        return score

filenamelist = []
#r = df['results'].values.tolist()
#scorea = (score.fid50k_full)
for filename in files:
    if filename.startswith('metric-is50k'):
        filenamelist.append(filename)
print(filenamelist)
columns = []
for f in filenamelist:
    score = scorefunction(f)
    is50k_mean = (score.is50k_mean)
    is50k_mean = is50k_mean[:-1]
    #print(is50k_mean)
    column = columns.extend(is50k_mean)
x = []
for i in range(len(columns)):
    x.append((i+1)*40)
print(x)
print(columns)
plt.plot(x, columns)


"""

    
for file in files:
    if file.startswith('metric-is50k'):
        score = scorefunction(file)
        is50k_mean = (score.is50k_mean)
        is50k_std = (score.is50k_std)
        is50k_mean = is50k_mean.append(is50k_mean)
        is50k_std = is50k_std.append(is50k_std)
        y = is50k_mean
        yerror = is50k_std
        print(is50k_mean)
    #plt.plot(x, is50k_mean)

    if file.startswith('metric-kid50k_full'):
        score = scorefunction(file)
        kid50k_full = (score.kid50k_full)
        kid50k_full = kid50k_full.append(kid50k_full)
        y = kid50k_full
        print(kid50k_full)
        plt.plot(x, y)

    elif file.startswith('metric-ppl2_wend'):
        score = scorefunction(file)
        ppl2_wend = (score.ppl2_wend)
        ppl2_wend = ppl2_wend.append(ppl2_wend)
        y = ppl2_wend
        print(ppl2_wend)
        #plt.plot(x, y)


    elif file.startswith('metric-pr50k3_full'):
        score = scorefunction(file)
        pr50k3_full_precision = (score.pr50k3_full_precision)
        pr50k3_full_precision = ppl2_wend.append(pr50k3_full_precision)
        y = pr50k3_full_precision
        print(pr50k3_full_precision)
        #plt.plot(x, y)

    elif file.startswith('metric-fid50k_full'):
        score = scorefunction(file)
        fid50k_full = (score.fid50k_full)
        fid50k_full = fid50k_full.append(fid50k_full)
        y = fid50k_full
        print(fid50k_full)
        plt.plot(x, y)

"""