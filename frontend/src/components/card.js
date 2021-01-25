import React, { Component } from 'react';
import Contacts from './contact';

class Card extends Component {
  state = {
    contacts: []
  }
  componentDidMount() {
    fetch('http://jsonplaceholder.typicode.com/users')
    .then(res => res.json())
    .then((data) => {
      this.setState({ contacts: data })
    })
    .catch(console.log)
  }

  render() {
    return (
      <Contacts contacts={this.state.contacts} />
    )
  }
}


export default Card;