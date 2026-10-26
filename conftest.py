import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, Browser, Page

from config import BASE_URL_INTERNAL
from helpers.mailpit import get_otp
from api.internal_user_api import InternalUserAPI
from pages.internal.login_page import LoginPage

load_dotenv()

# Domain aman untuk pengujian (sandbox & local only)
SAFE_DOMAINS = ["sandbox.zegen.app", "localhost", "127.0.0.1"]

LOGIN_URL = f"{BASE_URL_INTERNAL}/auth/users/login"
INTERNAL_DASH_URL = f"{BASE_URL_INTERNAL}/internal"
AUTO_EMAIL_INTERNAL = os.getenv("INTERNAL_SUPERADMIN_EMAIL") or os.getenv("AUTO_EMAIL_INTERNAL", "")
AUTO_PASSWORD_INTERNAL = os.getenv("INTERNAL_SUPERADMIN_PASSWORD") or os.getenv("AUTO_PASSWORD_INTERNAL", "")


@pytest.fixture(scope="session", autouse=True)
def guard_environment(base_url: str):
    """Mencegah test berjalan di luar domain sandbox/localhost."""
    assert any(domain in base_url for domain in SAFE_DOMAINS), f"URL tidak aman: {base_url}"


@pytest.fixture(scope="session")
def global_login_internal(playwright: Playwright):
    """Login UI 1x di awal dan simpan session cookies ke file json."""
    os.makedirs(".auth", exist_ok=True)
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # 1. Isi form login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(AUTO_EMAIL_INTERNAL, AUTO_PASSWORD_INTERNAL)

    # 2. Tunggu form OTP muncul
    page.wait_for_selector("input[placeholder*='kode'], input[placeholder*='OTP']")

    # 3. Ambil kode OTP dari Mailpit
    otp = get_otp(AUTO_EMAIL_INTERNAL)

    # 4. Ketik OTP dan verifikasi
    page.get_by_placeholder("kode").fill(otp)
    page.get_by_role("button", name="Verifikasi").click()

    # 5. Tunggu redirect ke dashboard
    page.wait_for_url(f"{INTERNAL_DASH_URL}/**", timeout=15000)

    # 6. Simpan cookies login
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
