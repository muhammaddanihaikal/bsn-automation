import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

# Konfigurasi Mailpit
MAILPIT_URL = os.getenv("MAILPIT_URL", "https://mailpit.zegen.app")
MAILPIT_USER = os.getenv("MAILPIT_USER", "admin")
MAILPIT_PASS = os.getenv("MAILPIT_PASS", "P@ssw0rd")


def get_otp(email: str, subject: str = "Kode Masuk") -> str:
    """Mengambil 6 digit kode OTP terbaru dari Mailpit."""
    auth = (MAILPIT_USER, MAILPIT_PASS)

    # 1. Cari pesan email terbaru
    params = {"query": f"to:{email} subject:{subject}", "limit": 1}
    response = requests.get(f"{MAILPIT_URL}/api/v1/search", params=params, auth=auth).json()
    messages = response.get("messages", [])
    if not messages:
        raise ValueError(f"Email OTP tidak ditemukan untuk {email}")

    # 2. Ambil isi HTML email
    message_id = messages[0]["ID"]
    detail = requests.get(f"{MAILPIT_URL}/api/v1/message/{message_id}", auth=auth).json()

    # 3. Ekstrak 6 angka OTP
    match = re.search(r"\b(\d{6})\b", detail.get("HTML", ""))
    if not match:
        raise ValueError("Kode OTP 6 digit tidak ditemukan di email")

    return match.group(1)
