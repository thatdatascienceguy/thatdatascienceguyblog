# -*- coding: utf-8 -*-
"""
@author: Jonathan Hernandez
@email: thatdatasciguy@gmail.com
@github: https://github.com/thatdatascienceguy

"""
import pandas as pd
import numpy as np
from pandasql import sqldf

"""Data Cleaning movie list

1. Extract movies that are only classified as either short, movie or tv Movie.
2. Remove adult films
3. Replace '\\N' with 'NA' as that is considered missing.
4. Extract movies that started from 2000 to 2021
5. Remove isAdult and 'endYear' columns as those are irrelevant. """

# read in data downloaded from https://datasets.imdbws.com/
imdb_movies = pd.read_csv("title.basics.tsv", sep = '\t', low_memory=False)

imdb_titles = imdb_movies[(imdb_movies['titleType'] == 'movie') | \
						  (imdb_movies['titleType'] == 'tvMovie') | \
						  (imdb_movies['titleType'] == 'short')]
	

imdb_titles = imdb_titles[(imdb_titles['startYear'] >= '2000') & \
						  (imdb_titles['startYear'] <= '2021')]

imdb_titles = imdb_titles[imdb_titles['isAdult'] == '0']

imdb_titles = imdb_titles.replace(to_replace = '\\N', value = 'NA')

imdb_titles = imdb_titles.drop(['isAdult', 'endYear'], axis = 1)

"""read the ratings table and join (left) on the movie list"""

title_ratings = pd.read_csv("title.ratings.tsv", sep = '\t', low_memory=False)

pysqldf = lambda q: sqldf(q, globals()) # using SQL in python

# query to join the title table with the ratings table which has
# average IMDB rating and number of votes on the movie

q = """SELECT t.*, r.averageRating, r.numVotes
FROM imdb_titles t
LEFT JOIN title_ratings r
ON t.tconst = r.tconst
"""

movie_and_ratings = pysqldf(q)

# Replace NaN with 0 for averageRating and numVotes
movie_and_ratings = movie_and_ratings.replace(np.nan, 0)
movie_and_ratings.to_csv("IMDB_movies_2020-2021.csv", index=False)