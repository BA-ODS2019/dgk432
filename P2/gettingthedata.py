#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:36:57 2019

@author: je
"""

import os
import json
import requests
from os import makedirs
from os.path import join, exists
from datetime import date, timedelta

DATADIR = str( os.getenv('OPENDATASCIENCE_DATADIR') )

# This creates two subdirectories called "theguardian" and "collection"
ARTICLES_DIR = join( DATADIR,'theguardian', 'collection')
makedirs(ARTICLES_DIR, exist_ok=True)

# Sample URL
#
# http://content.guardianapis.com/search?from-date=2016-01-02&
# to-date=2016-01-02&order-by=newest&show-fields=all&page-size=200
# &api-key=your-api-key-goes-here

# API Key is defined in your environement. 
# Define using (on unix) : export GUARDIAN_OPEN_API_KEY='xxxxx'
MY_API_KEY = os.getenv('GUARDIAN_OPEN_API_KEY')

API_ENDPOINT = 'http://content.guardianapis.com/search'
my_params = {
    'from-date': "", # leave empty, change start_date / end_date variables instead
    'to-date': "",
    'order-by': "newest",
    'show-fields': 'all',
    'page-size': 200,
    'api-key': MY_API_KEY
}

# day iteration from here:
# http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates

# Update these dates to suit your own needs.
start_date = date(2018, 1, 1)
end_date = date(2019, 10, 30)

dayrange = range((end_date - start_date).days + 1)
for daycount in dayrange:
    dt = start_date + timedelta(days=daycount)
    datestr = dt.strftime('%Y-%m-%d')
    fname = join(ARTICLES_DIR, datestr + '.json')
    if not exists(fname):
        # then let's download it
        print("Downloading", datestr)
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
            current_page += 1
            total_pages = data['response']['pages']

        with open(fname, 'w') as f:
            print("Writing to", fname)

            # re-serialize it for pretty indentation
            f.write(json.dumps(all_results, indent=2))
            
            
