#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:16:32 2019

@author: je
"""

from pandas import DataFrame
import matplotlib as plt
import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize
import requests

with open("response_1575208342694.json") as json_file:
    data = json.load(json_file)
   
print(data)
print(len(data['items']))

for item in data['items']:
    print(item)
    
print(type(item))
    
print(json.dumps(data, indent=2))

df = json_normalize(data['items'])
df.loc[8]

df.get_dtype_counts()



df.loc[0:, 'acquisition_date_precision'].head(10)
regex = r'^(\d{4})'
df['acquisition_year'] = df['acquisition_date_precision'].str.extract(r'^(\d{4})', expand=False)
df.loc[0:, 'acquisition_year'].head(10)




#df['acquisition_date_precision'] = pd.to_numeric(acquisition_years)
#df['acquisition_date_precision'].dtype
# to_drop = []

print(type(df))
print(df.shape)
print(df.size)
print(df.columns)
print(df.dtypes)

for name in df.columns:
    print(name)
    

# delen med anskaffelsesår - vælges til visualisering.
df.groupby('acquisition_year').count()

ax = df['acquisition_year'].value_counts().plot(kind='bar', title="Acquisitions per year")
ax.set_xlabel('acquisition year')
ax.set_ylabel('count')








    