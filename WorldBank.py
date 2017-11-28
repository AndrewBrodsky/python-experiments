
# coding: utf-8

# In[ ]:

import csv
import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

df = pd.read_csv("OneDrive/Andrew Academy/World Bank/data/WDI.csv")
df.shape


# In[ ]:

df.iloc[::50000, :]


# In[ ]:

df = df.rename(columns={'2014 [YR2014]' : 'Value_2014'})

dupes = df.duplicated(subset=['Country Code', 'Series Code'])
dupesframe = pd.DataFrame(dupes , columns = ["IsDupe"])
dupesframe['IsDupe'].value_counts()


# In[ ]:

df[dupesframe.IsDupe == True]


# In[ ]:

newdf = df[dupesframe.IsDupe == False]
newdf.shape


# In[ ]:

newdf.iloc[::50000, :]


# In[ ]:

table = newdf.pivot(index="Country Code", columns = "Series Code", values="Value_2014")

table.iloc[::25, :]


# In[ ]:

table.dtypes.value_counts()


# In[ ]:

table1 = table.apply(pd.to_numeric, errors='coerce')
table1.iloc[::25, :]
    


# In[ ]:

table1['AG.CON.FERT.PT.ZS'].describe()


# In[ ]:

itercols = iter(table1)
next(itercols)

#for col in itercols:
#    print df[col]
        
        #column.isnull().sum()



# In[ ]:

WBdict = pd.read_csv("OneDrive/Andrew Academy/World Bank/data/WDI_DataDict.csv", usecols = ['Code', 'Indicator Name'])
WBdict = WBdict.rename(columns={'Indicator Name' : 'Name'})
                 
WBdict.shape


# In[ ]:

WBdict.iloc[::100, :]


# In[ ]:

d= dict([(key, value) for key, value in zip(WBdict.Code, WBdict.Name)])

print {k: d[k] for k in d.keys()[:10]}


# In[ ]:

import random

iterator = 0
myxlabel =""



while iterator<5:

    series1 = random.choice(d.keys())
    
    for code, name in d.iteritems():
        if code == series1:
            myxlabel = name
                
    table1.hist(column= series1)
    plt.xlabel(myxlabel)
    plt.ylabel("Frequency")
    plt.show()
    
    iterator +=1


# In[ ]:

iterator = 0

while iterator<5:
    series1 = random.choice(d.keys())
    series2 = random.choice(d.keys())

    xs = table1[series1]
    ys = table1[series2]

    for code, name in d.iteritems():
        if code == series1:
             myxlabel = name
        if code==series2:
             myylabel = name

    #%matplotlib notebook
    
    plt.xlabel(myxlabel)
    plt.ylabel(myylabel)

    plt.scatter(xs,ys)
    plt.show()

    iterator += 1


# In[ ]:

Interesting_Series = ['NV.IND.TOTL.KD', 'SH.STA.ORCF.ZS', 'SE.TER.TCHR.FE.ZS']
myxlabel =""


# In[ ]:

for series in Interesting_Series:
    
    for code, name in d.iteritems():
        if code == series:
             myxlabel = name
                
    #%matplotlib notebook
    table1.hist(column= series)
    plt.xlabel(myxlabel)
    plt.ylabel("Frequency") 
    plt.show()


# In[ ]:




# In[ ]:

#series1 = 'SP.DYN.LE00.IN'
#series2 = 'NY.GDP.PCAP.PP.CD'

series1 = 'SE.SEC.PROG.FE.ZS'
series2 = 'AG.LND.PRCP.MM'

xs = table1[series1]
ys = table1[series2]

for code, name in d.iteritems():
    if code == series1:
        myxlabel = name
    if code==series2:
        myylabel = name

#%matplotlib notebook

plt.xlabel(myxlabel)
plt.ylabel(myylabel)

plt.scatter(xs,ys)
plt.show()

