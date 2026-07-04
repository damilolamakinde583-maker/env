"""Configuration management for the bot."""
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required!")

# API Keys (optional)
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BITLY_API_KEY = os.getenv("BITLY_API_KEY")

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=getattr(logging, LOG_LEVEL, logging.INFO)
)

# Service URLs
DEFAULT_SHORTENER = "https://is.gd/create.php"
FALLBACK_SHORTENER = "https://v.gd/create.php"

# Bot settings
MAX_IMAGE_PROMPT_LENGTH = 200
DEFAULT_IMAGE_SIZE = "512x512"
