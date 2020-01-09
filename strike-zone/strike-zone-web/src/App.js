import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Card} from './components/card'
import {Division} from './components/division'
import {Home} from './pages/home.js'
import {Pitchers} from './pages/pitchers.js'
import {Starts} from './pages/starts.js'
import {BrowserRouter, Route, Switch, withRouter} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/"><Home /></Route>
        <Route path="/team/:tn" render={(props) => <Pitchers {...props} />} />
        <Route path="/player/:pid" render={(props) => <Starts {...props} />} />
      </Switch>
    </BrowserRouter>

  );
}

export default App;
