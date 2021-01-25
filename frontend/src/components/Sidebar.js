import React from 'react'
import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
import Footer from './Footer'

function Sidebar({ items }) {
  return (

    <nav id="sidebar" className="sidebar">
        <div className="p-4 pt-5">
            <a  className="img logo rounded-circle mb-5" ></a>
            <ul className="list-unstyled components mb-5">
                {items.map(({ label, name, ...rest }) => (
                  <li key={name} >
                    <a>{label}</a>
                  </li>
                ))}
            </ul>
            <Footer/>
		</div>
    </nav>

  )
}

export default Sidebar