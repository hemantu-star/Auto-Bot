from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from responses import ecommerce_responses
import random

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Define the data model for the user's input
class UserInput(BaseModel):
    message: str

# Flatten responses for vectorization
all_responses = []
response_mapping = {}
index = 0
for category, responses in ecommerce_responses.items():
    for response in responses:
        all_responses.append(response)
        response_mapping[index] = (category, response)
        index += 1

# Initialize the TF-IDF vectorizer
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(all_responses)

def process_message(message):
    # Process the user's message using spaCy
    doc = nlp(message.lower())
    
    # Extract important keywords from the message
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]
    
    if not keywords:
        return random.choice(ecommerce_responses["default"])
    
    try:
        user_vector = tfidf.transform([message])
        similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
        
        # Get top 3 most similar responses
        top_indices = similarities.argsort()[-3:][::-1]
        
        # If the best similarity is too low, return a default response
        if similarities[top_indices[0]] < 0.1:
            return random.choice(ecommerce_responses["default"])
        
        # Return the response with highest similarity
        category, response = response_mapping[top_indices[0]]
        return response
        
    except Exception as e:
        return random.choice(ecommerce_responses["default"])

# Define the API endpoint to handle the user's message
@app.post("/chat")
async def chat(user_input: UserInput):
    response = process_message(user_input.message)
    return {"response": response}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)