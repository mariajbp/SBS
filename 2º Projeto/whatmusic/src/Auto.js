import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import './Css/Music.css';

export default function ComboBox() {
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
        <div className="AutoCompleteBoxes">
            <Autocomplete
                id="combo-box-demo"
                options={artist}
                onChange={(event, chosenArtist) => getSongsByArtist(chosenArtist)}
                getOptionLabel={(option) => option}
                style={{ width: 300 }}
                renderInput={(params) => <TextField {...params} label="Pesquisar artista" variant="outlined" />}

            />
            <Autocomplete
                id="combo-box-demo"
                options={song}
                onChange={(event, chosenSong) => getSuggestions(chosenSong, artist)}
                getOptionLabel={(option) => option}
                style={{ width: 300 }}
                renderInput={(params) => <TextField {...params} label="Pesquisar música" variant="outlined" />}
            />
            <div className="Music-List">
                <ol>
                    {suggestedSongs.map((m) =>
                        <li> {m}  </li>
                    )}
                </ol>
            </div>
        </div>

    );
}