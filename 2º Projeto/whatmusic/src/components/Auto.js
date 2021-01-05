import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';

export default function ComboBox() {
    const [artist, setArtists] = useState(0);
    useEffect(() => { fetch('/getArtists').then(res => res.json()).then(data => { setArtists(data.list); }); }, []);
    console.log(artist);

    const [song, setSongs] = useState([])
    const getSongList = async function getSongList(a) {
        const params = { artist: a }
        await axios.get('http://localhost:5000/getSongsByArtist', { params })
            .then(res => {
                let song = JSON.parse(res.data.list).data
                console.log(song)
                setSongs(song)
            });
    }



    return (
        <div className="AutoCompleteBoxes">
            <Autocomplete
                id="combo-box-demo"
                options={artist}
                getOptionLabel={(option) => option}
                style={{ width: 300 }}
                renderInput={(params) => <TextField {...params} label="Pesquisar por artista" variant="outlined" />}

            />
            <Autocomplete
                id="combo-box-demo"
                onChange={(event, v) => console.log(v)}
                options={song}
                getOptionLabel={(option) => option}
                style={{ width: 300 }}
                renderInput={(params) => <TextField {...params} label="Pesquisar música" variant="outlined" />}
            />
        </div>

    );
}