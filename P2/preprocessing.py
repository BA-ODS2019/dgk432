#!/usr/bin/env python3
import json
import os

# %matplotlib inline
import pandas as pd
import numpy as np
import string
import re
from collections import Counter
from nltk.corpus import stopwords

#-------------------------------------------------
# 
#-------------------------------------------------
def get_all_articles_texts():
    # Update to the directory that contains your json files
    # Note the trailing /

    DATADIR = str( os.getenv('OPENDATASCIENCE_DATADIR') )
    type(DATADIR)
    # TIDLIGERE ... directory_name = "../theguardian/collection/"

    directory_name = DATADIR + "/theguardian/collection/"
    print(directory_name)


    ids = list()
    texts = list()
    for filename in os.listdir(directory_name):
        if filename.endswith(".json"):
            with open(directory_name + filename) as json_file:
                data = json.load(json_file)
                for article in data:
                    id = article['id']
                    fields = article['fields']
                    text = fields['bodyText'] if fields['bodyText'] else ""
                    ids.append(id)
                    texts.append(text)

    print("Number of ids: %d" % len(ids))
    print("Number of texts: %d" % len(texts))

    return texts

#-------------------------------------------------
# Get top 10 words from a list of full-texts
#-------------------------------------------------
def topwords( list_of_data ):
    from sklearn.feature_extraction.text import CountVectorizer
    from nltk.corpus import stopwords as sw
    model_vect = CountVectorizer(max_features=10000, stop_words=sw.words('english'), token_pattern=r'[a-zA-Z\-][a-zA-Z\-]{2,}')
    # train and apply the model
    data_vect = model_vect.fit_transform( list_of_data )
    print('Shape: (%i, %i)' % data_vect.shape)

    # 3.c. The resulting matrix is a sparse matrix. What is the sparsity of this matrix?
    dense_count = np.prod(data_vect.shape)
    zeros_count = dense_count - data_vect.size
    sparsity = zeros_count / dense_count

    print("dense count ..........: %d" % dense_count )
    print("zeros_count ..........: %d" % zeros_count )
    print("sparsity of the matrix: %d" % sparsity )
    

    # 4. Show part of the document-term count matrix
    # 4.a. Give the indexes of the top-10 most used words.
    counts = data_vect.sum(axis=0).A1
    top_idxs = (-counts).argsort()[:10]
    
    # 4.b. Give the words belonging to the top-10 indexes.
    # Tip: Use an inverted vocabulary (see slides) to get the words that match your indexes.
    inverted_vocabulary = dict([(idx, word) for word, idx in model_vect.vocabulary_.items()])
    top_words = [inverted_vocabulary[idx] for idx in top_idxs]
    print("Top words: %s" % top_words)
    # Notice the strange non-word term 'ax'

    return top_words


#for article in texts:
#   print(article)


#import nltk
#import regex 

#import textcleaner as tc
#tc.main_cleaner('theguardian/collection')


# or
# tc.document('<FILE_NAME>')

#---------------------------------------------------------------
# MAIN PROGRAM ...

list_of_articlefulltexts = get_all_articles_texts()
article_top_words = topwords( list_of_articlefulltexts )
print ( article_top_words) 

