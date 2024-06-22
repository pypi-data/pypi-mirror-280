from dotenv import load_dotenv
import os

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_ENDPOINT = os.getenv("API_ENDPOINT")

if BEARER_TOKEN is None:
    raise ValueError("BEARER_TOKEN is not set in the environment variables.")
if API_ENDPOINT is None:
    raise ValueError("API_ENDPOINT is not set in the environment variables.")
