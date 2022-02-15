# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 21:31:49 2014

@author: johnboy
"""

import tweepy 
from itertools import combinations
import networkx as nx
import time

ckey ='1zJKyLMse97rB3znLpIgw'
csecret ='kymPetfK0DCu0aPuJCvQRNcRy11pNs6zCNqchWg'
atoken = '2373146288-sZzajcYGlBGqLZXoweew6SRcWOQVw09BJhyU9Wf'
asecret = 'Totxk6ik1WneRW2ySOZuALahB713eTAjJdukDpQgM5xGq'

#Authencation
auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

# read the gexf file corresponding to a specific timezone and examine friendships
# among that group

time_zone_graph = nx.read_gexf('/home/johnboy/Desktop/twitter_research/twitter_locavore_SNA_timezone_gexf_files/Ecuador_Time_Mod_May11_2014.gexf')
time_zone_graph = nx.DiGraph(time_zone_graph)
friendship_pairs = combinations(time_zone_graph,2)
time_zone_graph.remove_edges_from(time_zone_graph.edges())

ctr = 1
for a in friendship_pairs: # for every combinations of two users in the dataset    
    print ctr   
    try:
        friendship = api.show_friendship(source_screen_name=a[0],target_screen_name=a[1])
        if friendship[0].following: # is (user1 following user2)?
            print 'adding edge from', a[0], 'to', a[1]            
            time_zone_graph.add_edge(a[0],a[1]) # user1 ---> user2
        else:
            print a[0], 'is not following', a[1]
            
        if friendship[1].following: # is (user2 following user1)?
            print 'adding edge from', a[1], 'to', a[0]
            time_zone_graph.add_edge(a[1],a[0]) # user1 <--- user2
        else:
            print a[1], 'is not following', a[0]
    
        print '\n'
        ctr += 1
    except tweepy.TweepError:
        print '\t', 'rate limit excedded; sleeping for 15 mintues'
        time.sleep(60*15) # sleep for 15 minutes after being rate limited to use show_frienship() function again
        print '\t','resuming progress....'      
        continue
        
print 'writing to gexf file'
nx.write_gexf(time_zone_graph,'/home/johnboy/Desktop/Twitter_Locavore_User_Desc_SNA_ecuador_time_graph.gexf')    