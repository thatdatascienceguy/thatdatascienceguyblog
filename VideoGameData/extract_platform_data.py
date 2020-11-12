# -*- coding: utf-8 -*-
"""
Extracting video platform data from the Platform.xml file provided
by LaunchBox.
"""

import xml.etree.ElementTree as ET
import pandas as pd
import re

# read in the data
platforms_xml = ET.parse('Platforms.xml')
root_xml = platforms_xml.getroot()

# Create Empty list to store attributes
platform_attrs = ["Name", "Emulated", "ReleaseDate", "Developer",
	 "Manufacturer", "Cpu", "Memory", "Graphics", "Sound",
	 "Display", "Media", "MaxControllers", "Notes", "Category"]

# list to store all the data to be converted to CSV
rows = []

for platform in root_xml:
	data = []
	# Check if any of them are null and if so, set the value to 'None'
	for field in platform_attrs:
		if platform is not None and platform.find(field) is not None:
			data.append(platform.find(field).text) # add the data
		else: # it is a empty value set to None
			data.append(None)
	# append the data/observation to the rows list
	rows.append({platform_attrs[i]: data[i]
			  for i in range(0,len(platform_attrs))})

# Crate a dataframe out of the extracted data from the xml file
platforms = pd.DataFrame(rows, columns = platform_attrs)

# looking at the CSV file, there is also data that came from the <PlatformAlternativeName>
# attribute. As such, there are sparse data after the Linux platform. 
# Let's get rid of it

# Get the index list of Linux platforms (should be 1)
linux_platform = platforms.index[platforms["Name"] == "Linux"]

# find the first index of occurence
linux_platform_index = linux_platform.tolist()[0]

platforms = platforms[0:linux_platform_index + 1]

# looking around the csv file, there are time/timezones in the date as well.
# let's remove the time and keep the date
dates = [re.sub("T.*", "", date)
		 if date is not None else None
		 for date in platforms["ReleaseDate"]]

platforms["ReleaseDate"] = dates

# write to a csv file
platforms.to_csv("platforms.csv",index=False)

# How many nintendo consoles have been made and when?
nintendo_console_query = platforms[platforms["Name"].str.contains("Nintendo", case=False)]
print(nintendo_console_query[["Name", "ReleaseDate"]].sort_values("ReleaseDate"))

# What are the specs of each Sony system?
playstation_console_query = platforms[platforms["Name"].str.contains("Sony", case=False)]
print(playstation_console_query[["Name","Graphics", "Memory", "Cpu", "Display"]])

# Which consoles were using floppy disks and when did they start fading out?
floppy_disks_query = platforms[platforms["Media"].str.contains("Floppy", case=False, na=False)]
print(floppy_disks_query[["Name", "ReleaseDate"]])