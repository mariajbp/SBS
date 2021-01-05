import React, { useState, useEffect } from 'react';
import Footer from "./components/Footer";
import Autocomplete from "./components/Autocomplete";
import ComboBox from "./components/Auto";
import './Music.css';

function Music() {


  return (
    <div className="Music">
      <header className="Music-header">

      <ComboBox/>

      </header>
      <Footer />
    </div>
  );
}

export default Music;