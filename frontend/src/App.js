
import React from 'react'
import { Switch, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Quiz from './pages/Quiz'
import Results from './pages/Results'

import './App.css';

function App() {
  return (
    <>
    <h1>heyyy</h1>
      {/* <Router> */}
          <Routes>
              <Route path='/aa' element={<Home />}/>
              <Route path={'/Quiz'} component={Quiz}/>
              <Route path={'/Results'} component={Results}/>
          </Routes>
      {/* </Router> */}
    </>
    
  );
}

export default App;