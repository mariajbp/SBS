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

lyrics = pd.read_csv("Data/Lyrics.csv", sep = ",",
                           engine = 'python', encoding = 'utf8')

def suggestSongs(name, artist, numberSongs):
    
    song = songsNormalized.copy()
    song = song[(song['name'] == name) & 
                (song['artists'] == artist)]
    
    #print(song)
    if song.empty:
        print('Song not available... try again')
        return
    
    song = song.iloc[0]
    
    dif = pd.DataFrame()
    
    song = song.drop(columns = ['artists', 'name'])
    #print(song)
    #print(centroids)
    
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
    
    #print("Min: ", min, " and cluster: ", cluster)
    
    
    songsSugested = songsClusters[songsClusters['Cluster'] == ('cluster_' + str(cluster))]
    songsSugested = songsSugested[(songsSugested['artists'] != first['artists']) & 
                                  (songsSugested['name'] != first['name'])]
    
    songsSugested = songsSugested.drop_duplicates(subset = 'artists', keep = 'first')
    #print(songsSugested[['artists', 'name']].head(numberSongs))
    
    
    # Meter inteiro para sabermos se e pretendido haver artistas repetidos ou nao
    return songsSugested[['artists', 'name']].head(numberSongs).to_json(orient = 'split')


def suggestSongsByGenre(name, numberSongs):
    
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
    
    songsSugested = songsSugested.drop_duplicates(subset = 'artists', keep = 'first')
    print(songsSugested[['artists', 'name']].head(numberSongs))
    
    return songsSugested[['artists', 'name']].head(numberSongs).to_json(orient = 'split')


def nearestSongs(name, artist, numberSongs):
    
    #print(name)
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
            
    songsSugested = songsClusters.copy()
    songsSugested = songsSugested[songsSugested['Cluster'] == ('cluster_' + str(cluster))]
    
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
    #print(songs[['artists', 'name']].head(numberSongs))
    
    songs = getLyrics(songs.head(int(numberSongs)))
    
    songs['whyrecommend'] = whyRecommend(cluster)

    return songs[['artists', 'name',
                  'apple_music_player_url', 'header_image_thumbnail_url',
                  'url', 'whyrecommend']].to_json(orient = 'split')


def getArtists():
    
    artists = songsNormalized.copy()
    artists = artists.drop_duplicates(subset = 'artists', keep = 'first')
    
    artists = artists['artists']
    
    #print(list(artists))
    
    return list(artists) 


def getSongsByArtist(artist):
    
    songs = songsNormalized.copy()    
    songs = songs[songs['artists'] == artist]
    
    #print(list(songs['name']))
    
    return list(songs['name'])

'''
['valence', 'year', 'acousticness', 'danceability',
 'duration_ms', 'energy', 'instrumentalness', 'liveness',
 'loudness','speechiness', 'tempo']
'''

def getSongsByMood(mood, numberSongs):
    
    numericValues = ['valence', 'acousticness', 'danceability',
       'duration_ms', 'energy', 'instrumentalness', 'liveness', 
       'loudness','speechiness', 'tempo']   
    
    if mood == 'happy':
        m = [1, 0.5, 0.75,
         0.5, 0.5, 0.5, 0.5,
         0.5, 0.5, 0.5]
        mDf = pd.DataFrame(columns = numericValues)
        
        mDf.loc[-1] = m
        mDf.index = mDf.index + 1
        mDf = mDf.sort_index()
        
    elif mood == 'cheered':
        m = [1, 0.5, 1,
           0.5, 1, 0.5, 0.5,
           1, 0, 1]
        mDf = pd.DataFrame(columns = numericValues)
        
        mDf.loc[-1] = m
        mDf.index = mDf.index + 1  
        mDf = mDf.sort_index()
        
    elif mood == 'relaxed':
        m = [0.75, 1, 0,
           0.5, 0, 0.5, 0.5,
           0.25, 0.5, 0.25]
        mDf = pd.DataFrame(columns = numericValues)
        
        mDf.loc[-1] = m
        mDf.index = mDf.index + 1  
        mDf = mDf.sort_index()
    else:
        m = [0, 0.75, 0.25,
       0.5, 0, 0.5, 0.5,
       0.25, 0.5, 0.5]
        mDf = pd.DataFrame(columns = numericValues)

        mDf.loc[-1] = m
        mDf.index = mDf.index + 1  
        mDf = mDf.sort_index()

    #print(mDf)
    
    songs = songsNormalized.copy()
    
    dist = pd.DataFrame()
    
    tam = 1000
        
    for i in range(tam):
        dist = dist.append(mDf, ignore_index = True)
        
    #print ('dist apos append:\n', dist)
    
    
    dist = (pow((songs.head(tam)[numericValues] - dist), 2))
    dist = dist.sum(axis = 1)
    dist = dist.apply(np.sqrt)
    
    dist = dist[dist != 0]
    dist = dist.sort_values(ascending = True)
    
    listSongs = dist.index
    
    songsByMood = pd.DataFrame()
    for i in range(len(listSongs)):
        songsByMood = songsByMood.append(songs.iloc[listSongs[i]])
    
    return (songsByMood[['artists', 'name']].head(numberSongs).head(numberSongs).to_json(orient = 'split'))
    
    
def getLyrics(songs):
    songs = songs.merge(lyrics, how = 'left',
               left_on = ['name', 'artists'], 
               right_on = ['name', 'artists'])
    
    songs = songs.fillna('')
    #print(songs[['artists', 'name', 'url']])
    
    return songs

def whyRecommend(cluster):
    
    centroid = centroids.iloc[cluster]
        
    listPrincipalGenres = []
        
    for i in range(11, 24):
        if centroid[i] > 0.5:
            listPrincipalGenres.append(centroid.index[i])
    
    string = ', '.join(listPrincipalGenres)
    
    return """Recomendamos-te estas músicas, porque encontram-se
        dentro dos mesmos géneros de músicas que a inserida: {}.
        \nAchamos que és capaz de gostar!""".format(string) 
        
    #print(listPrincipalGenres)
    #return listPrincipalGenres
        
def whyRecommendMood(mood):
    
    if mood == 'happy':
        return """Recomendamos-te estas músicas pois apresentam bastante positividade na letra, dançabilidade e 
        energia alta"""
    elif mood == 'cheered':
        return """Recomendamos-te estas músicas pois apresentam bastante positividade na letra, dançabilidade, energia elevada e 
        um ritmo elevado"""
    elif mood == 'relaxed':
        return """Recomendamos-te estas músicas pois apresentam positividade na letra, contudo não têm dançabilidade, são de baixa energia, 
        acústicas e com ritmo lento"""
    elif mood == 'sad':
        return """Recomendamos-te estas músicas pois têm negatividade na letra, sem dançabilidade e baixa energia, 
        com ritmo lento e mais calma"""    
        


#getSongsByMood('relaxed', 10)

#suggestSongs(first['name'], first['artists'])

#suggestSongs('Toxic', 'Britney Spears')
#suggestSongs("Black", 'Pearl Jam')

#suggestSongsByGenre('Rock')

#suggestSongsByGenre('Pop')

#print(nearestSongs('Stressed Out', 'Twenty One Pilots', 10))
#nearestSongs('Ironic - 2015 Remaster', "Alanis Morissette")
#nearestSongs("Black", 'Pearl Jam', 5)

#getSongsByArtist('Pearl Jam')