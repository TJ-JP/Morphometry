# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 06:26:11 2022

@author: DELL
"""

import pandas as pd
from matplotlib import pyplot as plt
import os
from os import path
from os import listdir
from statsmodels.nonparametric.kde import KDEUnivariate
import openpyxl
import timeit

start = timeit.default_timer()

#Alpha, beta, laths, equiaxed, enter 4 variables for each to store
def singlecolumn():
    paths = input("Enter overall excel location: ")
    df = pd.read_excel(paths)
    df1 = df[df['Category'] == 1]
    df2 = df[df['Category'] == 2]
    df3 = df[df['Category'] == 3]
    dfs = {'1' : df1, '2' : df2, '3' : df3}
    select = input("Enter category: ")
    whichdataframe = dfs[select]
    Alpha =  whichdataframe.Alpha
    Beta = whichdataframe.Beta
    Laths = whichdataframe.Laths
    Equiaxed = whichdataframe.Equiaxed
    return Alpha, Beta, Laths, Equiaxed

#Enter 4 variables for each

A, B, C, D = singlecolumn()

data = A
kde_noweight = KDEUnivariate(data)
kde_noweight.fit()
x = kde_noweight.support
y = kde_noweight.density
dict = {'x': kde_noweight.support, 'y': kde_noweight.density} 
df = pd.DataFrame(dict)
df.to_excel('C:\\Users\\DELL\\Desktop\\Re2\\Stylegan GI\\Alpha_kde_df1.xlsx')


def plot1(A, B):
    A.plot.density(color = 'm', label = 'Generated')
    B.plot.density(color = 'black', label = 'Real')
    #plt.hist(rx, bins = 100, align='right', color='black', edgecolor='black', label = 'Real')
    #plt.hist(x, bins = 100, align='right', color='m', edgecolor='black', label = 'generated')
    plt.xlim(0, )
    plt.ylim(0, )
    plt.xlabel('Beta (% area)')
    plt.ylabel('Probability Density')
    plt.legend()
    #plt.savefig('K:\RTP\GAN\Beta1.png')
    plt.show() 
    

#Combine kde data
def combine_data(folder):
    paths = input("Enter overall excel location: ")
    df = pd.read_excel(paths)
    df1 = df[df['Category'] == 1]
    df2 = df[df['Category'] == 2]
    df3 = df[df['Category'] == 3]
    dfs = {'1' : df1, '2' : df2, '3' : df3}
    select = input("Enter category: ")
    whichdataframe = dfs[select]
    dflist = whichdataframe.Label
    
    # Change replace
    list2 = [y.replace('.png', '.xlsx') for y in dflist]
    #folder = input("Enter what you want to analyse: ")
    files2 = [f for f in listdir(folder)]
    combineddata = pd.DataFrame()
    for file in list2:
        if file in files2:
            data = pd.read_excel(os.path.join(folder, file), header=None)
            # Change iloc
            data = data.iloc[1:, 1:]

            combineddata = combineddata.append(data)
    #Change header
    combineddata.columns = ['Directionality', 'Probability Density']
    combineddata['Directionality'] = pd.to_numeric(combineddata['Directionality'])
    combineddata['Probability Density'] = pd.to_numeric(combineddata['Probability Density'])
    mean = combineddata.groupby(['Directionality'])['Probability Density'].mean().reset_index()
    std = combineddata.groupby(['Directionality'])['Probability Density'].std().reset_index()
    return mean, std

#Give different variable name for each mean and std


def plot2(A, B):
    plt.xlabel("Directionality")
    plt.ylabel("Probability Density")
    
    plt.errorbar(A['Directionality'], A['Probability Density'], color ='m', label = 'Generated', yerr= B['Probability Density'], ecolor='wheat')

    plt.xlim(0, 160)
    plt.ylim(0, )
    plt.legend()
    plt.show()

#cmean, cstd = combine_data("C:\\Users\\DELL\\Desktop\\Re2\\Stylegan GI\\Directionality\\kde\\")
"""
wb = openpyxl.Workbook()
wb.save('C:\\Users\\DELL\\Desktop\\Re2\\Stylegan GI\\Directionality\\KDE_df1.xlsx')
with pd.ExcelWriter('C:\\Users\\DELL\\Desktop\\Re2\\Stylegan GI\\Directionality\\KDE_df1.xlsx', engine = 'openpyxl', mode = 'a') as writer:
    cmean.to_excel(writer, sheet_name = 'mean', index = False, header = True)
    cstd.to_excel(writer, sheet_name = 'std', index = False, header = True)
    writer.save()
"""
stop = timeit.default_timer()

print('Time: ', stop - start)  





