import time
import json
from SelectMusics import suggestSongsByGenre, suggestSongs, getArtists, getSongsByArtist, nearestSongs, getSongsByMood, whyRecommendMood
from flask import request
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

############ Genre API ############
@app.route('/genrebuttons', methods = ['GET', 'POST'])
def getSuggestedSongsByGenre():
    g = request.args.get('genre', None)
    l = suggestSongsByGenre(g,10)
    #print(l)
    return {'list': l}

############ Music API ############

@app.route('/getArtists')
def getArtist():
    a = request.args.get('artist', None)
    l  = getArtists()
    return {'list': l}

@app.route('/getSongsByArtist', methods = ['GET', 'POST'])
def getSongsArtist():
    a = request.args.get('artist', None)
    global chosen_artist 
    chosen_artist = a
    l = getSongsByArtist(a)
    return {'songList': l}

@app.route('/getSuggestedSongs', methods = ['GET', 'POST'])
def getSuggestedSongs():
    #usar a nearest
    s = request.args.get('song')
    print(chosen_artist)
    print(s)
    print(option_number)
    l = nearestSongs(s,chosen_artist,option_number)
    print(l)
    return {'songList': l}

@app.route('/postNumber', methods = ['GET', 'POST'])
def postNumberChoices():
    n = request.args.get('number')
    global option_number
    option_number = n
    return {'n': option_number}

############ Mood API ############
@app.route('/handleMood', methods = ['GET', 'POST'])
def getMoods():
    mood = request.args.get('mood')
    print(mood)
    global chosenMood
    chosenMood = whyRecommendMood(mood)
    print(chosenMood)
    l = getSongsByMood(mood, 10)
    print(l)
    return {'list': l}

@app.route('/moodText', methods = ['GET', 'POST'])
def getMoodText():
    m = request.args.get('mood')
    text = whyRecommendMood(m)
    return {'mood': text}

############ Concerts API ############
@app.route('/getCountries', methods = ['GET', 'POST'])
def getCountries():
    #l = 
    return {'list': 'country'}

@app.route('/getConcertsFromCountry', methods = ['GET', 'POST'])
def getConcertCountries():
    #l = 
    return {'concertList': 'country'}

