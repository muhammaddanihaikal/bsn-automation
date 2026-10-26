"""
Test suite Authentication — Portal Internal BSN
TC-INT-AUTH-01 s/d TC-INT-AUTH-04
"""
import pytest
import allure
from playwright.sync_api import Page, expect

from config import BASE_URL_INTERNAL
from pages.internal.login_page import LoginPage

LOGIN_URL     = f"{BASE_URL_INTERNAL}/auth/users/login"
DASHBOARD_URL = f"{BASE_URL_INTERNAL}/internal"


class TestAuthInternal:

    @allure.title("[TC-INT-AUTH-01] Login valid berhasil masuk dashboard")
    @pytest.mark.smoke
    def test_login_valid(self, logged_in_internal: Page):
        """Verifikasi user berhasil login dan diarahkan ke dashboard internal."""
        # 1. Arrange & 2. Act: dihandle fixture logged_in_internal
        page = logged_in_internal

        # 3. Assert
        expect(page).to_have_url(f"{DASHBOARD_URL}/**")

    @allure.title("[TC-INT-AUTH-02] Logout redirect ke halaman Login")
    @pytest.mark.smoke
    def test_logout(self, logged_in_internal: Page):
        """[Bug Retest] Logout harus redirect ke Login, bukan halaman error."""
        # 1. Arrange
        page = logged_in_internal

        # 2. Act — ⚠️ Selector dropdown profil & tombol Keluar diisi setelah reconnaisance
        # page.get_by_role("button", name="...nama admin...").click()
        # page.get_by_role("menuitem", name="Keluar").click()

        # 3. Assert
        # expect(page).to_have_url(LOGIN_URL)
        pytest.skip("⚠️ Selector belum dikonfirmasi — tunggu reconnaisance UI (Phase 0b)")

    @allure.title("[TC-INT-AUTH-03] Button 'Masuk dengan akun lain' kembali ke form login")
    @pytest.mark.regression
    def test_other_account_btn(self, page: Page):
        """[Bug Retest] Button tidak berfungsi — seharusnya redirect ke form login awal."""
        pytest.skip("⚠️ Selector belum dikonfirmasi — tunggu reconnaisance UI (Phase 0b)")

    @allure.title("[TC-INT-AUTH-04] Button 'Halaman Utama' di auto-logout redirect ke Login internal")
    @pytest.mark.regression
    def test_home_btn_redirect(self, page: Page):
        """[Bug Retest] Redirect ke 404 — seharusnya ke halaman Login internal."""
        pytest.skip("⚠️ Selector belum dikonfirmasi — tunggu reconnaisance UI (Phase 0b)")
