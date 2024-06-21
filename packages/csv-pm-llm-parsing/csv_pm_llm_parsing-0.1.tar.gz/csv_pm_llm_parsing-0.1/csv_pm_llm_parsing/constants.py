import os

SLEEP_TIME = 3
MAX_RETRY = 5
OPENAI_API_URL = os.environ.get("OPENAI_API_URL", "https://api.openai.com/v1")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", None)
