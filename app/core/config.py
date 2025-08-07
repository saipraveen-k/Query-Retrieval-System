import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    PINECONE_ENV = os.getenv('PINECONE_ENV')
    PINECONE_INDEX = os.getenv('PINECONE_INDEX')
    DATABASE_URL = os.getenv('DATABASE_URL')

settings = Settings()
