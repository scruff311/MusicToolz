import React, { Component } from 'react';

class Builder extends Component {
  state = {
    init_msg: '',
  };

  componentDidMount() {
    $.ajax({
      url: '/builder_api/init/',
      datatype: 'json',
      cache: false,
      success: function(data) {
        this.setState({ init_msg: data });
      }.bind(this),
    });
  }

  render() {
    return (
      <div className="Builder">
        <h1>Builder</h1>
        <p>{this.state.init_msg.message}</p>
      </div>
    );
  }
}

export default Builder;
