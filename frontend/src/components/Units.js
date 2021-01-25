import React from 'react'

const Units = ({ units }) => {
  return (
    <div>
      <center><h1>Unit List</h1></center>
      {units.map((unit) => (
        <div className="card" key={unit.id}>
          <div className="card-body">
            <h5 className="card-title">{unit.name}</h5>
            <p className="card-text">{unit.description}</p>
          </div>
        </div>
      ))}
    </div>
  )
};

export default Units