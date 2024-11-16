// App.js
import React from 'react';
import './App.css';
import Chatbot from './components/Chatbot';

function App() {
  return (
    <div className="App">
      <div className='chat-container'>
      <h1>Welcome to E-commerce Chatbot</h1>
      <Chatbot />
      </div>
    </div>
  );
}

export default App;
