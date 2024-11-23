Auto-Bot: Automobile FAQ Chatbot
Auto-Bot is an AI-powered chatbot designed to answer frequently asked questions (FAQs) about automobiles. Built with a modular architecture, it combines the power of Natural Language Processing (NLP) using spaCy and TF-IDF vectorization with a dynamic and interactive UI created in React.js.

Features
Dynamic Query Handling: Understands user queries and provides relevant responses using TF-IDF and cosine similarity.
Interactive Chat Interface: A user-friendly UI for seamless real-time interactions.
Scalable Backend: RESTful API built with FastAPI for efficient communication between frontend and backend.
Modular Design: Easily extensible components for future enhancements.
Cross-Origin Compatibility: Ensured smooth integration between backend and frontend using CORS middleware.
Demo
Chatbot Interface:

Tech Stack
Frontend
React.js
HTML5, CSS3
Fetch API for RESTful communication
Backend
FastAPI (Python)
TF-IDF vectorization (scikit-learn)
NLP preprocessing using spaCy
JSON for response storage
Other Tools
CORS Middleware
Uvicorn (server)
How It Works
User Query: The user types a query into the chatbot interface.
Frontend to Backend Communication: The query is sent to the backend via a POST request.
Intent Detection:
TF-IDF Vectorization: Matches the user query against predefined patterns in the JSON dataset.
Cosine Similarity: Determines the most relevant intent.
Response Generation: Based on the detected intent, an appropriate response is fetched from the dataset.
Response Display: The chatbot UI displays the response in real time.
Installation and Setup
Follow these steps to set up and run the project:
Backend Setup
1.Clone this repository

git clone https://github.com/yourusername/auto-bot.git
cd auto-bot/backend
2. Create and activate a virtual environment:
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3.Install dependies
pip install -r requirements.txt
4. Run the server background
uvicorn main:app --reload

Frontend setup
1. Navigate to the frontend folder
cd ../frontend

2. Install dependies
npm install

3. Start the React development server:
npm start

Usage
Open the chatbot interface in your browser (http://localhost:3000).
Start interacting with Auto-Bot by asking automobile-related questions!
Example Queries:

"What is the best car for long drives?"
"Tell me about electric cars."
"What is the fuel efficiency of SUVs?"
