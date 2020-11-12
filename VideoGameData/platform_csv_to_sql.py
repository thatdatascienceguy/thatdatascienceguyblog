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
connection = sqlite3.connect("Video_Game_Platforms_DB.db")

# create the table 'platforms' with all the data
connection.execute('''CREATE TABLE platforms
				     (Name text,
			        Emulated text,
			        ReleaseDate date,
					 Developer text,
					  Manufacturer text,
					    CPU text,
						 Memory text,
						  Graphics text,
						   Sound text,
						    Display text,
							 Media text,
							 MaxControllers text,
							  Notes text,
							  Category text);''')

connection.commit()

# load the csv fiie and put it into sql.
platform_data = pd.read_csv("platforms.csv")
platform_data.to_sql('platforms', connection, if_exists='replace', index=False)