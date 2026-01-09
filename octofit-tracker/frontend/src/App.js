import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Teams from './components/Teams';
import Users from './components/Users';
import Activities from './components/Activities';
import Workouts from './components/Workouts';
import Leaderboard from './components/Leaderboard';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container">
            <Link className="navbar-brand" to="/">OctoFit Tracker</Link>
            <div className="navbar-nav">
              <Link className="nav-link" to="/teams">Teams</Link>
              <Link className="nav-link" to="/users">Users</Link>
              <Link className="nav-link" to="/activities">Activities</Link>
              <Link className="nav-link" to="/workouts">Workouts</Link>
              <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
            </div>
          </div>
        </nav>
        <Routes>
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/" element={<div className="container mt-4"><h1>Welcome to OctoFit Tracker</h1><p>Select a section from the navigation.</p></div>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;