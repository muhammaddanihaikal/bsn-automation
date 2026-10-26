import os

from dotenv import load_dotenv

# Muat file .env sekali untuk seluruh project
load_dotenv()

# URL & Browser
BASE_URL_INTERNAL = os.getenv("INTERNAL_URL", "https://terasrumah-sandbox.zegen.app")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

# Kredensial Superadmin Internal
INTERNAL_SUPERADMIN_EMAIL = os.getenv("INTERNAL_SUPERADMIN_EMAIL", "")
INTERNAL_SUPERADMIN_PASSWORD = os.getenv("INTERNAL_SUPERADMIN_PASSWORD", "")

# Mailpit (Email OTP)
MAILPIT_URL = os.getenv("MAILPIT_URL", "https://mailpit.zegen.app")
MAILPIT_USER = os.getenv("MAILPIT_USER", "admin")
MAILPIT_PASS = os.getenv("MAILPIT_PASS", "P@ssw0rd")
MAILPIT_AUTH = (MAILPIT_USER, MAILPIT_PASS)
