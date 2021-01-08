import React, { useState, useEffect } from 'react';
import Footer from "./components/Footer";
import { ReactComponent as Logo } from './logo.svg';
import Autocomplete from '@material-ui/lab/Autocomplete';
import TextField from '@material-ui/core/TextField';
import axios from 'axios';
import './Css/Concerts.css';

function Concerts() {

    const [country, setCountries] = useState(0);
    useEffect(() => {
        fetch('/getCountries').then(res => res.json()).then(data => {
            setCountries(data.list);
        });
    }, []);

    const [concerts, setConcerts] = useState([])
    const getConcerts = async function getConcerts(c) {
        const params = { country: c }
        await axios.get('http://localhost:5000/getConcertsFromCountry', { params })
            .then(res => {
                let song = res.data.concertList
                setConcerts(concerts)
            });
    }

    return (
        <div className="Concerts">
            <header className="Concerts-header">
                <Logo className="Logo" />
                <div className="HeaderText"> <p> Queres saber quais os concertos perto de ti? </p> </div>
                <Autocomplete
                    id="combo-box-demo"
                    options={country}
                    onChange={(event, v) => getConcerts(v)}
                    style={{ width: 300 }}
                    renderInput={(params) => <TextField {...params} label="Indica o teu pais" variant="outlined" />}
                />
                <div className="AutoCompleteBoxes">
                </div>
            </header>
            <Footer />
        </div>
    );

}
export default Concerts;
