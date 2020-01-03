#!/usr/bin/env python3

import requests
import json
import pandas as pd
import math 
import numpy as np
from pandas.io.json import json_normalize
from pandas import DataFrame
import matplotlib as plt

#-------------------------------------------------------------
# CONFIGURATION 
#-------------------------------------------------------------
# API Endpoint
API_SEARCH_URL = 'https://api.smk.dk/api/v1/art/search/'

# Paramerters to use whne searching
PARAMS = {
    'keys': 'vilhelm hammershøi' ,
    'rows': '200', ## TODO: 200
    'offset': '0'
}

#-------------------------------------------------------------
# MAIN PROGRAM 
#-------------------------------------------------------------
def main():
    json_data  = get_json_data()
    items_json = items_json_with_defaults( json_data ) 

    list_of_documents(    items_json )
    list_of_exhibitions(  items_json )
    all_data_with_counts( items_json )


#-------------------------------------------------------------
def get_json_data():
    print("-------------------------- GET JSON DATA ----------------------")
    resp = requests.get(API_SEARCH_URL, PARAMS)
    json_data = resp.json()
    #print( json.dumps( json_data, sort_keys=False, indent=4 ) )
    print("------------------------------------------------\n\n")
    return json_data

# ---------------------------------------------------------------------
def items_json_with_defaults( json_data ):
    """ Create a new JSON object containing only the item records, and with default values """
    print("-------------------------- GET ITEMS JSON WITH DEFAULTS ----------------------")
    # Create a Dataframe where all nested structures are just JSON 
    df = pd.DataFrame(json_data['items'])

    # Set missing columns meaningfull to default values
    df['documentation'] = df.apply( lambda row: set_default_list(row['documentation'] ), axis=1 )
    df['exhibitions']   = df.apply( lambda row: set_default_list(row['exhibitions']   ), axis=1 )

    # Dump DataFrame to new json, now with default values
    new_json_str = df.to_json(orient='records')
    new_json = json.loads(new_json_str)

    return new_json


#-------------------------------------------------------------
def list_of_documents( item_json_data ):
    print("-------------------------- LIST OF DOCUMENTS ----------------------")
    doc_df = json_normalize(item_json_data, record_path='documentation', meta=['id' ], meta_prefix="item.", errors='ignore')
    print( doc_df.head() )
    print( doc_df.dtypes )
    print("------------------------------------------------\n\n")


#-------------------------------------------------------------
def list_of_exhibitions( item_json_data ):
    print("-------------------------- LIST OF EXHIBITIONS ----------------------")
    exhibitions_df = json_normalize(item_json_data, record_path='exhibitions', meta=['id' ], meta_prefix="item.", errors='ignore')
    print( exhibitions_df.head() )
    print( exhibitions_df.dtypes )
    print("------------------------------------------------\n\n")

#-------------------------------------------------------------
def all_data_with_counts( item_json_data ):
    print("-------------------------- COUNT NUMBER OF EXHIBITIONS AND DOCUMENTATIONS ----------------------")
    all_df = pd.DataFrame(item_json_data)
    all_df['number_of_exhibitions'] = all_df.apply( lambda row: number_in_list(row['exhibitions']   ), axis=1 )
    all_df['number_of_documents']   = all_df.apply( lambda row: number_in_list(row['documentation'] ), axis=1 )

    #print( all_df.head() )
    print( all_df )
    print( all_df.dtypes)
    print("------------------------------------------------\n\n")


def set_default_list( value ):
    """ It the passed value is not a list object, simply return an empty list """
    empty_list = []
    if type(value) is not list:
        return empty_list
    return value

# NOT USED!
def set_default( value, default_value ):
    if value is None:
        print('NONE: ', type(value ))
        return default_value

    if value is float:
        if math.isnan(value):
            print('NaN: ', type(value ))
            return default_value

    print('Type: ', type(value ))

    return value

    
#-------------------------------------------------------------
def number_in_list( mylist ) :
    """ Return the number of items in a list. If the value is not a list, just return 0 """
    mylen = 0
    if type(mylist) is list:
        mylen = len( mylist) 
    return mylen



# Now run the program (Should be last line of this file!)
main()