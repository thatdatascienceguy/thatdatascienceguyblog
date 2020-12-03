#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:23:05 2020

@author: jonboy1987
"""
from datetime import datetime
import xml.etree.ElementTree as ET
import pandas as pd
import re

# read in the data
videogames_xml = ET.parse('Metadata.xml')
root_xml = videogames_xml.getroot()

# Video Game attributes to extract
videogame_attrs = ["Name", "ReleaseDate", "ReleaseYear", "Developer", "Platform",
	 "Genres", "Publisher", "MaxPlayers", "ESRB", "Overview", "Cooperative"]

# store list to keep video game data
rows = []

# loop through each game tag and for each game, get the data per
# videogame_attrs and store in a dictionary and then at the end,
# store in the rows list.
for game in root_xml.findall('Game'):
	data = [] # store game data
	# loop through each attribute
	for field in videogame_attrs:
		if game is not None and game.find(field) is not None:
			data.append(game.find(field).text) # append the data
		else:
			data.append(None) # data not found, just set to None
	rows.append({videogame_attrs[i]: data[i] # put the game data in the list
			  for i in range(0, len(videogame_attrs))})

# Take all the games and their data and put in a dataset/dataframe
games = pd.DataFrame(rows, columns = videogame_attrs)

# There are time/timezones in the 'ReleaseDate' column starting with 'T'
# remove them and just keep the data
dates = [re.sub("T.*", "", date)
		 if date is not None else None
		 for date in games["ReleaseDate"]]
games["ReleaseDate"] = dates

# format the Date as well for sorting purposes
dates = [datetime.strptime(date, "%Y-%m-%d") 
		 if date is not None else None
		 for date in dates]

# save dataframe in a csv file
games.to_csv("games.csv", index=False)

# Querying the data; Answering some questions

# All Megaman games
megaman_games = games[games["Name"].str.contains("Megaman|Mega Man", case=False)]
print(megaman_games[["Name", "ReleaseDate", "ESRB", "Publisher", "Platform"]].sort_values("ReleaseDate"))

# Every Konami game sorted by ReleaseDate and show ESRB ratings
konami_games = games[games["Developer"].str.contains("Konami", case=False, na=False)]
print(konami_games[["Name", "ReleaseDate", "ReleaseYear", "ESRB"]].sort_values("ReleaseDate"))