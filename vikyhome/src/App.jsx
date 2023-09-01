import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import MainPage from './components/page/MainPage';
import NotFound from './components/page/NotFound';
import ServerError from './components/page/ServerError';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="*" element={<NotFound />} />
        <Route path="/500" component={ServerError} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;