import React, { useState, useEffect } from 'react';
import { ReactComponent as Logo } from './logo.svg';
import Footer from "./components/Footer";
import './App.css';

function App() {

  const [currentTime, setCurrentTime] = useState(0);
  useEffect(() => { fetch('/time').then(res => res.json()).then(data => { setCurrentTime(data.time); });}, []);

  return (
    <div className="App">
      <header className="App-header">

        <Logo className="App-logo" />
        <Buttons/>
        <p>The current time is {currentTime}.</p>
      </header>
      <Footer/>
    </div>
  );


}

export default App;
