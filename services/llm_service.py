# Import libraries
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables 
load_dotenv()
GROQ_API = os.getenv("GROQ_API_KEY")

def get_llm_model():
    """Function to load LLM Model
    """
    groq_model = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=GROQ_API,
        temperature=0
    )
    return groq_model


