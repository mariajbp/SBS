"""
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
    
    songsSugested = songsSugested.drop_duplicates(subset = 'artists', keep = 'first')
    print(songsSugested[['artists', 'name']].head(8))
    
    return songsSugested[['artists', 'name']].head(8).to_json(orient = 'split')


def suggestSongsByGenre(name):
    
    genre = genres[genres['genres'] == name]
    
    print(genre)
    
    if genre.empty:
        print('Something went wrong :(')
        return
        
    dif = pd.DataFrame()
    
    genre = genre.drop(columns = 'genres')
    print(centroids)
    
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
    
    print("Min: ", min, " and cluster: ", cluster)
    
    
    songsSugested = songsClusters[songsClusters['Cluster'] == ('cluster_' + str(cluster))]
    
    songsSugested = songsSugested.drop_duplicates(subset = 'artists', keep = 'first')
    print(songsSugested[['artists', 'name']].head(8))
    
    return songsSugested[['artists', 'name']].head(8).to_json(orient = 'split')


def nearestSongs(name, artist):
    
    song = songsNormalized.copy()
    songWithName = song.copy()
    song = song[(song['name'] == name) & 
                (song['artists'] == artist)]
    
    if song.empty:
        print('Song not available... try again')
        return
    
    song = song.iloc[0]
    
    dif = pd.DataFrame()
    
    song = song.drop(columns = ['artists', 'name'])
    
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
    
    print('cluster: ', cluster)
        
    songsSugested = songsClusters.copy()
    songsSugested = songsSugested[songsSugested['Cluster'] == ('cluster_' + str(cluster))]
    songsSugested = songsSugested[(songsSugested['artists'] != first['artists']) & 
                                  (songsSugested['name'] != first['name'])]
    
    songsSugested = songsSugested.drop(columns = 'Cluster')
    
    
    dist = pd.DataFrame()
    
    numericValues = ['valence', 'year', 'acousticness', 'danceability',
       'duration_ms', 'energy', 'instrumentalness', 'liveness', 'loudness',
       'speechiness', 'tempo', 'Rock', 'Pop', 'Rap/Hip hop',
       'Eletronic/Dance', 'Latin', 'Indie', 'Classical', 'Country', 'Metal',
       'Blues', 'Other', 'Soul', 'Jazz', 'Punk']
    
    if len(songWithName) > 100:
        tam = 100
    else:
        tam = len(songWithName)
        
    for i in range(tam):
        dist = dist.append(songsSugested[numericValues], ignore_index = True)
        
    dist = (pow((songWithName.head(tam)[numericValues] - dist), 2))
    dist = dist.sum(axis = 1)
    dist = dist.apply(np.sqrt)
    
    dist = dist[dist != 0]
    dist = dist.sort_values(ascending = True)
    
    listSongs = dist.index
    
    songs = pd.DataFrame()
    for i in range(len(listSongs)):
        songs = songs.append(songsSugested.iloc[listSongs[i]])
        
    songs = songs.drop_duplicates(subset = 'artists', keep = 'first')
    print(songs[['artists', 'name']].head(8))
    
    return songs[['artists', 'name']].head(8).to_json(orient = 'split')

#suggestSongs(first['name'], first['artists'])

#suggestSongs('Toxic', 'Britney Spears')
#suggestSongs("Black", 'Pearl Jam')

#suggestSongsByGenre('Rock')

#suggestSongsByGenre('Pop')

#nearestSongs('Stressed Out', 'Twenty One Pilots')
#nearestSongs('Ironic - 2015 Remaster', "Alanis Morissette")
nearestSongs("Black", 'Pearl Jam')
