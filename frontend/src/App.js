import React, { Component } from 'react';
import { Route } from 'react-router-dom';
import Home from './components/Home';
import Builder from './components/Builder';
import Results from './components/Results';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Route exact path="/" component={Home} />
        <Route exact path="/builder" component={Builder} />
        <Route exact path="/builder/results" component={Results} />
      </div>
    );
  }
}

export default App;
