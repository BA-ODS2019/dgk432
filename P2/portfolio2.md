## Portfolio 2 documentation

inspiration and documentation:
* https://liferay.de.dariah.eu/tatom/preprocessing.html#index-0


Preprocessing data/text is all about making better sense of the text, you are working with, and is a very common and useful task in text analysis.
It's about discovering patterns and examining context, uniqueness and outliers of large chuncks of text, that being newsgroup data, novels like <b>Jane Austens<b/> *Emma* or like in our case, news articles and feature articles from a well known newspaper like The Guardian.

Tokenization is the process of splitting a text into individual words or perhaps sequences of words (n-grams). [ litt fra pensum bogen - s. xx ]
Big decisions need to be thought through when using tokenization, one reason being  language differences. Splitting words in the english language versus the danish language may see difficult in one iteration. But in most cases - I believe - the data that you want to use will be fetched from one source and therefore in one single language. At least in our Portfolio 2 case I grab news from The Guardian, all in english.

In this assignment we are asked to use the Python library scikit-learn, inkl the CountVectorizer. But it seems there are lot´s of other similar tools that can do the job
(https://liferay.de.dariah.eu/tatom/preprocessing.html#index-0)

In order to look for word patterns and word frequencies you will experience lots of "similar words just spelled a bit different, being plural versions or inflected forms of a word". This special procedure is called *stemming*, and is used in many search engines behind the scenes, resulting in a better search experience. 

... programming is supposed to reduce workloads,, and instead of performing the same line of code on several different words for counting and analysis, creating a function (incl a few arguments you have decided will return better and well structured programming. Functions are defined using the def keyword like this:

___________

def count_in_list(item_to_count, list_to_search): # define function and give it a name +                                                        two arguments
    number_of_hits = 0                            # define our variable + assign value zero
    for item in list_to_search:                   # we loop over all words in our list
        if item == item_to_count:                 # if we find words equal to 
            number_of_hits += 1                   # we add 1 to our variable [list]              
    return number_of_hits                         # finally return the result 

print(count_in_list(' keyword of our choice ', words))

from source: https://nbviewer.jupyter.org/github/fbkarsdorp/python-course/blob/master/Chapter%202%20-%20First%20steps.ipynb

________________

split: 
We can transform our sentence into a list of words (represented by strings) using the split() function as follows:

words = sentence.split()
print(words)

By issuing the function split on our sentence, Python splits the sentence on spaces and returns a list of words. In many ways a list functions like a string. We can access all of its components using indexes and we can use slice indexes to access parts of the list.
Using the split function is a *quick and dirty* way to get an overview of a corpus. And the function to not take lower and uppercase into consideration. It simply splits sentences into *strings/words* by use of *spaces*, and then return a list of strings/words to work with further.

Document term matrix:

Treating texts as a list of word frequencies (a vector) also makes available a vast range of mathematical tools developed for studying and manipulating vectors. 
kilde: https://liferay.de.dariah.eu/tatom/working_with_text.html 

meaning that you can turn all the texts from a document into unordered lists / .. Bag of Words ( BOW ) is simply just at bag of words -> documents as vectors

______

## topic modelling - machine learning - text analysis 

term frequency - inverse document frequency :
https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf#fn:1

used for: 
corpus exploration = meaning analysing a corpus of text 
a pre-processing step for text-mining measures and models = cleaning, pattern recognition..

Tf-idf is especially appropriate if you are looking for a way to get a bird’s eye view of your corpus early in the exploratory phase of your research because the algorithm is transparent and the results are reproducible - The math behind tf-idf is lucid enough to depict in a spreadsheet.

