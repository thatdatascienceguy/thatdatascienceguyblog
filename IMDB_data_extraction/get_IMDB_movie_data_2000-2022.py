# -*- coding: utf-8 -*-
"""
@author: Jonathan Hernandez
@email: thatdatasciguy@gmail.com
@github: https://github.com/thatdatascienceguy

"""
from imdb import IMDb
import pandas as pd
from functools import reduce # for flattening the data

movie_file = pd.read_csv("IMDB_movies_2020-2022.csv", dtype = str)

movie_id = movie_file['movie_ID']
movie_rating = []
imdb_rating = []
movie_metascore = []
movie_directors = []

# imdb object
ia = IMDb()

""" Variables to Extract
Title: Title of Movie
IMDB_Rating: IMDB Rating on the movie
Movie Rating: movie rating
"""
count = 1
# for each url, parse the html data and extract movie features
for ID in movie_id:
	
	print(count, ID)
	
	if (ia.get_movie(ID)) == None:
		continue
	else:
		movie = ia.get_movie(ID)# get movie information
	
	try:
			
		movie_rating.append(movie['certificate']) # movie rating in various countries
	
		imdb_rating.append(movie['rating']) # IMDB rating
		
		directors = []
		for director in movie['director']:
			movie_directors.append(directors.append(director))
	except KeyError:
		pass
	
	count +=1

movie_data = pd.DataFrame({"movie_rating": movie_rating,
						  "IMDB_rating": imdb_rating,
						  "Directors": movie_directors})