import React, { Component } from 'react';
import Slider from 'react-rangeslider';
import 'react-rangeslider/lib/index.css';
import '../stylesheets/builder.scss'

class Builder extends Component {
  state = {
    songs: [],
    num_sets: 1,
  };

  componentDidMount() {
    $.ajax({
      url: '/builder_api/init/',
      datatype: 'json',
      cache: false,
      success: function(data) {
        this.setState({ songs: data.songs });
      }.bind(this),
    });
  }

  handleOnSliderChange = value => {
    this.setState({
      num_sets: value,
    });
  };

  listSongs = () => {
    const songList = this.state.songs.map(song => {
      return <li key={song.id}>{song.title}</li>;
    });

    return songList;
  };

  render() {
    const { num_sets } = this.state;

    return (
      <div className="Builder">
        <h1>Builder</h1>
        <div className="slider-horizontal">
          <label>Number of sets</label>
          <Slider
            min={1}
            max={5}
            step={1}
            value={num_sets}
            onChange={this.handleOnSliderChange}
          />
          <div className="value">{num_sets}</div>
        </div>
        <ul>{this.listSongs()}</ul>
      </div>
    );
  }
}

export default Builder;
