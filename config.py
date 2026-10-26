import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL_INTERNAL = os.getenv("INTERNAL_URL", "https://terasrumah-sandbox.zegen.app")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
