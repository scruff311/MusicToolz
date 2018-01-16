import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Home extends Component {
  render() {
    return (
      <div className="Home">
        <h1>Music Toolz</h1>
        <p>
          <Link to={'/builder'}>Carson Daily Setlist Builder</Link>
        </p>
      </div>
    );
  }
}

export default Home;
