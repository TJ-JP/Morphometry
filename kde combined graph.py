# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 19:21:57 2022

@author: DELL
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 
import os
import glob
from os import path
from os import listdir

paths = 'C:\\Users\\DELL\\Desktop\\Re2\\Stylegan GI\\Overall GI.xlsx' 
df = pd.read_excel(paths)
df1 = df[df['Category'] == 1]
df2 = df[df['Category'] == 2]
df3 = df[df['Category'] == 3]

#change dflist
dflist = df1.Label
#Change replace
list2 = [y.replace('.png', '_LocThk.xlsx') for y in dflist]
#Change folder
folder = "C:\\Users\\DELL\\Desktop\\Re2\\Stylegan GI\\Local thickness background\\Excel with range\\kde 100"
files2 = [f for f in listdir(folder)]
combineddata = pd.DataFrame()
for file in list2:
    if file in files2:
        data = pd.read_excel(os.path.join(folder, file), header = None)
        #Change iloc
        data = data.iloc[1:, 1:]
        
        combineddata = combineddata.append(data)
#Change header
combineddata.columns = ['Local thickness', 'Probability Density']
combineddata['Local thickness'] = pd.to_numeric(combineddata['Local thickness'])
combineddata['Probability Density'] = pd.to_numeric(combineddata['Probability Density'])
gcombineddata = combineddata.groupby(['Local thickness'])['Probability Density'].mean().reset_index()
gstd = combineddata.groupby(['Local thickness'])['Probability Density'].std().reset_index()
print(gstd)

#Real
paths = 'C:\\Users\\DELL\\Desktop\\Re2\\Test\\Overall test.xlsx' 
df = pd.read_excel(paths)
df1 = df[df['Category'] == 1]
df2 = df[df['Category'] == 2]
df3 = df[df['Category'] == 3]

#change dflist
dflist = df1.Label
#Change replace
list2 = [y.replace('.png', '_LocThk.xlsx') for y in dflist]
#Change folder
folder = "C:\\Users\\DELL\\Desktop\\Re2\\Test\\Local thickness background\\Excel with range\\kde100"

files2 = [f for f in listdir(folder)]

combineddata = pd.DataFrame()
for file in list2:
    if file in files2:
        data = pd.read_excel(os.path.join(folder, file), header = None, engine='openpyxl')
        #Change iloc
        data = data.iloc[1:, 1:]
        
        combineddata = combineddata.append(data)
#Change header
combineddata.columns = ['Local thickness', 'Probability Density']
combineddata['Local thickness'] = pd.to_numeric(combineddata['Local thickness'])
combineddata['Probability Density'] = pd.to_numeric(combineddata['Probability Density'])
rcombineddata = combineddata.groupby(['Local thickness'])['Probability Density'].mean().reset_index()
rstd = combineddata.groupby(['Local thickness'])['Probability Density'].std().reset_index()




plt.xlabel("Local thickness")
plt.ylabel("Probability Density")

#plt.savefig('K:\RTP\GAN\Lltn3.png')
plt.errorbar(gcombineddata['Local thickness'], gcombineddata['Probability Density'], color ='m', label = 'Generated', yerr= gstd['Probability Density'], ecolor='wheat')
plt.errorbar(rcombineddata['Local thickness'], rcombineddata['Probability Density'], color ='black', label = 'Real', yerr= rstd['Probability Density'], ecolor='khaki')
plt.xlim(0, 160)
plt.ylim(0, )
plt.legend()
plt.show()

#rm = rcombineddata.groupby(['Value'])['Count'].describe().reset_index()

#plt.errorbar(rcombineddata2.Value, rcombineddata2.Count, yerr= rs.Count)
#plt.show()

#d = rcombineddata.loc[rcombineddata.index.repeat(rcombineddata['Count'])]

#d.Value.plot.density(color = 'black', label = 'Real')
"""
kde1= KDEUnivariate(rcombineddata2.Value)
kde_noweight = KDEUnivariate(rcombineddata2.Value)
kde1.fit(weights=rcombineddata2.Count, fft=False)
kde_noweight.fit()
plt.plot(kde1.support, kde1.density)
plt.plot(kde_noweight.support, kde_noweight.density)
plt.legend(['weighted', 'unweighted'])

"""