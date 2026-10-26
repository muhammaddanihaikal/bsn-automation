"""
Root conftest — shared configuration & safety guardrails.
Login fixtures ada di tests/internal/conftest.py dan tests/external/conftest.py
"""
import pytest

# Daftar domain yang aman untuk dites (sandbox & local only)
SAFE_DOMAINS = ["sandbox.zegen.app", "localhost", "127.0.0.1"]


@pytest.fixture(scope="session", autouse=True)
def guard_environment(base_url: str):
    """
    🛡️ SAFETY GUARDRAIL — Environment Lock.
    Mencegah AI atau tester salah menembak environment staging lain / production.
    Jika target URL tidak mengandung domain aman, pytest otomatis menolak berjalan.
    """
    assert any(domain in base_url for domain in SAFE_DOMAINS), (
        f"\n\n🚨 KEAMANAN TERPICU!\n"
        f"Target URL '{base_url}' bukan sandbox atau localhost!\n"
        f"Pengujian otomatis DIHENTIKAN untuk mencegah kerusakan data.\n"
        f"Domain yang diizinkan: {SAFE_DOMAINS}\n"
    )
