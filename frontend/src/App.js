import React, { Component } from 'react';
import {Route, Switch, BrowserRouter} from 'react-router-dom';
import ListUnit from "./components/ListUnit";
import Sidebar from "./components/Sidebar";
import Content from "./components/Content"
import './css/style.css'

const items = [
  { name: 'home', label: 'Home' },
  { name: 'sensors', label: 'Sensors' },
  { name: 'unit', label: 'Units' },
]

class App extends Component {
  render() {
  return (
    <BrowserRouter>
        <div className="wrapper d-flex align-items-stretch">
            <Sidebar items={items} />
            <Content/>
        </div>

    </BrowserRouter>
  );
  }
}

export default App;