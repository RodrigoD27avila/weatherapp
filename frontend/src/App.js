import React, { useState, useEffect } from 'react';
import api from './Api';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useParams
} from "react-router-dom";

import './App.css';

function App() {
  return (
    <Router>
        <Switch>
          <Route path="/forecast/:cityid">
            <Forecast />
          </Route>
          <Route path="/">
            <Cities />
          </Route>
        </Switch>
    </Router>
  );
}

function Cities(props) {

  const [city, setCity]     = useState('');
  const [error, setError] = useState('');
  const [cities, setCities] = useState([]);

  function fetchCities() {
    let baseapi = api()
    fetch(`${baseapi}/cities/`).then((response) => {
      if (response.status === 200) {
        response.json().then(function(data) {
          setCities(data.map((element) => {
            return <li key={element.id} className="city"><Link to={"/forecast/" + element.id}>{element.name.charAt(0).toUpperCase() + element.name.slice(1)}</Link></li>
            }))
        })
      }
    })
  }

  function addCity() {
    if (city.trim().length > 3) {
      let baseapi = api()
      fetch(`${baseapi}/cities/`, {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: city})
      }).then((response) => {
        if (response.status === 201) {
          fetchCities();
        } else {
          setCity("")
          response.json().then((message) => {
            setError(message.detail)
            setTimeout(() => {
              setError("")
            }, 2000)
          })
        }
      }).catch((err) => {
        console.log(err)
      })
      setCity("")
    }
  }
  
  useEffect(fetchCities, []);

  return <div>
    <div className="title">
      <h1>ADICIONE UMA CIDADE</h1>
    </div>
    <div className="search-bar">
    <input type="text" className="input-city" value={city}
    onChange={
        (event) => setCity(event.target.value)
    }
    onKeyDown={
      (event) => {
        if (event.key === 'Enter') {
          addCity()
        }
      }
    }></input>
    <button className="button-search" onClick={addCity}>ADICIONAR</button>
    </div>
    <ul className="city-list">{cities}</ul>
    <span className="error">{error}</span>
 </div>
}

function Forecast(props) {
  const [forecast, setForecast] = useState([]);
  const [city, setCity] = useState("");
  let params = useParams()

  function fetchForecast() {
    let baseapi = api()
    fetch(`${baseapi}/cities/${params.cityid}`).then((response) => {
      if (response.status === 200) {
        response.json().then(function(data) {
          setCity(data.name)
          setForecast(
            data.forecast.list.map((element) => {
              return (
                <Weather key={element.dt_txt}
                  date={new Date(element.dt_txt)}
                  temp={element.main.temp}
                  description={element.weather[0].description}
                ></Weather>
              );
            })
          )
        })
      }
    })
  }

  useEffect(fetchForecast, []);

  return <div>
    <div className="title">
      <h1>{city.charAt(0).toUpperCase() + city.slice(1)}</h1>
    </div>
      <ul>{forecast}</ul>
      <Link className="goback" to="/">voltar</Link>
  </div>  

}


function Weather(props) {
  return (
    <li className="card">
      <div>{props.date.getDate() + '/' + (props.date.getMonth()+1) + '/' + props.date.getFullYear() + ' ' + props.date.getHours() + 'hs'}</div>
      <div>{(props.temp - 273.15).toFixed(1)} °C</div>
      <div>{props.description}</div>
    </li>
  );
}

export default App;
