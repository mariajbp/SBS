import React, { useState, useEffect } from 'react';
import {Link } from "react-router-dom";
import { ReactComponent as Logo } from './logo.svg';
import Footer from "./components/Footer";
import './App.css';
import { Button } from "reactstrap";

function App() {

  const [currentTime, setCurrentTime] = useState(0);
  useEffect(() => { fetch('/time').then(res => res.json()).then(data => { setCurrentTime(data.time); });}, []);

  return (
    <div className="App">
      <header className="App-header">

        <Logo className="App-logo" />
        <Link to="/page3"> <button> Pesquisar por música </button> </Link>
        <Link to="/page2"> <Button color="danger" size="lg" block>Block level button</Button> </Link>
        <Button color="danger" size="lg" block>Block level button</Button>
        <p>The current time is {currentTime}.</p>

      </header>
      <Footer/>
    </div>
  );


}
export default App;
