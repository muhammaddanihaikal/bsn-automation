"""Helper untuk mengambil OTP dari Mailpit (shared antara internal & external)."""
import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

MAILPIT_URL  = os.getenv("MAILPIT_URL", "https://mailpit.zegen.app")
MAILPIT_AUTH = (
    os.getenv("MAILPIT_USER", "admin"),
    os.getenv("MAILPIT_PASS", "")
)


def get_otp(recipient_email: str, subject: str = "Kode Masuk") -> str:
    """
    Ambil kode OTP 6 digit terbaru dari Mailpit untuk email dan subject tertentu.
    Dipanggil SETELAH form OTP muncul di browser (memastikan email sudah ada di Mailpit).

    Args:
        recipient_email: Email penerima OTP (akun automation).
        subject: Subject email OTP (default: 'Kode Masuk').

    Returns:
        String 6 digit OTP (contoh: '680169').
    """
    resp = requests.get(
        f"{MAILPIT_URL}/api/v1/search",
        params={
            "query": f"to:{recipient_email} subject:{subject}",
            "limit": 1
        },
        auth=MAILPIT_AUTH
    )
    resp.raise_for_status()
    messages = resp.json().get("messages", [])
    assert messages, (
        f"❌ Email OTP tidak ditemukan di Mailpit untuk: {recipient_email}\n"
        f"Pastikan form OTP sudah muncul di browser sebelum memanggil fungsi ini."
    )

    # Ambil detail email
    detail = requests.get(
        f"{MAILPIT_URL}/api/v1/message/{messages[0]['ID']}",
        auth=MAILPIT_AUTH
    ).json()

    # Extract OTP dari HTML body (6 digit angka)
    html_body = detail.get("HTML", "")
    match = re.search(r'\b(\d{6})\b', html_body)
    assert match, (
        f"❌ OTP 6 digit tidak ditemukan di body email!\n"
        f"Body: {html_body[:200]}..."
    )
    return match.group(1)
