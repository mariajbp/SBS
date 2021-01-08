import React, { useState, useEffect } from 'react';
import Footer from "./components/Footer";
import { ReactComponent as Logo } from './logo.svg';
import Autocomplete from '@material-ui/lab/Autocomplete';
import TextField from '@material-ui/core/TextField';
import axios from 'axios';
import './Css/Mood.css';

function Mood() {

  const [mood, setMood] = useState(0);
  useEffect(() => {
    fetch('/getMoods').then(res => res.json()).then(data => {
      setMood(data.list);
    });
  }, []);

  const [songsbyMood, setsongsbyMood] = useState([])
  const getMood = async function getMood(c) {
    const params = { mood: c }
    await axios.get('http://localhost:5000/getMoodSuggestions', { params })
      .then(res => {
        let songsbyMood = res.data.moodList
        setsongsbyMood(songsbyMood)
      });
  }

  return (
    <div className="Mood">
      <header className="Mood-header">
        <Logo className="Logo" />
        <div className="HeaderText"> <p> Como te sentes hoje? </p> </div>
        <Autocomplete
          id="combo-box-demo"
          options={mood}
          onChange={(event, v) => getMood(v)}
          style={{ width: 300 }}
          renderInput={(params) => <TextField {...params} label="Conta-nos..." variant="outlined" />}
        />
        <div className="AutoCompleteBoxes">
        </div>

        <div className="Music-List">
          <ol>
            <br></br>
            {songsbyMood.map((m) =>
              <li> {m[0]} - {m[1]}  </li>
            )}
          </ol>
        </div>
        <div className="smallerText"> <p> Em função do teu estado de espírito sugerimos-te as músicas cuja ??? </p> <p> mais se adequa ao ambiente um uma merda qualquer genérica que pareça bem</p> </div>
      </header>

      <Footer />
    </div>
  );

}
export default Mood;
