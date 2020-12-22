import React, { useState, useEffect } from 'react';
import {Link } from "react-router-dom";
import { ReactComponent as Logo } from './logo.svg';
import Footer from "./components/Footer";
import './App.css';
import { Button } from "reactstrap";

function App() {


  return (
    <div className="App">
      <header className="App-header">
        <Logo className="App-logo" />
        <div class="Buttons"> 

          <div class="btn-group">
            <Link to="/page2"><button type="button" class="btn btn-danger">Pesquisar por género</button> </Link> {' '}
            <Link to="/page3"><button type="button" class="btn btn-danger">Pesquisar por música</button> </Link> 

        </div>
        </div>

        <p>The current time is {currentTime}.</p>
      </header>
      <Footer/>
    </div>
  );


}
export default App;


