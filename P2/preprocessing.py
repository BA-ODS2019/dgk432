#!/usr/bin/env python3
import json
import os
 
import pandas as pd
import numpy as np
import string
import re
from collections import Counter
import random

# Python Libraries for visualising 
from wordcloud import WordCloud
import matplotlib.pyplot as plt 

# Python Libraries for Tf-idf vectorizing 
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords as sw
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import LatentDirichletAllocation

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
    # basic text analysis

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
# Codesnippets are inspired by class exercises + https://liferay.de.dariah.eu/tatom/preprocessing.html#index-0 
#-------------------------------------------------
def topwords( list_of_data ):

    model_vect = CountVectorizer(max_features=10000, stop_words=sw.words('english'), token_pattern=r'[a-zA-Z\-][a-zA-Z\-]{2,}')
 
    # train and apply the model
    data_vect = model_vect.fit_transform( list_of_data )
    print('Shape: (%i, %i)' % data_vect.shape)

    # The resulting matrix is a sparse matrix. 
    dense_count = np.prod(data_vect.shape)
    zeros_count = dense_count - data_vect.size
    sparsity = zeros_count / dense_count

    print("dense count ..........: %d" % dense_count )
    print("zeros_count ..........: %d" % zeros_count )
    print("sparsity of the matrix: %f" % sparsity )
    

    # Show part of the document-term count matrix
    # Give the indexes of the top-10 most used words.
    counts = data_vect.sum(axis=0).A1
    top_idxs = (-counts).argsort()[:10]
    
    # Give the words belonging to the top-10 indexes.
    # Tip: Use an inverted vocabulary to get the words that match your indexes.
    inverted_vocabulary = dict([(idx, word) for word, idx in model_vect.vocabulary_.items()])
    top_words = [inverted_vocabulary[idx] for idx in top_idxs]
    print("Top words: %s" % top_words)

    # Show the document vectors for 10 random documents. 
    # Limit the vector to only the top-10 most used words.
    # Note: To slice a sparse matrix use A[list1, :][:, list2] 
    # (see https://stackoverflow.com/questions/7609108/slicing-sparse-scipy-matrix)

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
# Use Term Frequency (tf-idf) indexing to return most relevant articles
# INPUT:
#   query : String with space separated query terms
# OUTPUT:
#     list of strings, containing the full texts that match the query 
# -------------
def search_for( query, list_of_data ) :
    list_of_result_data = []

    model_vect = CountVectorizer(max_features=10000, stop_words=sw.words('english'), token_pattern=r'[a-zA-Z\-][a-zA-Z\-]{2,}')
    data_vect = model_vect.fit_transform(list_of_data)

    # Apply TF-IDF weighting for this query model 
    model_tfidf = TfidfTransformer()
    data_tfidf = model_tfidf.fit_transform(data_vect)

    query_vect_counts = model_vect.transform([query])
    query_vect = model_tfidf.transform(query_vect_counts)
    print("Query vector : ", query_vect)

    # Calculate the similarity between the query vector and each document.
    # Tip: Use scikit's cosine_similarity to compare the query vector with the document-term tfidf matrix.
    sims = cosine_similarity(query_vect, data_tfidf)
    print("Cosine similarity : ", sims)

    sims_sorted_idx = (-sims).argsort()
    sims_sorted_idx # Article indexes sorted by similarity to the query

    top_article_text = list_of_data[sims_sorted_idx[0,0]]
    print("Top article matching my query : ", top_article_text)

    # Tabulate top-10 document indexes and similarities using pandas DataFrame
    # Tip: cosine_similarity returns a nested (query x documents) array ("sims"). 
    # Evaluate len(sims) and len(sims[0,:])) first.
    print("Shape of 2-D array sims: (%i, %i)" % (len(sims), len(sims[0,:])) )
    df = pd.DataFrame(data=zip(sims_sorted_idx[0,:], sims[0,sims_sorted_idx[0,:]]), columns=["index", "cosine_similarity"])
    print("Dataframe with top 10 document indexes : ", df[0:10])

    print("Getting top 10 articles ....")
    for idx in sims_sorted_idx[0,0:10] :
        article_text = list_of_data[idx]
        print( idx )
        #print( article_text )
        list_of_result_data.append( article_text  )

    return list_of_result_data


