import React from 'react';
import Navibar from './components/navibar';
import Home from "./components/home";
import Search from "./components/search";
import {BrowserRouter, Route} from 'react-router-dom';


function App() {
  return (
      <BrowserRouter>
          <div className="App">
              <Navibar />
              <Route exact path={'/'}>
                  <Home/>
              </Route>
              <Route path={'/search'}>
                  <Search/>
              </Route>
          </div>
      </BrowserRouter>
  );
}

export default App;
