import React, { Component } from 'react';
import Units from './Units';

class ListUnit extends Component {
  state = {
    units: []
  }
  componentDidMount() {
    fetch('/api/unit/')
    .then(res => res.json())
    .then((data) => {
      this.setState({ units: data.results })
    })
    .catch(console.log)
  }

  render() {
    return (
      <Units units={this.state.units} />
    )
  }
}


export default ListUnit;