import os
import pytest
from playwright.sync_api import Playwright, Browser, Page

from config import (
    BASE_URL_INTERNAL,
    HEADLESS,
    INTERNAL_SUPERADMIN_EMAIL,
    INTERNAL_SUPERADMIN_PASSWORD,
)
from helpers.mailpit import get_otp
from api.internal_user_api import InternalUserAPI
from pages.internal.login_page import LoginPage

# Domain aman untuk pengujian
SAFE_DOMAINS = ["sandbox.zegen.app", "localhost", "127.0.0.1"]
INTERNAL_DASH_URL = f"{BASE_URL_INTERNAL}/internal/dashboard"


@pytest.fixture(scope="session", autouse=True)
def guard_environment(base_url: str):
    """Mencegah test berjalan di luar domain sandbox/localhost."""
    assert any(domain in base_url for domain in SAFE_DOMAINS), f"URL tidak aman: {base_url}"


@pytest.fixture(scope="session")
def global_login_internal(playwright: Playwright):
    """Login UI 1x di awal dan simpan session cookies ke file json."""
    os.makedirs(".auth", exist_ok=True)
    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context()
    page = context.new_page()

    # 1. Isi form login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(INTERNAL_SUPERADMIN_EMAIL, INTERNAL_SUPERADMIN_PASSWORD)

    # 2. Ambil kode OTP dari Mailpit & isi via LoginPage
    otp = get_otp(INTERNAL_SUPERADMIN_EMAIL)
    login_page.fill_otp(otp)

    # 3. Tunggu redirect ke dashboard
    page.wait_for_url(f"{INTERNAL_DASH_URL}/**", timeout=15000)

    # 4. Simpan cookies login
    context.storage_state(path=".auth/internal_state.json")
    browser.close()


@pytest.fixture
def logged_in_internal(browser: Browser, global_login_internal) -> Page:
    """Menyediakan halaman yang sudah login untuk test internal."""
    context = browser.new_context(storage_state=".auth/internal_state.json")
    page = context.new_page()
    page.goto(INTERNAL_DASH_URL)
    yield page
    context.close()


@pytest.fixture
def api_create_user(logged_in_internal: Page) -> dict:
    """Menyiapkan user tumbal via API (Setup & Teardown)."""
    user_api = InternalUserAPI(logged_in_internal, BASE_URL_INTERNAL)
    # TODO: Dani aktifkan API seeding saat endpoint BSN sudah diketahui
    mock_user = {"id": "tumbal_123", "name": "User Tumbal"}
    yield mock_user
