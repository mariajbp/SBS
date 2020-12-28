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

## working post
@app.route('/genrebuttonpost', methods = ['POST'])
def workingpost():
    data =  request.get_json()
    g = data.get('genre', '')
    print(g)
    l = suggestSongsByGenre(g)
    print(l)
    return {'list': l}

############ Music API ############