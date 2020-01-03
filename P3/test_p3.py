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

from pandas.io.json import json_normalize
# json_normalize(sample_object)


with open("response_1577463161987_final.json") as json_file:
    data = json.load(json_file)
    
#print(data)


#sample_object = {'data'}
#json_normalize(sample_object)
 

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
            
    flatten(y)
    return out

   
print(data)
print(len(data['items']))

for item in data['items']:
    print(item)
    
print(type(item))

#dic_flattened = [flatten_json(d) for d in json['items']]
dic_flattened = flatten_json(data['items'][0])       
    
print(dic_flattened)


df= json_normalize(dic_flattened)
json_normalize(data)
    
print(json.dumps(data, indent=2))

df = json_normalize(data['items'])
#df.loc[8]

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








    