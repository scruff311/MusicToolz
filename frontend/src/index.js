import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { BrowserRouter as Router } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.css';

// import registerServiceWorker from './registerServiceWorker';

// window.React = React;

ReactDOM.render(
  // <App />,
  <Router>
    <App />
  </Router>,
  document.getElementById('root'),
);
// registerServiceWorker();
