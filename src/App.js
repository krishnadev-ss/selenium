import './App.css';
import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import User from './components/User';
import Notfound from './components/Notfound';

function App() {
  return (
   <>
      <Router >
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/user" element={<User />} />
            <Route path='/notfound' element={<Notfound />} />
          </Routes>
      </Router>
   
   </>
  );
}

export default App;
