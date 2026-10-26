"""Fixtures login khusus portal Internal BSN (employee/staff)."""
import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, Browser, Page
from helpers.mailpit import get_otp

load_dotenv()

LOGIN_URL           = "https://terasrumah-sandbox.zegen.app/auth/users/login"
INTERNAL_DASH_URL   = "https://terasrumah-sandbox.zegen.app/internal"
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
