#!/usr/bin/env python3
import json
import os
 
import pandas as pd
import numpy as np
import string
import re
from collections import Counter
from nltk.corpus import stopwords

# %td-idf vectorizing 
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords as sw
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

# -------------
# CONSTANT DEFINITIONS
# -------------------

EXCLUDE_SECTION_IDS = {'culture', 'about', 'housing-network', 'fashion', 'travel', 'technology', 'australia-news', 'film', 
'education', 'clinique-beyond-beauty', 'provoking-progress', 'commentisfree', 'books', 'theobserver',
'breakthrough-science', 'kids-travel-guides', 'crosswords', 'football', 'born-adventurous', 'sport', 'raising-cats-and-dogs', 
'fill-your-heart-with-ireland', 'membership', 'tv-and-radio', 'stage', 'science', 'the-a-to-z-of-sleep',
'britain-get-talking', 'music', 'food', 'spains-secret-coast', 
'cities', 'lifeandstyle', 'artanddesign', 'games', 'guardian-masterclasses'}

DATADIR = str( os.getenv('OPENDATASCIENCE_DATADIR') )
    # TIDLIGERE version kaldte jeg det -  directory_name = "../theguardian/collection/"

#-------------------------------------------------
# Getting access to  my downloaded Guardian text corpus - incl full text 
#   - collection_subdirs : Directory containting all datasets to be read
#   -  exclude_sectionIds : 
# returns list of articles as strings from my dataset 
#-------------------------------------------------
def get_all_articles_texts( collection_subdir, exclude_sectionIds) :
    # Update to the directory that contains the json files ( articles from my fetched dataset)
    # Note the trailing /

    #include_sections = {'world', 'cities', 'money', 'media', 'community', 'global-development', 
    # 'society', 'info', 'business', 'science', 'environment', 'technology', 'politics', 
    # 'global', 'news', 'law', 'uk-news', 'us-news'}
    
    directory_name = DATADIR + "/" + collection_subdir  # "$OPENDATASCIENCE_DATADIR/theguardian/collection/"
    print(directory_name)

    unique_sectionIds       = set()
    unique_articletypes     = set()
    excluded_articles_count = 0
    texts = list()
    for filename in os.listdir(directory_name):
        if filename.endswith(".json"):
            with open(directory_name + filename) as json_file:
                data = json.load(json_file)
                for article in data:
                    sectionId = article['sectionId']
                    if sectionId not in exclude_sectionIds:
                        # 
                        unique_sectionIds.add(sectionId)
                        articletype = article['type']
                        unique_articletypes.add(articletype)
                        fields = article['fields']
                        text   = fields['bodyText'] if fields['bodyText'] else ""
                        # ids.append(id)
                        texts.append(text)
                    else:
                        excluded_articles_count += 1

    # print("Number of ids: %d" % len(ids))
    print("Number of included documents : %8d" % len(texts))
    print("Number of excluded documents : %8d" % excluded_articles_count )

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
    # --------------------------------------------------
   
    print("Total sum of all characters in articles: %i" % sum(all_lengths))
    print("MEAN size of articles: %d characters" % np.mean(all_lengths))
    

    return texts

#-------------------------------------------------
# Count words in a list of strings
# INPUT:
#   list_of_data : Array of strings containing long texts
# OUTPUT:
#   Total number of words in all the data.
#-------------------------------------------------
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
# Calculate average length of a list of text strings
# INPUT:
#   list_of_data : Array of strings containing long texts 
# OUTPUT:
#   Average length in characters (int)
#-------------------------------------------------
def average_length( list_of_data ):
    total = 0
    for text in list_of_data:
        total = total + len(text)

    number_of_data_elements = len(list_of_data)

    average_article_length = total / number_of_data_elements

    return average_article_length


