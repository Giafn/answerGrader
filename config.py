import os

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    API_SECRET_KEY = os.getenv("API_SECRET_KEY")
