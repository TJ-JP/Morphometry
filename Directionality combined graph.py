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
dflist = df3.Label
#Change replace
list2 = [y.replace('.png', '.xls') for y in dflist]
#Change folder
folder = "C:\\Users\\DELL\\Desktop\\Re2\\Stylegan GI\\Directionality\\Excel"

files2 = [f for f in listdir(folder)]
combineddata = pd.DataFrame()
for file in list2:
    if file in files2:
        data = pd.read_csv(os.path.join(folder, file), delimiter = '\t', header = None, encoding = 'unicode_escape', engine ='python')
        #Change iloc
        data = data.iloc[1:, 0:2]
        
        combineddata = combineddata.append(data)
#Change header
combineddata.columns = ['Direction', 'Amount']
combineddata['Direction'] = pd.to_numeric(combineddata['Direction'])
combineddata['Amount'] = pd.to_numeric(combineddata['Amount'])
combineddata2 = combineddata.groupby(['Direction']).Amount.mean().reset_index()

#Real
paths = 'C:\\Users\\DELL\\Desktop\\Re2\\Test\\Overall test.xlsx' 
df = pd.read_excel(paths)
df1 = df[df['Category'] == 1]
df2 = df[df['Category'] == 2]
df3 = df[df['Category'] == 3]

#change dflist
dflist = df3.Label
#Change replace
list2 = [y.replace('.png', '.xls') for y in dflist]
#Change folder
folder = "C:\\Users\\DELL\\Desktop\\Re2\\Test\\Directionality\\Excel"

files2 = [f for f in listdir(folder)]
combineddata = pd.DataFrame()
for file in list2:
    if file in files2:
        data = pd.read_csv(os.path.join(folder, file), delimiter = '\t', header = None, encoding = 'unicode_escape', engine ='python')
        #Change iloc
        data = data.iloc[1:, 0:2]
        
        combineddata = combineddata.append(data)
#Change header
combineddata.columns = ['Direction', 'Amount']
combineddata['Direction'] = pd.to_numeric(combineddata['Direction'])
combineddata['Amount'] = pd.to_numeric(combineddata['Amount'])
rcombineddata2 = combineddata.groupby(['Direction']).Amount.mean().reset_index()



plt.plot(rcombineddata2.Direction, rcombineddata2.Amount, color ='black', label = 'Real')
plt.plot(combineddata2.Direction, combineddata2.Amount, color ='m', label = 'Generated')

plt.xlabel("Direction")
plt.ylabel("Amount")
plt.legend()
#plt.savefig('K:\RTP\GAN\Lltn3.png')
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