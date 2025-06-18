import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    MONGODB_URI = os.getenv('MONGODB_URI')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'ytmanager')
    COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'videos')
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present"""
        if not cls.MONGODB_URI:
            raise ValueError("MONGODB_URI environment variable is required")
        return True