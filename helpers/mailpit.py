import re
import requests
from config import MAILPIT_URL, MAILPIT_AUTH


def get_otp(email: str, subject: str = "Kode Masuk") -> str:
    """Mengambil 6 digit kode OTP terbaru dari Mailpit."""
    # 1. Cari pesan email terbaru
    params = {"query": f"to:{email} subject:{subject}", "limit": 1}
    response = requests.get(f"{MAILPIT_URL}/api/v1/search", params=params, auth=MAILPIT_AUTH).json()
    messages = response.get("messages", [])
    if not messages:
        raise ValueError(f"Email OTP tidak ditemukan untuk {email}")

    # 2. Ambil isi HTML email
    message_id = messages[0]["ID"]
    detail = requests.get(f"{MAILPIT_URL}/api/v1/message/{message_id}", auth=MAILPIT_AUTH).json()

    # 3. Ekstrak 6 angka OTP
    match = re.search(r"\b(\d{6})\b", detail.get("HTML", ""))
    if not match:
        raise ValueError("Kode OTP 6 digit tidak ditemukan di email")

    return match.group(1)
