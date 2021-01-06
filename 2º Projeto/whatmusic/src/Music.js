import React, { useState, useEffect } from 'react';
import Footer from "./components/Footer";
import axios from 'axios';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import './Music.css';

function Music() {

  var number = [1,2]
  const [artist, setArtists] = useState(0);
    useEffect(() => { fetch('/getArtists').then(res => res.json()).then(data => { setArtists(data.list); }); }, []);
    console.log(artist);


    const [song, setSongs] = useState([])
    const getSongsByArtist = async function getSongsByArtist(a) {
        console.log(a)
        const params = { artist: a }
        await axios.get('http://localhost:5000/getSongsByArtist', { params })
            .then(res => {
                let song = res.data.songList
                setSongs(song)
            });
    }

    const [suggestedSongs, setSuggestedSongs] = useState([])
    const getSuggestions = async function getSuggestions(s,a) {
        const params = { artist: a,
                         song: s
                        }
        await axios.get('http://localhost:5000/getSuggestedSongs', { params })
            .then(res => {
                let suggestedSongs = res.data.songList
                setSuggestedSongs(suggestedSongs)
            });
    }


  return (
    <div className="Music">
      <header className="Music-header">

      <div className="AutoCompleteBoxes">
            <Autocomplete
                id="combo-box-demo"
                options={artist}
                onChange={(event, chosenArtist) => getSongsByArtist(chosenArtist)}
                style={{ width: 300 }}
                renderInput={(params) => <TextField {...params} label="Pesquisar artista" variant="outlined" />}

            />
            <Autocomplete
                id="combo-box-demo"
                options={song}
                onChange={(event, chosenSong) => getSuggestions(chosenSong, artist)}
                style={{ width: 300 }}
                renderInput={(params) => <TextField {...params} label="Pesquisar música" variant="outlined" />}
            />

        <Autocomplete
                id="combo-box-demo"
                options={number}
                onChange={(event,n) => console.log(n)}
                style={{ width: 150 }}
                renderInput={(params) => <TextField {...params} label="Nº de sugestões" variant="outlined" />}
            />
        </div>

        <div className="Music-List">
                <ol>
                  <br></br>
                    {suggestedSongs.map((m) =>
                        <li> {m}  </li>
                    )}
                </ol>
            </div>

      </header>
      <Footer />
    </div>
  );
}

export default Music;