# -------------------
# Search for top 10 words in a list of article texts and create a WordCloud with ...
# Use model vector and LatentDirichletAllocation 
# INPUT:
#   query : String with space separated query terms
# OUTPUT:
#     list of strings, containing the full texts that match the query 
# -------------
def create_topics_wordcloud( list_of_data, title, filename ) :
    
    model_vect = CountVectorizer(max_features=10000, stop_words=sw.words('english'), token_pattern=r'[a-zA-Z\-][a-zA-Z\-]{2,}')
    data_vect = model_vect.fit_transform(list_of_data)

    print("Random names: ", random.sample(model_vect.get_feature_names(), 10) )

    # Perform topic modelling
    # using Latent Dirichlet Allocation (LDA) on your pre-processed data
    # Note: Set n_components=4 (nr. of topics) and random_state=0 (so we get...... #TODO:
    model_lda = LatentDirichletAllocation(n_components=4, random_state=0)
    data_lda = model_lda.fit_transform(data_vect)
    
    # Describe the shape of the resulting matrix.
    import numpy as np
    np.shape(data_lda)
    
    # Display the top-10 terms and their weights for each topic.
    # Are the topics recognisable?
    # Tip: Use the components_ attribute of your LDA model, which contains the topic-t
    # Use enumerate to loop over the components.
    for i, term_weights in enumerate(model_lda.components_):
        top_idxs = (-term_weights).argsort()[:10]
        top_words = ["%s (%.3f)" % (model_vect.get_feature_names()[idx], term_weights[idx]) for idx in top_idxs]
        print("Topic %d: %s" % (i, ", ".join(top_words)))
    # A big challenge of topic modelling is too make the topics interpretable and meaningfull

    # Display doc-topic matrix for 10 documents
    topic_names = ["Topic" + str(i) for i in range(model_lda.n_components)]
    doc_names = ["Doc" + str(i) for i in range(len(list_of_data))]
    df = pd.DataFrame(data=np.round(data_lda, 2), columns=topic_names, index=doc_names).head(10)
    # extra styling
    #df.style.applymap(lambda val: "background: yellow" if val>.3 else '', )
    print("dataframe: ", df)

    # Inspect a random document
    doc_idx = random.randint(0,len(list_of_data)-1)
    print('Doc idx: %d' % doc_idx)
    # What is the most likely topic according to LDA?
    topics = data_lda[doc_idx]
    print('Topic vector: %s' % topics)
    vote = np.argsort(-topics)[0]
    print('Topic vote: %i' % vote)
    # Look at the textual content of the document
    print('Document text: ', list_of_data[doc_idx])

    # Topic visualization by use of Wordcloud 
    # Word cloud
    # Display a word cloud for a topic. Display the top-10 words and use their term loadings as weight/frequency.
    # Tip: Install and use the wordcloud package.
    # Example usage: https://stackoverflow.com/questions/43145199/create-wordcloud-fro.....#TODO 

    plt.clf()
    
    for i, term_weights in enumerate(model_lda.components_):
        top_idxs = (-term_weights).argsort()[:10]
        top_words = [model_vect.get_feature_names()[idx] for idx in top_idxs]
        word_freqs = dict(zip(top_words, term_weights[top_idxs]))
        wc = WordCloud(background_color="white",width=300,height=300, max_words=10).generate_from_frequencies(word_freqs)
        plt.subplot(2, 2, i+1)
        plt.imshow(wc)
        plt.axis("off")
    
    plt.suptitle(title)
    plt.savefig(filename)

    return 
    
#---------------------------------------------------------------
# MAIN PROGRAM ...
#---------------------------------------------------------------

# Update to the directory that contains your json files
# Note the trailing /

do_not_exclude_anything= set()

# 1. Get the data set ............
# below are some of my test-data-sets for fetching data - since the data range is very large, I have 
# selected a few articles in a test collection for the text analysis / pre processing for increasing 
# speed 
#list_of_articlefulltexts = get_all_articles_texts("theguardian/collection_test/", EXCLUDE_SECTION_IDS)
#list_of_articlefulltexts = get_all_articles_texts("theguardian/collection/", do_not_exclude_anything )
list_of_articlefulltexts = get_all_articles_texts("theguardian/collection_full/", EXCLUDE_SECTION_IDS)


# 2. analyse and visualize full data set .....................

article_top_words = topwords( list_of_articlefulltexts )
word_count =  word_count( list_of_articlefulltexts)
unique_word_count = unique_words( list_of_articlefulltexts)
average_article_length = average_length( list_of_articlefulltexts  )

print("word_count: ........... %9i" % word_count)
print("Unique word count: .... %9i" % unique_word_count)
print("Average article length: %9i" % average_article_length)

# 3. Search for ... Query: with which topics was "Bill Clinton ... " discussed? ...................

bill_clinton_articles = search_for( "Bill Clinton", list_of_articlefulltexts) 
create_topics_wordcloud(bill_clinton_articles, "Bill Clinton in Wordclouds", "clinton_wordcloud.png")

trumps_articles = search_for( "Donald Trump", list_of_articlefulltexts) 
create_topics_wordcloud(trumps_articles, "Donald Trump in Wordclouds", "trump_wordcloud.png")

climate_articles = search_for( "Climate change", list_of_articlefulltexts) 
create_topics_wordcloud(climate_articles, "Climate Change Topics in Wordclouds", "climate_wordcloud.png")

thunbergs_articles = search_for( "Greta Thunberg", list_of_articlefulltexts) 
create_topics_wordcloud(thunbergs_articles, "Greta Thunberg in Wordclouds", "thunberg_wordcloud.png")


# --------------


