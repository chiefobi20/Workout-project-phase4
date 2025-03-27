import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";

function App() {
  const [users, setUsers] = useState([])
  console.log(users)

  useEffect(getUsers, [])

  function getUsers(){
    fetch('/users')
    .then((response) => response.json())
    .then((usersData) => {
      setUsers(usersData)
    })
  }

  return <h1>Project Client</h1>;
}

export default App;
