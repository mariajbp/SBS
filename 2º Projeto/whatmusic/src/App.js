import React, { useState, useEffect } from 'react';
import {Link } from "react-router-dom";
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

          <div className="btn-group">
            <Link to="/genre"><button type="button" className="btn btn-danger btn-lg">Pesquisar por género</button> </Link> {' '}
            <Link to="/music"><button type="button" className="btn btn-danger btn-lg">Pesquisar por música</button> </Link> 
          </div>

        
      </header>
      <Footer/>
    </div>
  );


}
export default App;


