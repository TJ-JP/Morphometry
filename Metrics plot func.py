# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:12:15 2022

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:51:39 2022

@author: Priya
"""

import pandas as pd
from matplotlib import pyplot as plt
import os
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
#file_path = (r"H:\testing\metric-kid50k_full.jsonl")

folder = 'J:\\Jp\\Metrics excel\\testing\\New folder\\'
aug = 'noise256'
files = os.listdir(folder)
#r = df['results'].values.tolist()
#scorea = (score.fid50k_full)
keyword = ['1', '2']
def append_files(files, startswith, column):
    filenamelist = []
    for filename in files:
        if filename.startswith(startswith) and filename.endswith('jsonl'):
            filenamelist.append(filename)
    y = []
    for f in filenamelist:
        df = pd.read_json(os.path.join(folder, f), lines = True)
        score = df['results'].apply(pd.Series)
        result = (score[column])
        y.extend(result)
        
        """
      
        if (len(result)) == 9:
            y.extend(result)
        elif (len(result)) == 8:
            result = result[:-2]
            y.extend(result) 
        else:
            result = result[:-1]
            y.extend(result)  
           
        
        if '3' in f:
            y.extend(result)
            
        else:
            result = result[:-1]
            y.extend(result)
           """
    x = [0]
    for i in range(len(y) - 1):
        x.append((i+1)*40)
    
    return x, y

xis50k_mean, yis50k_mean = append_files(files, 'metric-is50k', 'is50k_mean')
xis50k_mean, yis50k_std = append_files(files, 'metric-is50k', 'is50k_std')

xppl2_wend, yppl2_wend = append_files(files, 'metric-ppl2_wend', 'ppl2_wend')


xkid50k_full, ykid50k_full = append_files(files, 'metric-kid50k_full', 'kid50k_full')


xpr50k3_full_precision, ypr50k3_full_precision = append_files(files, 'metric-pr50k3_full', 'pr50k3_full_precision')
print(len(ypr50k3_full_precision))

xfid50k_full, yfid50k_full = append_files(files, 'metric-fid50k_full', 'fid50k_full')

data = pd.DataFrame({'X': xis50k_mean, 'yis50k_mean': yis50k_mean, 'yis50k_std' : yis50k_std, 
                          'yppl2_wend' : yppl2_wend,
                          'ykid50k_full' : ykid50k_full,
                          'ypr50k3_full_precision' : ypr50k3_full_precision,
                          'yfid50k_full' : yfid50k_full})

# writing to Excel
Combined_data = pd.ExcelWriter('J:\\Jp\\Metrics excel\\testing\\' + aug +'a.xlsx')
  
# write students data to excel
data.to_excel(Combined_data)
  
# save the students result excel
Combined_data.save()


"""
label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(xis50k_mean))
plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
plt.plot(label_loc, yis50k_mean, label='is50k_mean')
plt.plot(label_loc, ykid50k_full, label='kid50k_full')
plt.plot(label_loc, yfid50k_full, label='fid50k_full')
plt.title('metrics', size=20)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels = xis50k_mean)
plt.legend()
plt.show()

fig = px.line_polar(
                    r=xis50k_mean,
                    theta=yis50k_mean,
                    line_close=True)


fig.show()
"""