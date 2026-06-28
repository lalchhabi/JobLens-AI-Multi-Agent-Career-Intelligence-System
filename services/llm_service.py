# Import libraries
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import time
from utils.logger import get_logger

# Initialize the logger
logger = get_logger(__name__)

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


