import time
import json
from SelectMusics import suggestSongsByGenre, suggestSongs
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
    l = suggestSongsByGenre(g)
    print(l)
    return {'list': l}

############ Music API ############

@app.route('/getArtists')
def getArtist():
    l = ['m','mar','maria', 'cris']
    return {'list': l}

@app.route('/getSongsByArtist', methods = ['GET', 'POST'])
def getSongsArtist():
    a = request.args.get('artist', None)
    l = ['Song1', 'Song2']
    return {'list': l}