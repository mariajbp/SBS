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
genres = pd.read_csv("Data/genres.csv", sep = ",",
                            engine = 'python', encoding = 'utf8')

#print(songsClusters.head())

first = songsNormalized.iloc[0]

def suggestSongs(name, artist):
    
    song = songsNormalized.copy()
    song = song[(song['name'] == name) & 
                (song['artists'] == artist)]
    
    print(song)
    if song.empty:
        print('Song not available... try again')
        return
    
    song = song.iloc[0]
    
    dif = pd.DataFrame()
    
    song = song.drop(columns = ['artists', 'name'])
    print(song)
    print(centroids)
    
    for i in range(len(centroids)):
        dif = dif.append(song, ignore_index = True)
        
    dif = (pow((centroids - dif), 2))
    dif = dif.sum(axis = 1)
    dif = dif.apply(np.sqrt)
        
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
    
    print(songsSugested[['artists', 'name']].head(8))


def suggestSongsByGenre(name):
    
    genre = genres[genres['genres'] == name]
    
    #print(genre)
    
    if genre.empty:
        print('Something went wrong :(')
        return
        
    dif = pd.DataFrame()
    
    genre = genre.drop(columns = 'genres')
    #print(centroids)
    
    for i in range(len(centroids)):
        dif = dif.append(genre, ignore_index = True)
        
    dif = (pow((centroids - dif), 2))
    dif = dif.sum(axis = 1)
    dif = dif.apply(np.sqrt)
        
    min = dif[0]
    cluster = 0
    
    for i in range(len(dif)):
        if dif[i] < min:
            min = dif[i]
            cluster = i
    
    #print("Min: ", min, " and cluster: ", cluster)
    
    
    songsSugested = songsClusters[songsClusters['Cluster'] == ('cluster_' + str(cluster))]
    ss = songsSugested[['artists', 'name']].head(8).to_json()
    return(ss)
    #print(songsSugested[['artists', 'name']].head(8))


#suggestSongs(first['name'], first['artists'])

#suggestSongs('Give Me Love', 'Ed Sheeran')
#suggestSongs("Let's Love", 'David Guetta')

#suggestSongs('Toxic', 'Britney Spears')

#suggestSongsByGenre('Pop')
