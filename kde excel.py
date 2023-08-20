# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:45:53 2022

@author: DELL
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 
import os
from os import path
from os import listdir
from statsmodels.nonparametric.kde import KDEUnivariate
"""
rpaths = 'C:\\Users\\DELL\\Desktop\\Re2\\Test\\Overall test.xlsx' 
rdf = pd.read_excel(rpaths)

rdf1 = rdf[rdf['Category'] == 1]
rdf2 = rdf[rdf['Category'] == 2]
rdf3 = rdf[rdf['Category'] == 3]
#change rdflist
rdflist = rdf1.Label
rlist2 = [y.replace('.png', '') for y in rdflist]
"""
rfolder = "J:\\UK GAN Work Pending\\Generated Images\\512_bgcfnc\\Bimodal local thickness lines\\Excel"

rfiles2 = [f for f in listdir(rfolder)]
rcombineddata = pd.DataFrame()

# loop over the list of csv files
for rfile in rfiles2:
        #rdata = pd.read_excel(os.path.join(rfolder, rfile), header=None, engine ='python')
        rdata = pd.read_csv(os.path.join(rfolder, rfile), delimiter = '\t', header = 0, encoding = 'unicode_escape', engine ='python')
        rdata = rdata.iloc[:, :]
        kde1= KDEUnivariate(rdata['Value'])
        kde_noweight = KDEUnivariate(rdata['Value'])
        kde1.fit(weights=rdata[rdata.columns[2]], fft=False)
        kde_noweight.fit()
        dict = {'x': kde1.support, 'y': kde1.density} 
        df = pd.DataFrame(dict)
        name = rfile.replace('.xls', '')
        df.to_excel('J:\\UK GAN Work Pending\\Generated Images\\512_bgcfnc\\Bi_KDE local thickness lines\\' + name +'.xlsx')
print(df)


 
"""
     import pandas as pd
     from matplotlib import pyplot as plt
     import numpy as np 
     import os
     from os import path
     from os import listdir
     from statsmodels.nonparametric.kde import KDEUnivariate
     file = 'C:\\Users\\DELL\\Desktop\\Re2\\Mike\\epoch1000\\Alpha.csv'
     rdata = pd.read_csv(file, delimiter = ',', header = 0, encoding = 'unicode_escape', engine ='python')
     rdata = rdata.iloc[:, :]
     print(rdata)
     kde_noweight = KDEUnivariate(rdata['%Area'])
     kde_noweight.fit()
     x = kde_noweight.support
     y = kde_noweight.density
     dict = {'x': kde_noweight.support, 'y': kde_noweight.density} 
     df = pd.DataFrame(dict)
     df.to_excel('C:\\Users\\DELL\\Desktop\\Re2\\Mike\\epoch1000\\Alphakde.xlsx')

"""

#rcombineddata2 = rcombineddata.groupby(['Value']).Count.mean().reset_index()

#rm = rcombineddata.groupby(['Value'])['Count'].describe().reset_index()

#plt.errorbar(rcombineddata2.Value, rcombineddata2.Count, yerr= rs.Count)
#plt.show()

#d = rcombineddata.loc[rcombineddata.index.repeat(rcombineddata['Count'])]

#d.Value.plot.density(color = 'black', label = 'Real')
"""
kde1= KDEUnivariate(rcombineddata2.Value
)
kde_noweight = KDEUnivariate(rcombineddata2.Value
)
kde1.fit(weights=rcombineddata2.Count, fft=False)
kde_noweight.fit()
plt.plot(kde1.support, kde1.density)
plt.plot(kde_noweight.support, kde_noweight.density)
plt.legend(['weighted', 'unweighted'])

"""