import React, { useState, useEffect } from 'react';
import { ReactComponent as Logo } from './logo.svg';
import './App.css';

function App() {

  const [currentTime, setCurrentTime] = useState(0);
  useEffect(() => { fetch('/time').then(res => res.json()).then(data => { setCurrentTime(data.time); });}, []);

  return (
    <div className="App">
      <header className="App-header">

        <Logo className="App-logo" />
        <p>The current time is {currentTime}.</p>
      </header>
      <View style={{ flexDirection: "row" }}>
    <View style={styles.buttonStyle}>
        <Button title={"Button 11"}/>
        <Button title={"Button 12"}/>
    </View>
    <View style={styles.buttonStyle}>
        <Button title={"Button 21"}/>
        <Button title={"Button 22"}/>
    </View>
</View>
    </div>
  );




}


export default App;
