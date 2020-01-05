## Portfolio 2 documentation 

* By Jeannette Ekstrøm, 
* jeek [ at ] dtu.dk 
* student ID : dgk432 


-------------------- 

In order to solve the assignment I had to struggle a bit with code. 

I had 3 steps I wanted to solve:

1. Getting the data 
2. Pre-process the data and answer the questions
   2.   incl. built vector models, topic models and queries
3. Visualize by use of WordCloud

I decided to split up the process, and having one script for *Getting the data* 
https://github.com/BA-ODS2019/dgk432/blob/master/P2/gettingthedata.py 

and a second script *pre-processing the results and visualizations* 
https://github.com/BA-ODS2019/dgk432/blob/master/P2/preprocessing.py

I created 7 functions inspired by the lecture slides and supplementary links & literature we have
been through during the themes from Module 2 ( Basic Text Analysis, Vector Space Models, Text Classification and Topic Modelling).
I used Visual Code Studio and also Spyder as editors, not Jupyter Notebook as the teacher did.

That way I kept a better structure - and a better understand of which *variables* I was processing on, as  well as an understanding of how I got access to my data.

I used "literature and google" to learn about - how to add create functions (*def*) .
... programming is supposed to reduce workloads and create a nice overview, so instead of performing the same line of code on several different words for counting and analysis, creating a function (incl a few arguments I wanted to return better structured code.
Functions are defined and inspired using *def* function like this one below:
___________

def count_in_list(item_to_count, list_to_search): # define function and give it a name +                                                                    two arguments

    number_of_hits = 0                            # define our variable + assign value zero
    for item in list_to_search:                   # we loop over all words in our list
        if item == item_to_count:                 # if we find words equal to 
            number_of_hits += 1                   # we add 1 to our variable [list]              
    return number_of_hits                         # finally return the result 

print(count_in_list(' keyword of our choice ', words))

from source: 
(https://nbviewer.jupyter.org/github/fbkarsdorp/python-course/blob/master/Chapter%202%20-%20First%20steps.ipynb)

Because my data fetch was pretty large I had to create a few "sub-sets" - otherwise the process would take to long. The PATH I did not use was then just hash'ed out, which made it easier for me to process the statements - without much delay 
The final script is with the complete dataset.

## Pre-processing unstructured data like news articles ( text mining )
Preprocessing data/text is all about making better sense of the text, you are working with, and is a very common and useful task in text analysis.
It's about discovering patterns and examining context, uniqueness and outliers of large chuncks of text, that being newsgroup data, novels like <b>Jane Austens</b> *Emma* or like in our case, news articles and feature articles from a well known newspaper like The Guardian.

Tokenization is the process of splitting a text into individual words or perhaps sequences of words (n-grams).(Ignatow & Mihalcea, 2018, page 101-103).
Big decisions need to be thought through when using tokenization, one reason being language differences. Splitting words in the english language versus the danish language may see difficult in one iteration. But in most cases - I believe - the data that you want to use will be fetched from one source and therefore in one single language. At least in our Portfolio 2 case I grab news from The Guardian, all in english.
In order to look for word patterns and word frequencies you will experience lots of "similar words just spelled a bit different, being plural versions or inflected forms of a word". This special procedure is called *stemming*, and is used in many search engines behind the scenes, resulting in a better search experience. In this case, I have left out these options (stemming, lemmatization) in my assignment delivery. 

One of the first pre-processing was to split all the sentence into a list of words (represented by strings).
By issuing the function split Python splits the sentence on spaces and returns a list of words. And returns a list. It makes it possible to access all the individual components using indexes and we can use slice indexes to access parts of the list.
Using the split function is a *quick and dirty* way to get an overview of a corpus. And the function do unfortunately not take lower and uppercase into consideration. It simply splits sentences into *strings/words* by use of *spaces*, and then return a list of strings/words to work with further.
But all this is taken care of by using the Scikit learn library.
______

## Document term matrix - Vector - Topic modelling - Text analysis for text mining.. 

Treating texts as a list of word frequencies (a vector) also makes available a vast range of mathematical tools developed for studying and manipulating vectors. Something that really is not neccessary to "know in dept". (https://liferay.de.dariah.eu/tatom/working_with_text.html )
But the process turn the texts into unordered lists / socalled *Bag of Words* ( BOW ) - that you can start working on.

In text mining we often access collections of documents (open data or otherwise), like in this case with the Guardian news articles. when we "scrape the fulltext" of news articles by use of an API key, we have acquired. The data is OPEN, we need to credit where we got it from, and also accept what to use it for, but the result is, that we receive lots of unstructured data, that we can start to process in order to discover "head and tail" in the context for either study or research. 

In our course Python programmering was a large part of the learning objectives, and we had to learn quite a few special Python programming libraries. From Pandas DataFrames, to Numpy mathematics and to more specialised libraries that would assist us in the text classification process.

    "Latent Dirichlet allocation (LDA) is a particularly popular method for fitting a topic model. It treats each document as a mixture of topics, and each topic as a mixture of words. This allows documents to “overlap” each other in terms of content, rather than being separated into discrete groups, in a way that mirrors typical use of natural language." 
    (https://www.tidytextmining.com/topicmodeling.html)

LDA was really useful for getting hold of topics in my collection of "top 10 documents" - and it is definitely something I will explore further, after the class. We have "learned" it by example, by googling and by reading literature, next step is to get it to use in practice.

Another method was looking at similaries and frequencies, by use of Tf-idf (term frequency - inverse document frequency) that I before new from the major search-engines. Tf-idf is a way to add algorithms behind search results, in order to receive relevant results - with similar topics/themes. It has been intesting to understand some of what goes on behind the nice search interfaces. In this assigment I used it as thought in class, by looking into patterns and similarities in my search result/downloaded dataset. One think though is, that the algorithm is transparent and the results are reproducible in other contexts - open science rules .... 

    "Corpus exploration = meaning analysing a corpus of text 
    a pre-processing step for text-mining measures and models = cleaning, pattern recognition..

    Tf-idf is especially appropriate if you are looking for a way to get a bird’s eye view of your corpus early in the exploratory phase of your research because the algorithm is transparent and the results are reproducible - The math behind tf-idf is lucid enough to depict in a spreadsheet."
    (https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf#fn:1)

I have used # in my script, to explain how and what process I have done. 

## Inspiration and documentation:
* https://liferay.de.dariah.eu/tatom/preprocessing.html#index-0
* https://www.tidytextmining.com/topicmodeling.html
* https://learning.oreilly.com/library/view/mastering-machine-learning/9781788299879/73015649-db61-4956-a5dd-5116ca59e839.xhtml
* Ignatow & Mihalcea, 2018 
https://us.sagepub.com/en-us/nam/an-introduction-to-text-mining/book249451

