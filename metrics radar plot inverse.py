# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:27:09 2022

@author: DELL
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
import os
from os import listdir



folder = 'J:/Jp/Metrics excel/testing/256/'
files = [f for f in listdir(folder)]
files = os.listdir(folder)

Aug = []
for file in files:
    if file.endswith('.xlsx'):
        df = pd.read_excel(os.path.join(folder, file))
        df.yis50k_mean = df.yis50k_mean.iloc[-1]*210.605090750457
        df.yppl2_wend = df.yppl2_wend.iloc[-1]*22.902669421165573
        df.ykid50k_full = df.ykid50k_full.iloc[-1]*1499.9054734290519
        df.ypr50k3_full_precision = df.ypr50k3_full_precision.iloc[-1]*667.8063982647849
        df.yfid50k_full = df.yfid50k_full.iloc[-1]*1.748389522204691
        df.drop(df.iloc[:,0:2], inplace = True, axis = 1)
        df.drop(df.iloc[:,1:2], inplace = True, axis = 1)
        test = df.values[-1].tolist()
        Aug.append(test)




categories = ['IS', 'PPL_WEND', 'KID', 'PR', 'FID']
categories = [*categories, categories[0]]
bg = Aug[0]
print(bg)
bg = [*bg, bg[0]]
bgc = Aug[1]
bgc = [*bgc, bgc[0]]
bgcf = Aug[2]
bgcf = [*bgcf, bgcf[0]]
bgcfn = Aug[3]
bgcfn = [*bgcfn, bgcfn[0]]
blit = Aug[4]
blit = [*blit, blit[0]]
color = Aug[5]
color = [*color, color[0]]
cutout = Aug[6]
cutout = [*cutout, cutout[0]]
filte = Aug[7]
filte = [*filte, filte[0]]
geom = Aug[8]
geom = [*geom, geom[0]]
noise = Aug[9]
noise = [*noise, noise[0]]

label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(bg))

plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
plt.scatter(label_loc, bg, label='bg')
plt.scatter(label_loc, bgc, label='bgc')
plt.scatter(label_loc, bgcf, label='bgcf')
plt.scatter(label_loc, bgcfn, label='bgcfn')
plt.scatter(label_loc, blit, label='blit')
plt.scatter(label_loc, color, label='color')
plt.scatter(label_loc, cutout, label='cutout')
plt.scatter(label_loc, filte, label='filter')
plt.scatter(label_loc, geom, label='geom')
plt.scatter(label_loc, noise, label='noise')

plt.title('Metrics scores at 1000th iteration', size=20)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
plt.tick_params(labelsize=12)
plt.legend(bbox_to_anchor=(1, 1), fontsize = 12)
plt.tight_layout()
#plt.savefig(folder + '1000th.png', dpi = 1200)
plt.show()



