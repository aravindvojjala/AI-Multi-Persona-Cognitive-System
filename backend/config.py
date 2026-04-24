import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("CEREBRAS_API_KEY")