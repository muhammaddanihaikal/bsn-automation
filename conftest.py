import os

import pytest
from playwright.sync_api import Browser, Page, Playwright

from config import (
    BASE_URL_INTERNAL,
    HEADLESS,
    INTERNAL_SUPERADMIN_EMAIL,
    INTERNAL_SUPERADMIN_PASSWORD,
)
from helpers.mailpit import get_otp
from pages.internal.login_page import LoginPage

# Konfigurasi konstanta & environment guard
AUTH_FILE = ".auth/internal_state.json"
DASHBOARD_URL = f"{BASE_URL_INTERNAL}/internal/dashboard"
SAFE_DOMAINS = ["sandbox.zegen.app", "localhost", "127.0.0.1"]


# =========================================================================
# 1. BROWSER & ENVIRONMENT SETTINGS
# =========================================================================


@pytest.fixture(scope="session", autouse=True)
def guard_environment(base_url: str):
    """Mencegah script berjalan di luar domain sandbox/localhost."""
    assert any(domain in base_url for domain in SAFE_DOMAINS), (
        f"URL tidak aman: {base_url}"
    )


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Mengatur mode headless browser Playwright sesuai file .env."""
    return {**browser_type_launch_args, "headless": HEADLESS}


# =========================================================================
# 2. AUTHENTICATION FIXTURES (SESSION REUSE)
# =========================================================================


@pytest.fixture(scope="session")
def global_login_internal(playwright: Playwright):
    """Login UI sekali di awal sesi dan simpan session state ke json."""
    os.makedirs(".auth", exist_ok=True)
    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context()
    page = context.new_page()

    # 1. Buka portal & isi form login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(INTERNAL_SUPERADMIN_EMAIL, INTERNAL_SUPERADMIN_PASSWORD)

    # 2. Ambil OTP Mailpit & submit form OTP
    otp = get_otp(INTERNAL_SUPERADMIN_EMAIL)
    login_page.fill_otp(otp)

    # 3. Tunggu mendarat di dashboard & simpan session
    page.wait_for_url(f"{DASHBOARD_URL}*", timeout=15000)
    context.storage_state(path=AUTH_FILE)
    browser.close()


@pytest.fixture
def logged_in_internal(browser: Browser, global_login_internal) -> Page:
    """Menyediakan halaman browser yang sudah dalam kondisi login."""
    context = browser.new_context(storage_state=AUTH_FILE)
    page = context.new_page()
    page.goto(DASHBOARD_URL)
    yield page
    context.close()
