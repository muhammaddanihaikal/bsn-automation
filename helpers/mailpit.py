import re
import time
from datetime import datetime, timezone

import requests

from config import MAILPIT_AUTH, MAILPIT_URL


def _search_latest_email(email: str, subject: str) -> dict | None:
    # Cari 1 email teratas dari API Mailpit
    params = {"query": f"to:{email} subject:{subject}", "limit": 1}
    res = requests.get(
        f"{MAILPIT_URL}/api/v1/search", params=params, auth=MAILPIT_AUTH
    ).json()
    messages = res.get("messages", [])
    return messages[0] if messages else None


def _is_fresh_email(message: dict, max_age: int = 60) -> bool:
    # Periksa apakah email berumur kurang dari 60 detik
    waktu_email = datetime.fromisoformat(message["Created"])
    umur_detik = (datetime.now(timezone.utc) - waktu_email).total_seconds()
    return umur_detik <= max_age


def _extract_otp_from_html(message_id: str) -> str | None:
    # Buka pesan dan ekstrak 6 digit angka OTP
    detail = requests.get(
        f"{MAILPIT_URL}/api/v1/message/{message_id}", auth=MAILPIT_AUTH
    ).json()
    match = re.search(r"\b(\d{6})\b", detail.get("HTML", ""))
    return match.group(1) if match else None


def get_otp(email: str, subject: str = "Kode Masuk", timeout: int = 30) -> str:
    """Tunggu email baru mendarat di Mailpit lalu ambil 6 digit OTP."""
    start_time = time.time()

    # Looping tunggu email baru (maksimal 30 detik)
    while time.time() - start_time < timeout:
        # 1. Cari email terbaru
        message = _search_latest_email(email, subject)

        # 2. Cek apakah email baru mendarat (< 60 detik)
        if message and _is_fresh_email(message):
            # 3. Ambil 6 digit OTP
            otp = _extract_otp_from_html(message["ID"])
            if otp:
                return otp

        # 4. Tunggu 1 detik sebelum cek ulang
        time.sleep(1)

    # 5. Lempar error jika waktu habis
    raise TimeoutError(
        f"Email OTP baru belum masuk ke Mailpit setelah {timeout} detik"
    )
