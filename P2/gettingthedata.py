#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:36:57 2019

This program only download data from The Guardian
processing the acquired data happens in another file.. 

@author: je
"""

import os
import json
import requests
from os import makedirs
from os.path import join, exists
from datetime import date, timedelta

# ---------------------
# CONSTANT DEFINITIONS 
# ---------------------------
# ARTICLE DATA DIRECTORY:
DATADIR = str( os.getenv('OPENDATASCIENCE_DATADIR') )
          # This creates two subdirectories called "theguardian" and "collection"  
ARTICLES_DIR = join( DATADIR,'theguardian', 'collection')

# API Key is defined in the environement. 
# Define using (on unix) : export GUARDIAN_OPEN_API_KEY='xxxxx'
MY_API_KEY = os.getenv('GUARDIAN_OPEN_API_KEY')

# Where to get the data from...
API_ENDPOINT = 'http://content.guardianapis.com/search'

# TIME PERIOD TO DOWNLOAD: Update these dates to suit your own needs
START_DATE = date(2018, 1, 1)
END_DATE = date(2019, 10, 30)

# -----------------------------------
# Main program
# -----------------------------------
def main() :
    # Make sure the data download dir exist 
    makedirs(ARTICLES_DIR, exist_ok=True)

    # download_date ("2019-10-12", "testfil.json") - test document for processing..
    download_date_range( START_DATE, END_DATE, ARTICLES_DIR)

# ---------------------------------------
# Iterate over each day and download the data
# -------------------------------------------

def download_date_range ( start_date, end_date, articles_dir ) :
    # REFERENCE: day iteration from here:
    # http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates

    dayrange = range((end_date - start_date).days + 1)
    for daycount in dayrange:
        current_date = start_date + timedelta(days=daycount)
        current_datestr = current_date.strftime('%Y-%m-%d')
        print("\n---------- Processing: ", current_datestr)

        fname = join(articles_dir, current_datestr + '.json')
        if exists(fname):
            print("already downloaded, skipping....")
        else: 
            # then let's download it
            print("Downloading", current_datestr)
            download_date (current_datestr, fname)

#----------------------------------------
# Download the data for a specific date and write it to a JSON file
#
# Sample URL :
# 
# http://content.guardianapis.com/search?from-date=2016-01-02&
# to-date=2016-01-02&order-by=newest&show-fields=all&page-size=200
# &api-key=your-api-key-goes-here
# -----------------
def download_date( datestr, filename) :

    my_params = {
    'from-date': "", # leave empty, change start_date / end_date variables instead
    'to-date': "",
    'order-by': "newest",
    'show-fields': 'all',
    'page-size': 200,
    'api-key': MY_API_KEY
}

    all_results = []
    my_params['from-date'] = datestr
    my_params['to-date'] = datestr
    current_page = 1
    total_pages = 1
    
    while current_page <= total_pages:
        print("...page", current_page)
        my_params['page'] = current_page
        resp = requests.get(API_ENDPOINT, my_params)
        data = resp.json()
        all_results.extend(data['response']['results'])
        # if there is more than one page
        total_pages = data['response']['pages']
        current_page += 1
        
        
    with open(filename, 'w') as f:
        print("Writing to", filename)

        # re-serialize it for pretty indentation
        f.write(json.dumps(all_results, indent=2))
            



# ---------------------------
# Now all functions have been defined. Run the main program.
main() # This should be the last line of the file !