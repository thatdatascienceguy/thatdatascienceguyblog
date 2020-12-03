#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:24:41 2020

@author: jonboy1987
"""

# Take the video game platform csv file and convert it to a .db file

import sqlite3
import pandas as pd

# create a new file for the DB
connection = sqlite3.connect("Video_Games_DB.db")

# create the table 'games' with all the data
connection.execute('''CREATE TABLE games
				     (Name text,
			        ReleaseDate date,
			        ReleaseYear text,
					 Developer text,
					  Platform text,
					    Genres text,
						 Publisher text,
						  MaxPlayers text,
						   ESRB text,
						    Overview text,
							 Cooperative text);''')

connection.commit()

# load the csv fiie and put it into sql.
game_data = pd.read_csv("games.csv")
game_data.to_sql('games', connection, if_exists='replace', index=False)