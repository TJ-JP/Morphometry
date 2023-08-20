# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:50:16 2022

@author: Priya
"""
"""
import pandas as pd
from matplotlib import pyplot as plt

path = 'K:\RTP\GAN\Overall.xlsx'
df = pd.read_excel(path)

df1 = df[df['Category'] == 1]
df2 = df[df['Category'] == 2]
df3 = df[df['Category'] == 3]

plt.hist(df3.Equiaxed, bins = 100, align='right', color='darkviolet', edgecolor='black')
plt.xlabel('Equiaxed (% area)')
plt.ylabel('Counts')
plt.savefig('K:\RTP\GAN\Equiaxed3.png')
plt.show() 
"""


"""
# import necessary libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 
import os
import glob


folder = "K:\RTP\GAN\Directionality\Histo\Three"

files = os.listdir(folder)

df = pd.DataFrame()
 
# loop over the list of csv files
for file in files:
    data = pd.read_csv(os.path.join(folder, file), delimiter = '\t', header = None, encoding = 'unicode_escape', engine ='python')
    data = data.iloc[1:, 0:2]


    df = df.append(data)
#df.columns = df.iloc[0]
df.columns = ['Direction', 'Amount']

df['Direction'] = pd.to_numeric(df['Direction'])
df['Amount'] = pd.to_numeric(df['Amount'])
df2 = df.groupby(['Direction']).Amount.mean().reset_index()
print(df2)
plt.bar(df2.Direction, df2.Amount, color ='blue')
 
plt.xlabel("Direction (°)")
plt.ylabel("Amount")
plt.savefig('K:\RTP\GAN\Direction3.png')
plt.show()
"""

"""
# import necessary libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 
import os
import glob


folder = "K:\RTP\GAN\local thickness\Inversed"

files = os.listdir(folder)
df = pd.DataFrame()
 
# loop over the list of csv files
for file in files:
    data = pd.read_csv(os.path.join(folder, file), delimiter = '\t', header = None)
    data = data.iloc[1:, 1:]


    df = df.append(data)
#df.columns = df.iloc[0]
df.columns = ['Value', 'Count']

df['Value'] = pd.to_numeric(df['Value'])
df['Count'] = pd.to_numeric(df['Count'])
df2 = df.groupby(['Value']).Count.mean().reset_index()

plt.bar(df2.Value, df2.Count, color ='slategray')
 
plt.xlabel("Value")
plt.ylabel("Count")
plt.savefig('K:\RTP\GAN\localthickness1.png')
plt.show()

"""

