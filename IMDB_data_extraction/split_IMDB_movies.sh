#!/bin/bash

FILENAME=IMDB_movies_2020-2021.csv
HEADER=$(head -n1 $FILENAME)

# split IMDB dataset into files having 50000 entries each prefixed by abc
split -d -l 50000 IMDB_movies_2020-2022.csv abc

N=1 # counter to see how many files processed in the for loop

for F in abc*
do
	if [ $N -gt 1 ]; then
		echo $HEADER > data_$N.csv # append the header first
	fi
	cat $F >> data_$N.csv
	rm -f $F # remove old file and keep new one with header
	((N++))
done

# Take the newly splitted files and upload them to AWS S3
aws s3 cp . s3://imdbdatajon/ --exclude "*" --include "data_*" --recursive
