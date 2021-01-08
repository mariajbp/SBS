import React, { useState, useEffect } from 'react';
import Footer from "./components/Footer";
import { ReactComponent as Logo } from './logo.svg';
import CustomizedRatings from "./components/Rate";
import axios from 'axios';
import './Css/Mood.css';

function Mood() {

  const [songsbyMood, setsongsbyMood] = useState([])
  const handleClick = async function handleClick(e) {
    textS(e)
    const params = { mood: e }
    await axios.get('http://localhost:5000/handleMood', { params })
      .then(res => {
        let songsbyMood = JSON.parse(res.data.list).data
        setsongsbyMood(songsbyMood);
      });
  }

  const [text, setText] = useState([])
  const textS = async function textS(e) {
    const params = { mood: e }
    await axios.get('http://localhost:5000/moodText', { params })
      .then(res => {
        let text = res.data.mood
        setText(text)
      });
  }

  return (
    <div className="Mood">
      <header className="Mood-header">
        <Logo className="Logo" />
        <div className="HeaderText"> <p> Como te sentes hoje? </p> </div>
        <div className="btn-group">
          <button onClick={e => handleClick("relaxed")} type="button" className="btn btn-danger"> Relaxado </button>
          <button onClick={e => handleClick("happy")} type="button" className="btn btn-danger ">  Feliz </button>
          <button onClick={e => handleClick("sad")} type="button" className="btn btn-danger "> Triste </button>
          <button onClick={e => handleClick("cheered")} type="button" className="btn btn-danger "> Animado </button>
        </div>


        <div className="Music-List">
          <ol>
            <br></br>
            {songsbyMood.map((m) =>
              <li> {m[0]} - {m[1]}  </li>
            )}
          </ol>
        </div>

        <div className="smallerText"> <p> {text} </p> </div>
        
        {<CustomizedRatings />}
      </header>

      <Footer />
    </div>
  );

}
export default Mood;
