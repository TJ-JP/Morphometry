# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 04:11:32 2022

@author: DELL
"""
"""
import pandas as pd
from matplotlib import pyplot as plt
rdf = pd.read_csv('C:\\Users\\DELL\\Desktop\\Re2\\Mike\\original_patches256x256\\Beta.csv')
gdf = pd.read_csv('C:\\Users\\DELL\\Desktop\\Re2\\Mike\\original_patches256x256\\Beta.csv')
A = rdf['%Area']
B = gdf['%Area']
B.plot.density(color = 'm', label = 'Generated')
A.plot.density(color = 'black', label = 'Real')
#plt.hist(A, bins = 100, align='right', color='black', label = 'Real')
#plt.hist(B, bins = 100, align='right', color='m', label = 'generated')
plt.xlim(0, )
plt.ylim(0, )
plt.xlabel('Beta (% area)')
plt.ylabel('Autocorrelation')
plt.legend()
plt.savefig('C:\\Users\\DELL\\Desktop\\Re2\\Mike\\Beta_pd.jpg', dpi = 1200)
plt.show() 

"""

import pandas as pd
from matplotlib import pyplot as plt
import os
from os import path
from os import listdir
from statsmodels.nonparametric.kde import KDEUnivariate
import timeit
import openpyxl
import matplotlib.font_manager as font_manager
start = timeit.default_timer()

#Your statements here
"""

def combine_data(folder):
    files = [f for f in listdir(folder)]
    combineddata = pd.DataFrame()
    for file in files:
            data = pd.read_excel(os.path.join(folder, file), header=None)
            #data = pd.read_csv(os.path.join(folder, file), delimiter = '\t', header = None, encoding = 'unicode_escape', engine ='python')
           
            # Change iloc
            data = data.iloc[1:, 1:]
              
            combineddata = combineddata.append(data)
    #Change header
    combineddata.columns = ['x', 'y']
    combineddata['x'] = pd.to_numeric(combineddata['x'])
    combineddata['y'] = pd.to_numeric(combineddata['y'])
    mean = combineddata.groupby(['x'])['y'].mean().reset_index()
    std = combineddata.groupby(['x'])['y'].std().reset_index()
    return mean, std


def plot2(x, rm, rs, gm, gs):
    plt.figure(figsize=(15,10))
    plt.xlabel("Direction (°)",labelpad=10,fontsize=28,weight='bold')
    plt.ylabel("Probability",labelpad=10,fontsize=28,weight='bold')
    
   
    plt.plot(x, gm,  label='Directionality',linewidth='3')
    plt.fill_between(x, gm- gs, gm+ gs,  alpha=0.2)
    
    plt.plot(x, rm,  label='Original',linewidth='3',alpha=0.7)
    plt.fill_between(x, rm- rs, rm+ rs, alpha=0.2)
    
    plt.errorbar(gm['R'], gm['Autocorrelation'], color ='m', label = 'Generated', yerr= gs['Autocorrelation'], ecolor='lightskyblue')
    plt.errorbar(rm['R'], rm['Autocorrelation'], color ='black', label = 'Real', yerr= rs['Autocorrelation'], ecolor='wheat')
    plt.xlim(0, 145)
    plt.ylim(0, 0.6)
    font = font_manager.FontProperties(family='Times New Roman',
                                   weight='bold',
                                   style='normal', size=28)
    plt.grid(False)
    plt.legend( prop=font,loc='upper right', labels=['Synthetic', 'Original'])
    plt.savefig('G:\\GAN\\stylegan\\tSNE\\Excel\\autocorrelation.jpg', dpi = 600)
    plt.show()
    
    
 
realmean, realstd = combine_data("J:\\UK GAN Work Pending\\Original Images\\256_no_rot\\KDE local thickness lines\\Bimodal\\")

realmeannp = realmean.to_numpy()
realmeannp=realmeannp[:,-1]

realstdnp  = realstd.to_numpy()
realstdnp=realstdnp[:,-1]
realmeannp.shape
realstdnp

wb = openpyxl.Workbook()
name = 'J:\\UK GAN Work Pending\\Original Images\\256_no_rot\\Bi_KDE local thickness lines.xlsx'
wb.save(name)
with pd.ExcelWriter(name, engine = 'openpyxl', mode = 'a') as writer:
    realmean.to_excel(writer, sheet_name = 'mean', index = False, header = True)
    realstd.to_excel(writer, sheet_name = 'std', index = False, header = True)
    writer.save()
 
#genmean, genstd = combine_data("G:\\UK\\patches\\Copy\\cc\\Directionality\\excel\\")

#genmeannp = genmean.to_numpy()

#x=genmeannp[:,0]
#x.shape

#genmeannp=genmeannp[:,-1]
#genstdnp  = genstd.to_numpy()
#genstdnp =genstdnp [:,-1]

#plot2(x, genmeannp, genstdnp)






stop = timeit.default_timer()

print('Time: ', stop - start)  

"""
gdf = pd.read_excel('G:\\UK\\patches\\Morphometry\\Original\\Overall.xlsx')

A = gdf['Alpha']
Akde1= KDEUnivariate(A)
Akde_noweight = KDEUnivariate(A)
Akde_noweight.fit()

B = gdf['Beta']
Bkde1= KDEUnivariate(B)
Bkde_noweight = KDEUnivariate(B)
Bkde_noweight.fit()

L = gdf['Lamellar']
Lkde1= KDEUnivariate(L)
Lkde_noweight = KDEUnivariate(L)
Lkde_noweight.fit()
E = gdf['Equiaxed']
Ekde1= KDEUnivariate(E)
Ekde_noweight = KDEUnivariate(E)
Ekde_noweight.fit()


Adf = pd.DataFrame(Akde_noweight.support, Akde_noweight.density)
Adf.to_excel("G:\\UK\\patches\\Morphometry\\Original\\Alpha prob.xlsx")

Bdf = pd.DataFrame(Bkde_noweight.support, Bkde_noweight.density)
Bdf.to_excel("G:\\UK\\patches\\Morphometry\\Original\\Beta prob.xlsx")

Ldf = pd.DataFrame(Lkde_noweight.support, Lkde_noweight.density)
Ldf.to_excel("G:\\UK\\patches\\Morphometry\\Original\\Lamellar prob.xlsx")
Edf = pd.DataFrame(Ekde_noweight.support, Ekde_noweight.density)
Edf.to_excel("G:\\UK\\patches\\Morphometry\\Original\\\\Equiaxed prob.xlsx")

plt.plot(Ekde_noweight.support, Ekde_noweight.density)

#plt.legend(['weighted', 'unweighted'])

