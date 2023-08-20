# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:02:32 2022

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
is50k = []
ppl2_wend = []
kid50k = []
pr50k3 = []
fid50k = []
x = []
Aug = []
for file in files:
    if file.endswith('256.xlsx'):
        Aug.append(file[:-8])
        df = pd.read_excel(os.path.join(folder, file))
        x.append(df.X)
        test = df.values[-1].tolist()
        is50 = df.yis50k_mean.iloc[-1]
        is50k.append(is50)
        ppl2_wen = df.yppl2_wend.iloc[-1]
        ppl2_wend.append(ppl2_wen)
        kid50 = df.ykid50k_full.iloc[-1]
        kid50k.append(kid50)
        pr50k = df.ypr50k3_full_precision.iloc[-1]
        pr50k3.append(pr50k)
        fid50 = df.yfid50k_full.iloc[-1]
        fid50k.append(fid50)

#Sort scores and plot
"""
X = ['bg', 'bgc', 'bgcf', 'bgcfn', 'bgcfnc', 'blit', 'color', 'cutout', 'filter', 'geom', 'noise']
ist = is50k
is_y = np.argsort(ist)
ist.sort()
is_order = [x for _,x in sorted(zip(is_y,X))]

ppl = ppl2_wend
ppl_y = np.argsort(ppl)
ppl.sort()
ppl_order = [x for _,x in sorted(zip(ppl_y,X))]

kid = kid50k
kid_y = np.argsort(kid)
kid.sort()
kid_order = [x for _,x in sorted(zip(kid_y,X))]

pr = pr50k3
pr_y = np.argsort(pr)
pr.sort()
pr_order = [x for _,x in sorted(zip(pr_y,X))]

fid = fid50k
fid_y = np.argsort(fid)
fid.sort()
fid_order = [x for _,x in sorted(zip(fid_y,X))]


data = pd.DataFrame({'FID': fid, 'FID_order': fid_order,
                     'IS': ist, 'IS_order': is_order,
                     'KID': kid, 'KID_order': kid_order,
                     'PPL': ppl, 'PPL_order': ppl_order,
                     'PR': pr, 'PR_order': pr_order})

# writing to Excel
Combined_data = pd.ExcelWriter(folder + 'sorted.xlsx')
  
# write students data to excel
data.to_excel(Combined_data)
  
# save the students result excel
Combined_data.save()

print(data)



plt.plot(data.FID, data.FID_order, **{'marker': 'o'})
plt.xlabel("FID", fontsize=18)  # add X-axis label
plt.ylabel('Augmentations', fontsize=18) 
plt.savefig(folder + 'fid_sort.png', dpi = 1200)
plt.show()
"""

#Conversion factor for 512 metrics
"""
#print(500/max(ppl2_wend))
#print(500/max(kid50k))
#print(500/max(pr50k3))
#print(500/max(fid50k))
        is50 = df.yis50k_mean.iloc[-1]*218.23723300656667
        ppl2_wen = df.yppl2_wend.iloc[-1]*47.45852986348595
        kid50 = df.ykid50k_full.iloc[-1]*813.2243596830897
        pr50k = df.ypr50k3_full_precision.iloc[-1]*727.35735404007
        fid50 = df.yfid50k_full.iloc[-1]*1.0413415023530714
        """
#Conversion factor for 256 metrics
"""
        is50 = df.yis50k_mean.iloc[-1]*210.605090750457
        is50k.append(is50)
        ppl2_wen = df.yppl2_wend.iloc[-1]*22.902669421165573
        ppl2_wend.append(ppl2_wen)
        kid50 = df.ykid50k_full.iloc[-1]*1499.9054734290519
        kid50k.append(kid50)
        pr50k = df.ypr50k3_full_precision.iloc[-1]*667.8063982647849
        pr50k3.append(pr50k)
        fid50 = df.yfid50k_full.iloc[-1]*1.748389522204691
        """
#Plot
"""
categories = ['bg', 'bgc', 'bgcf', 'bgcfn', 'bgcfnc', 'blit', 'color', 'cutout', 'filter', 'geom', 'noise']
categories = [*categories, categories[0]]
IS = is50k
IS = [*IS, IS[0]]
PPL_WEND = ppl2_wend
PPL_WEND = [*PPL_WEND, PPL_WEND[0]]
KID = kid50k
KID = [*KID, KID[0]]
PR = pr50k3
PR = [*PR, PR[0]]
FID = fid50k
FID = [*FID, FID[0]]
label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(IS))

plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
plt.plot(label_loc, FID, label='FID*1.75')
plt.plot(label_loc, IS, label='IS*210.61')
plt.plot(label_loc, KID, label='KID*1499.91')
plt.plot(label_loc, PPL_WEND, label='PPL_WEND*22.90')
plt.plot(label_loc, PR, label='PR*667.81')

plt.title('Metrics scores at 1000th iteration', size=20)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
plt.tick_params(labelsize=12)
plt.legend(bbox_to_anchor=(1, 1), fontsize = 12)
plt.tight_layout()
#plt.savefig(folder + '1000th.png', dpi = 1200)
plt.show()

"""


