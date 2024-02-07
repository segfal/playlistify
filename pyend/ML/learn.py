#credit: https://www.kaggle.com/code/groovitasconsulting/recommendation-engine-by-hammad-ahmed
import nltk # Import the NLTK library
import random # To shuffle the dataset
from nltk.corpus import movie_reviews # Import movie reviews corpus
from nltk.classify.scikitlearn import SklearnClassifier # Wrapper to include scikit-learn algorithms in NLTK
from sklearn.naive_bayes import BernoulliNB, MultinomialNB # Naive Bayes
from sklearn.linear_model import LogisticRegression, SGDClassifier # Stochastic Gradient Descent
import os
import pandas as pd
import numpy as np

#spotify_df = pd.read_csv('spotify.csv')



