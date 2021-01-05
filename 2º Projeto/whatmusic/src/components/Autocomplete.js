import React, { useState, useEffect } from 'react';
import { ReactSearchAutocomplete } from 'react-search-autocomplete'

function Autocomplete() {
    const [artist, setArtists] = useState(0);
    useEffect(() => { fetch('/getArtists').then(res => res.json()).then(data => { setArtists(data.list); }); }, []);
    console.log(artist);

  const handleOnSearch = (string, cached) => {
    // onSearch returns the string searched and if
    // the values are cached. If the values are cached
    // "cached" contains the cached values, if not, returns false
    console.log(string, cached)
  }

  const handleOnSelect = (item) => {console.log(item)}

  const handleOnFocus = () => {console.log('Focused')}

  return (
    <div className="App">
      <header className="App-header">
        <div style={{ width: 400 }}>
          <ReactSearchAutocomplete
            items={artist}
            onSearch={handleOnSearch}
            onSelect={handleOnSelect}
            onFocus={handleOnFocus}
            autoFocus
          />
        </div>
      </header>
    </div>
  )
}

export default Autocomplete