#-------------------------------------------------
# Get top 10 words from a list of full-texts 
# INPUT:
#     list_of_data: Array of strings containing the text to be counted
# OUTPUT:
#     list of strings, containing top 10 words 
# PROCESS:
#     removes english stopwords - apply token_pattern (includes only word containing 2 characters/letters or more, a-zA-Z or - )
# 
# Codesnippets are inspired by class exercises (textmining101) + https://liferay.de.dariah.eu/tatom/preprocessing.html#index-0 
#-------------------------------------------------
def topwords( list_of_data ):

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
    # Give the indexes of the top-10most used words.
    counts = data_vect.sum(axis=0).A1
    top_idxs = (-counts).argsort()[:10]
    
    # Give the words belonging to the top-10 indexes.
    # Tip: Use an inverted vocabulary (see slides) to get the words that match your indexes.
    inverted_vocabulary = dict([(idx, word) for word, idx in model_vect.vocabulary_.items()])
    top_words = [inverted_vocabulary[idx] for idx in top_idxs]
    print("Top words: %s" % top_words)

    # Show the document vectors for 10 random documents. 
    # Limit the vector to only the top-10 most used words.
    # Note: To slice a sparse matrix use A[list1, :][:, list2] 
    # (see https://stackoverflow.com/questions/7609108/slicing-sparse-scipy-matrix)

    import random
    some_row_idxs = random.sample(range(0, len(list_of_data)), 10)
    print("Selection: " % (some_row_idxs))
    sub_matrix = data_vect[some_row_idxs, :][:, top_idxs].todense()
    print(sub_matrix)

    df = pd.DataFrame(columns=top_words, index=some_row_idxs, data=sub_matrix)
    print("print the DataFrame - incl the random sample from the index")
    print(df)

    return top_words

# -------------------
# Search for a list of query terms in a list of full texts
#
#  Use Term Frequency indexing to return most relevant articles
#
# INPUT:
#   query : String with Space seperated query terms
# OUTPUT:
#     list of strings, containing the full texts that macht the query 
# -------------
def search_for( query, list_of_data ) :
    list_of_result_data = ()

    model_vect = CountVectorizer(max_features=10000, stop_words=sw.words('english'), token_pattern=r'[a-zA-Z\-][a-zA-Z\-]{2,}')
    data_vect = model_vect.fit_transform(list_of_data)

    # Apply TF-IDF weighting
    model_tfidf = TfidfTransformer()
    data_tfidf = model_tfidf.fit_transform(data_vect)

    query_vect_counts = model_vect.transform([query])
    query_vect = model_tfidf.transform(query_vect_counts)
    print("Query vector : ", query_vect)

    # Calculate the similarity between your query vector and each document.
    # Tip: Use scikit's cosine_similarity to compare your query vector with your document-term tfidf matrix.
    sims = cosine_similarity(query_vect, data_tfidf)
    print("Cosine similarity : ", sims)

    sims_sorted_idx = (-sims).argsort()
    sims_sorted_idx # Article indexes sorted by similarity to my query

    top_article_text = list_of_data[sims_sorted_idx[0,0]]
    print("Top article matching my query : ", top_article_text)

    # Tabulate top-10 document indexes and similarities using pandas DataFrame
    # Tip: cosine_similarity returns a nested (1 query x 18846 documents) array ("sims"). 
    # Evaluate len(sims) and len(sims[0,:])) first.
    print("Shape of 2-D array sims: (%i, %i)" % (len(sims), len(sims[0,:])) )
    df = pd.DataFrame(data=zip(sims_sorted_idx[0,:], sims[0,sims_sorted_idx[0,:]]), columns=["index", "cosine_similarity"])
    print("Dataframe with top 10 document indexes : ", df[0:10])

    #TODO: generate list of result data from fond article indexes. look up in list_of_data 
    return list_of_result_data

#---------------------------------------------------------------
# MAIN PROGRAM ...
#---------------------------------------------------------------

# Update to the directory that contains your json files
# Note the trailing /

do_not_exclude_anything= set()

# 1. Get the data set ............
list_of_articlefulltexts = get_all_articles_texts("theguardian/collection_test/", EXCLUDE_SECTION_IDS)
#list_of_articlefulltexts = get_all_articles_texts("theguardian/collection/", do_not_exclude_anything )
#list_of_articlefulltexts = get_all_articles_texts("theguardian/collection_full/", EXCLUDE_SECTION_IDS)


# 2. analyse and visualize full data set .....................

article_top_words = topwords( list_of_articlefulltexts )
word_count =  word_count( list_of_articlefulltexts)
unique_word_count = unique_words( list_of_articlefulltexts)
average_article_length = average_length( list_of_articlefulltexts  )

print("word_count: ........... %9i" % word_count)
print("Unique word count: .... %9i" % unique_word_count)
print("Average article length: %9i" % average_article_length)

# 3. Search for ... Greta Turnberg .....................

found_articles = search_for( "Bill Clinton", list_of_articlefulltexts) 

# TODO: found_articles_topics = find_topics( found_articles )
# TODO: show_topics( found_articles_topics )

# --------------


#print ( article_top_words) 

