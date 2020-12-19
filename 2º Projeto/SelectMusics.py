"""
Created on Sat Dec 19 17:55:04 2020

@author: GRUPO_1_MLFA
"""

import pandas as pd
import numpy as np

songsNormalized = pd.read_csv("Data/Songs_normalized.csv", sep = ",",
                              engine = 'python', encoding = 'utf8')
centroids = pd.read_csv("Data/centroids.csv", sep = ",",
                        engine = 'python', encoding = 'utf8')
songsClusters = pd.read_csv("Data/Songs_clusters.csv", sep = ",",
                            engine = 'python', encoding = 'utf8')

print(songsClusters.head())

first = songsNormalized.iloc[0]

def suggestSongs(name, artist):
    
    song = songsNormalized[(songsNormalized['name'] == name) &
                           (songsNormalized['name'] == artist)]
    
    dif = pd.DataFrame()
    
    dif = (pow(song-centroids, 2)).drop(columns = ['artists', 'name'])
    dif = dif.sum(axis = 1)
    dif = dif.apply(np.sqrt)
    
    print(dif)
    
    min = dif[0]
    cluster = 0
    
    for i in range(len(dif)):
        if dif[i] < min:
            min = dif[i]
            cluster = i
    
    print("Min: ", min, " and cluster: ", cluster)
    
    
    songsSugested = songsClusters[songsClusters['Cluster'] == ('cluster_' + str(cluster))]
    songsSugested = songsSugested[(songsSugested['artists'] != first['artists']) & 
                                  (songsSugested['name'] != first['name'])]
    
    print(songsSugested[['artists', 'name']].head(4))



suggestSongs(first['name'], first['artists'])