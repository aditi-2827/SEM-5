# ==================== NLTK ====================

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('all')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

text = "The natural language processing is interesting."

# Tokenization
tokens = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered = [word for word in tokens if word.lower() not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered]

# POS Tagging
pos = nltk.pos_tag(filtered)

print("NLTK Tokens:", tokens)
print("NLTK Without Stop Words:", filtered)
print("NLTK Stemmed:", stemmed)
print("NLTK Lemmatized:", lemmatized)
print("NLTK POS:", pos)


# ==================== spaCy ====================

import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

text = "Apple is opening a new office in Mumbai."
doc = nlp(text)

# POS Tagging
print("\nspaCy POS:")
for word in doc:
    print(word.text, word.pos_)

# Named Entity Recognition
print("\nspaCy Entities:")
for entity in doc.ents:
    print(entity.text, entity.label_)


# ==================== TextBlob ====================

from textblob import TextBlob

# Perform sentiment analysis
text = "I love Python. It is very easy to learn."

blob = TextBlob(text)

print("\nTextBlob Sentiment:")
print(blob.sentiment)


# ==================== Stanza ====================

import stanza

# Load English NLP pipeline
stanza.download('en')
nlp = stanza.Pipeline('en')

text = "Apple is opening a new office in Mumbai."
doc = nlp(text)

# POS Tagging
print("\nStanza POS:")
for sentence in doc.sentences:
    for word in sentence.words:
        print(word.text, word.upos)


# ==================== Scikit-learn ====================

from sklearn.feature_extraction.text import CountVectorizer

# Convert text into Bag of Words
documents = [
    "I love machine learning",
    "Machine learning is interesting",
    "I love Python"
]

vectorizer = CountVectorizer()
result = vectorizer.fit_transform(documents)

print("\nScikit-learn Vocabulary:")
print(vectorizer.get_feature_names_out())

print("Bag of Words:")
print(result.toarray())








# What is nlp?
# NLP (Natural Language Processing) is a branch of AI that allows computers to understand,process and analyze human language.
# A) NLTK
# What is NLTK?
# NLTK (Natural Language Toolkit) is a Python library used for processing and analyzing human language.
# In your practical, NLTK performs:
# 1.	Tokenization 
# 2.	Stop-word removal 
# 3.	Stemming 
# 4.	Lemmatization 
# 5.	POS tagging 
# Algorithm / Steps
# 1.	Take the input text. 
# 2.	Tokenize the text into individual words. 
# 3.	Remove common stop words such as the, is, a, etc. 
# 4.	Apply stemming to reduce words to their root form. 
# 5.	Apply lemmatization to obtain the meaningful base form of words. 
# 6.	Perform POS tagging to identify the grammatical category of each word.
# B) spaCy
# What is spaCy?
# spaCy is an NLP library designed for fast and efficient processing of text.
# In your practical, it performs:
# •	POS Tagging 
# •	Named Entity Recognition (NER) 
# Algorithm / Steps
# 1.	Load the English language model. 
# 2.	Give the text to spaCy. 
# 3.	spaCy processes the text and creates tokens. 
# 4.	Identify the Part of Speech of each word. 
# 5.	Identify Named Entities such as people, organizations and locations.
# C) TextBlob
# What is TextBlob?
# TextBlob is a simple Python library for processing text and performing basic NLP tasks.
# we use it for Sentiment Analysis.
# What is Sentiment Analysis?
# It determines the feeling or opinion expressed in text.

# D) Stanza
# What is Stanza?
# Stanza is a Python NLP library developed by the Stanford NLP group for processing human language.
# In your practical, we use it for POS tagging.
# Algorithm / Steps
# 1.	Download/load the required language model. 
# 2.	Create the Stanza NLP pipeline. 
# 3.	Give the text to the pipeline. 
# 4.	Stanza divides the text into sentences and words. 
# 5.	Assign a POS tag to each word.
