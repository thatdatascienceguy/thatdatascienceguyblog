# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:15:26 2019

@author: jonboy1987
"""

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import pycountry
#import chart_studio
#import chart_studio.plotly as py
#import chart_studio.tools as tls

# load dataset
# powerlifting 2-25-2020
powerlifting = pd.read_csv("/home/jonboy1987/Desktop/powerlifting/openpowerlifting.csv",
						   low_memory=False)

# print out some statistics

print("Dimensions:", powerlifting.shape)
print("Missing data: ")
print(powerlifting.isnull().sum())

# describe the dataset
print(powerlifting.dtypes)
gender_plot = sb.countplot(x="Sex", data=powerlifting)
gender_plot.set_title("Gender")

# Plot each of the 1st, 2nd, and, 3rd attempts for benchpress, deadlift and squats
# for each gender

not_mixed_gender = powerlifting[powerlifting["Sex"] != "Mx"]

g1 = sb.FacetGrid(not_mixed_gender, col="Sex")
g1.map(plt.hist, "Bench1Kg")

g2 = sb.FacetGrid(not_mixed_gender, col="Sex")
g2.map(plt.hist, "Bench2Kg")
# What meet location countries are people getting disqualified?
# The goal is to create a global geo plot of each of the countries where these
# competitions are held and see which countries have the most disqualifying countries
# First, convert each country to it's respective alpha_3 code. Then, 


# Let's check out the unique Meet Countries


powerlifting_countries = pd.unique(powerlifting["MeetCountry"]) # countries in the powerlifting dataset
country_list = [country.name for country in list(pycountry.countries)] # countries in the pycountry dataset

# get the difference between the countries in powerlifting meets and from pycountry
# see which ones are not there in the powerlifting dataset and do a manual replacement
set(powerlifting_countries).difference(set(country_list))

# some countries are not found in the pycountry.countries package and some countries
# are in the same alpha code

# manual mapping:
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("East Germany",
																  "Germany")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("West Germany",
																  "Germany")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("UK" ,"United Kingdom")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("N.Ireland" ,"United Kingdom")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("Scotland" ,"United Kingdom")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("Wales" ,"United Kingdom")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("Ivory Coast" ,"Côte d'Ivoire")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("Russia" ,"Russian Federation")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("USSR" ,"Russian Federation")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("South Korea" ,"Korea, Republic of")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("Tahiti" ,"French Polynesia")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("Taiwan" ,"Taiwan, Province of China")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("UAE" ,"United Arab Emirates")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("US Virgin Islands" ,"Virgin Islands, U.S.")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("Venezuela" ,"Venezuela, Bolivarian Republic of")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("Yugoslavia" ,"Serbia")
powerlifting["MeetCountry"] = powerlifting["MeetCountry"].replace("Moldova" ,"Moldova, Republic of")

# removed mixed genders as there are not many
#not_mixed_gender = powerlifting[powerlifting["Sex"] != "Mx"]

# Group each meet country and count how many people were disqualified in each of them
disqualified_lifters = powerlifting[(powerlifting["Place"] == "DQ") |
												  (powerlifting["Place"] == "DD")]

print(disqualified_lifters)

num_disqualifers_per_country = disqualified_lifters.groupby("MeetCountry").size().reset_index(
	name="lifters_disqualified")

# compute the alpha code of each country to the num_disqualifers_per_country dataset
ISO_code = [pycountry.countries.search_fuzzy(country)[0].alpha_3
			for country in num_disqualifers_per_country["MeetCountry"]]

# append it to the num_disqualifers_per_country dataset
num_disqualifers_per_country["ISO_Code"] = ISO_code