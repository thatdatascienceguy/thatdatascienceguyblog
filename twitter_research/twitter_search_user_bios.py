# -*- coding: utf-8 -*-
# Author: Jonathan Hernandez
# Email: jayhernandez1987@gmail.com

import tweepy
import re
import csv

ckey ='1zJKyLMse97rB3znLpIgw'
csecret ='kymPetfK0DCu0aPuJCvQRNcRy11pNs6zCNqchWg'
atoken = '2373146288-sZzajcYGlBGqLZXoweew6SRcWOQVw09BJhyU9Wf'
asecret = 'Totxk6ik1WneRW2ySOZuALahB713eTAjJdukDpQgM5xGq'

#Authencation
auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

''' Checks to see if the list of words match a twitter users bios
or description 
input: twitter_names_to_search: list of words to search in bios
        twitter_user_bios: the twitter users description to be searched on
output: True if all the names in twitter_names_to_search match a user's bios
        False otherwise
'''
def __is_match(twitter_names_to_search,twitter_user_bios):
    for i in range(0,len(twitter_names_to_search)): # search through all list of names
        my_regex= r"\b" + re.escape(twitter_names_to_search[i]) + r"\b" # search words that don't include spaces or other characters next to them        
        if re.search(my_regex,twitter_user_bios,re.IGNORECASE): # if match continue searching
            continue
        else: # no match simply exit
            return False
    return True

    
def twitter_search_bios_result_csv(twitter_search_words,csv_file_to_save): 
    f=open(csv_file_to_save,'ar+b')
    writer = csv.writer(f)
    for user in tweepy.Cursor(api.search_users,q=" ".join(twitter_search_words)).items(1000):
    #find if users acutally have the words in their bios
        x = user.__getstate__()
        twitter_vars=[x['created_at'],x['description'],x['favourites_count'],x['followers_count'],
                             x['friends_count'],x['geo_enabled'],x['id'],x['id_str'],
                             x['lang'],x['listed_count'],x['location'],x['name'],x['screen_name'],x['statuses_count'],
                             x['time_zone'],x['verified']]
        if __is_match(twitter_search_words,twitter_vars[1]):
            writer.writerow(twitter_vars)
    f.close() 

twitter_search_bios_result_csv(['locavore'],'/home/johnboy/Desktop/sample.csv')
