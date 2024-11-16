import React, { useState } from 'react';
import './Chatbot.css';

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState('');

  const handleSend = async () => {
    if (userInput.trim() === '') return; // Prevent sending empty messages

    // Add user input to messages with sender as 'user'
    setMessages([...messages, { sender: 'user', text: userInput }]);

    // Make POST request to backend with user's message
    const response = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: userInput }),
    });
    const data = await response.json();

    // Add the bot's response to the messages
    setMessages([...messages, { sender: 'bot', text: data.response }]);

    // Clear the user input
    setUserInput('');
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chat-display">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message-bubble ${msg.sender === 'user' ? 'user-bubble' : 'bot-bubble'}`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="Ask me anything..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default Chatbot;