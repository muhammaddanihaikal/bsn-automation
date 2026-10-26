"""Fixtures login khusus portal Internal BSN (employee/staff)."""
import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, Browser, Page

from config import BASE_URL_INTERNAL
from helpers.mailpit import get_otp
from api.internal_user_api import InternalUserAPI
from utils.data_factory import generate_full_name, generate_username

load_dotenv()

LOGIN_URL           = f"{BASE_URL_INTERNAL}/auth/users/login"
INTERNAL_DASH_URL   = f"{BASE_URL_INTERNAL}/internal"
AUTO_EMAIL_INTERNAL = os.getenv("AUTO_EMAIL_INTERNAL", "")


@pytest.fixture(scope="session")
def global_login_internal(playwright: Playwright):
    """
    Jalan 1x saja per pytest run.
    Login ke portal Internal BSN + handle MFA via Mailpit.
    Hasil: session tersimpan di .auth/internal_state.json
    """
    os.makedirs(".auth", exist_ok=True)
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page    = context.new_page()

    # ── 1. Isi form login ──────────────────────────────────────────────
    page.goto(LOGIN_URL)
    page.get_by_placeholder("Email").fill(AUTO_EMAIL_INTERNAL)
    page.get_by_placeholder("Kata Sandi").fill(os.getenv("AUTO_PASSWORD_INTERNAL", ""))
    page.get_by_role("button", name="Masuk").click()

    # ── 2. Tunggu form OTP muncul ──────────────────────────────────────
    # ⚠️ Sesuaikan selector setelah reconnaisance UI (Phase 0b)
    page.wait_for_selector("input[placeholder*='kode'], input[placeholder*='OTP']")

    # ── 3. Ambil OTP dari Mailpit ──────────────────────────────────────
    otp = get_otp(AUTO_EMAIL_INTERNAL)

    # ── 4. Inject OTP ke form & submit ────────────────────────────────
    # ⚠️ Sesuaikan placeholder & nama button setelah reconnaisance
    page.get_by_placeholder("kode").fill(otp)
    page.get_by_role("button", name="Verifikasi").click()

    # ── 5. Tunggu masuk dashboard ──────────────────────────────────────
    page.wait_for_url(f"{INTERNAL_DASH_URL}/**", timeout=15000)

    # ── 6. Simpan session (cookies + localStorage) ─────────────────────
    context.storage_state(path=".auth/internal_state.json")
    browser.close()


@pytest.fixture
def logged_in_internal(browser: Browser, global_login_internal) -> Page:
    """Per-test: page internal yang sudah login. Tidak perlu login ulang."""
    context = browser.new_context(storage_state=".auth/internal_state.json")
    page    = context.new_page()
    page.goto(INTERNAL_DASH_URL)
    yield page
    context.close()


@pytest.fixture
def api_create_user(logged_in_internal: Page) -> dict:
    """
    Fixture Seeding Data Tumbal:
    1. Setup: Membuat data user tumbal via REST API sebelum test dimulai.
    2. Yield: Meminjamkan payload data ke fungsi test.
    3. Teardown: Menghapus data user tumbal via REST API setelah test selesai.
    """
    user_api = InternalUserAPI(logged_in_internal, BASE_URL_INTERNAL)
    tumbal_name = generate_full_name("Pengguna")
    tumbal_username = generate_username("tumbal")

    # TODO: Dani lengkapi payload dan aktifkan saat API BSN sudah diketahui
    # created_user = user_api.create_tumbal_user({
    #     "name": tumbal_name,
    #     "username": tumbal_username,
    # })

    mock_user_data = {
        "id": "mock_tumbal_id_123",
        "name": tumbal_name,
        "username": tumbal_username,
    }

    yield mock_user_data

    # Teardown: pembersihan data uji
    # user_api.delete_tumbal_user(mock_user_data["id"])
