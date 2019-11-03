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
# Getting access to  my downloaded Guardian text corpus - incl full text 
# returns list of articles as strings from my dataset 
#-------------------------------------------------
def get_all_articles_texts( collection_subdir) :
    # Update to the directory that contains your json files
    # Note the trailing /


    include_sections = {'world', 'cities', 'money', 'media', 'community', 'commentisfree', 
    'global-development', 'books', 'theobserver', 'society', 'info', 'business', 
    'science', 'environment', 'technology', 'politics', 'global', 'news', 
    'law', 'uk-news', 'us-news'}

    DATADIR = str( os.getenv('OPENDATASCIENCE_DATADIR') )
    # TIDLIGERE version kaldte jeg det -  directory_name = "../theguardian/collection/"

    directory_name = DATADIR + "/" + collection_subdir  # "theguardian/collection/"
    print(directory_name)

    unique_sectionIds = set()
    unique_articletypes = set()
    texts = list()
    for filename in os.listdir(directory_name):
        if filename.endswith(".json"):
            with open(directory_name + filename) as json_file:
                data = json.load(json_file)
                for article in data:
                    sectionId = article['sectionId']
                    if sectionId in include_sections:
                        unique_sectionIds.add(sectionId)
                        articletype = article['type']
                        unique_articletypes.add(articletype)
                        fields = article['fields']
                        text = fields['bodyText'] if fields['bodyText'] else ""
                        # ids.append(id)
                        texts.append(text)

    # print("Number of ids: %d" % len(ids))
    print("Number of documents: %d" % len(texts))
    print("Unique sectionIDs:" )
    print( unique_sectionIds )
    print("Unique article type:" )
    print ( unique_articletypes )

    all_lengths = list()
    for article in texts:
        all_lengths.append(len(article))

# --------------------------------------------------
# How long are the texts?
# Calculate total length in characters per class.
# Tip: Use zip() method and pandas's groupby feature
# --------------------------------------------------
    print("Total sum of all characters in articles: %i" % sum(all_lengths))
    print("MEAN size of articles: %d characters" % np.mean(all_lengths))

    return texts

# -----------------
# figuring out how to perform simple word counts in my data set from The Guardian 
# inspiration from our TDM classes incl 1, 2 and 3..
# -----------------
def word_count ( list_of_data):
    # word count (simple tokenization) 

    word_count = 0
    for text in list_of_data:
        words = text.split()
        word_count = word_count + len(words)

    return word_count

def unique_words ( list_of_data ): 
    # word count plus the unique word count
    unique_words = set()
    for text in list_of_data:
        words = text.split()
        unique_words.update(words)

        # reference taken from https://www.programiz.com/python-programming/set
        # unique_words = set(all_words)
    
    unique_word_count = len(unique_words)

    return unique_word_count



#-------------------------------------------------
# Get top 10 words from a list of full-texts 
# ren copy paste fra øvelserne i TDM 101 1+2 og 3 + URL... 
#-------------------------------------------------
def topwords( list_of_data ):
    from sklearn.feature_extraction.text import CountVectorizer
    from nltk.corpus import stopwords as sw
    model_vect = CountVectorizer(max_features=10000, stop_words=sw.words('english'), token_pattern=r'[a-zA-Z\-][a-zA-Z\-]{2,}')
    # train and apply the model
    data_vect = model_vect.fit_transform( list_of_data )
    print('Shape: (%i, %i)' % data_vect.shape)

    # The resulting matrix is a sparse matrix. What is the sparsity of this matrix?
    dense_count = np.prod(data_vect.shape)
    zeros_count = dense_count - data_vect.size
    sparsity = zeros_count / dense_count

    print("dense count ..........: %d" % dense_count )
    print("zeros_count ..........: %d" % zeros_count )
    print("sparsity of the matrix: %f" % sparsity )
    

    # Show part of the document-term count matrix
    # Give the indexes of the top-25 most used words.
    counts = data_vect.sum(axis=0).A1
    top_idxs = (-counts).argsort()[:25]
    
    # Give the words belonging to the top-10 indexes.
    # Tip: Use an inverted vocabulary (see slides) to get the words that match your indexes.
    inverted_vocabulary = dict([(idx, word) for word, idx in model_vect.vocabulary_.items()])
    top_words = [inverted_vocabulary[idx] for idx in top_idxs]
    print("Top words: %s" % top_words)

    #from sklearn.decomposition import LatentDirichletAllocation
    #model_lda = LatentDirichletAllocation(n_components=4, random_state=0)
    #data_lda = model_lda.fit_transform(data_vect)
    # Describe the shape of the resulting matrix
    #np.shape(data_lda)

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




list_of_articlefulltexts = get_all_articles_texts("theguardian/collection/")
#list_of_articlefulltexts = get_all_articles_texts("theguardian/collection_full/")

article_top_words = topwords( list_of_articlefulltexts )
word_count =  word_count( list_of_articlefulltexts)
unique_word_count = unique_words( list_of_articlefulltexts)

print("word_count: ........... %9i" % word_count)
print("Unique word count: .... %9i" % unique_word_count)

# --------------


#print ( article_top_words) 

