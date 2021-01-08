import React, { useState, useEffect } from 'react';
import Footer from "./components/Footer";
import CustomizedRatings from "./components/Rate";
import axios from 'axios';
import { ReactComponent as Logo } from './logo.svg';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import './Css/Music.css';


function Music() {
  var n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

  const [artist, setArtists] = useState(0);
  useEffect(() => {
    fetch('/getArtists').then(res => res.json()).then(data => {
      setArtists(data.list);
    });
  }, []);

  const postNumber = async function postNumber(n) {
    const params = { number: n }
    await axios.get('http://localhost:5000/postNumber', { params })
      .then(res => { console.log(res) });
  }

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
  const getSuggestions = async function getSuggestions(s) {
    const params = {
      song: s
    }
    await axios.get('http://localhost:5000/getSuggestedSongs', { params })
      .then(res => {
        let suggestedSongs = JSON.parse(res.data.songList).data
        setSuggestedSongs(suggestedSongs)
      });
  }

  return (
    <div className="Music">
      <header className="Music-header">
        <Logo className="Logo" />
        <div className="HeaderText"> <p> Indica-nos uma música que gostes e sugerimos-te o que ouvir </p> </div>
        <div className="AutoCompleteBoxes">
          <Autocomplete
            id="combo-box-demo"
            options={n}
            onChange={(event, number) => postNumber(number)}
            style={{ width: 150 }}
            renderInput={(params) => <TextField {...params} label="Nº de sugestões" variant="outlined" />}
          />

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
            onChange={(event, chosenSong) => getSuggestions(chosenSong)}
            style={{ width: 300 }}
            renderInput={(params) => <TextField {...params} label="Pesquisar música" variant="outlined" />}
          />
        </div>

        <div className="Music-List">
          <ol>
            <br></br>
            {suggestedSongs.map((m) =>
              <li> {m[0]} - {m[1]}  </li>
            )}
          </ol>
        </div>
        <div className="smallerText"> <p> Com base em wtv estas são as musicas que mais wtvvvv </p> </div>
        {<CustomizedRatings />}
      </header>
      <Footer />
    </div>
  );
}

export default Music;