# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables de entorno desde .env

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
