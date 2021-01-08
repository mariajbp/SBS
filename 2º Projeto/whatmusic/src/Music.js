import React, { useState, useEffect } from 'react';
import Footer from "./components/Footer";
import CustomizedRatings from "./components/Rate";
import axios from 'axios';
import { ReactComponent as Logo } from './logo.svg';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import './Css/Music.css';
import { Link } from 'react-router-dom';
import { Button } from 'reactstrap';


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
    getTxt(s)
    const params = {
      song: s
    }
    await axios.get('http://localhost:5000/getSuggestedSongs', { params })
      .then(res => {
        let suggestedSongs = JSON.parse(res.data.songList).data
        setSuggestedSongs(suggestedSongs); 
      });
  }

  const [txt, setTxt] = useState([])
  const getTxt = async function getTxt(s) {
    const params = {
      song: s
    }
    await axios.get('http://localhost:5000/getSuggestedSongs', { params })
      .then(res => {
        let txt = JSON.parse(res.data.songList).data
        setTxt(txt[0][5]);
      });
  }


  return (
    <div className="Music">
      <header className="Music-header">
        <Logo className="Logo" />
        <div className="HeaderText"> <p> Indica-nos uma música que gostes e sugerimos-te o que ouvir </p> </div>
        <div className="AutoCompleteBoxes">
          <Autocomplete
            options={n}
            onChange={(event, number) => postNumber(number)}
            style={{ width: 150 }}
            renderInput={(params) => <TextField {...params} label="Nº de sugestões" variant="outlined" />}
          />

          <Autocomplete
            options={artist}
            onChange={(event, chosenArtist) => getSongsByArtist(chosenArtist)}
            style={{ width: 300 }}
            renderInput={(params) => <TextField {...params} label="Pesquisar artista" variant="outlined" />}
          />

          <Autocomplete
            options={song}
            onChange={(event, chosenSong) => getSuggestions(chosenSong)}
            style={{ width: 300 }}
            renderInput={(params) => <TextField {...params} label="Pesquisar música" variant="outlined" />}
          />
        </div>
        <br></br>
        <div className="smallerText"> <p> {txt} </p> </div>

        <div className="Music-List">
          <ol>
         
            {suggestedSongs.map((m) => 
              <li> {m[0]} - {m[1]}
                <div className="LinkStyle"> <a href={m[4]} >     lyrics - </a> <a href={m[2]} > play </a> </div>
              </li>
            )}
          </ol>
        </div>
    
        {<CustomizedRatings />}
      </header>
      <Footer />
    </div>
  );
}

export default Music;

