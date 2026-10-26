"""Page Object untuk halaman Login Portal Internal BSN (employee/staff)."""
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Halaman login portal internal BSN (employee/staff)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/auth/users/login"

        # ⚠️ Semua selector dikonfirmasi setelah reconnaisance UI (Phase 0b)
        self.email_input       = page.get_by_placeholder("Email")
        self.password_input    = page.get_by_placeholder("Kata Sandi")
        self.login_btn         = page.get_by_role("button", name="Masuk")

        # Halaman Konfirmasi Identitas (setelah submit email+password)
        self.other_account_btn = page.get_by_role("button", name="Masuk dengan akun lain")

        # Halaman auto-logout / session expired
        self.home_btn          = page.get_by_role("button", name="Halaman Utama")

    def login(self, email: str, password: str):
        """Isi form login dan submit."""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_btn.click()

    def click_other_account(self):
        """Klik button 'Masuk dengan akun lain' di halaman Konfirmasi Identitas."""
        self.other_account_btn.click()

    def click_home_button(self):
        """Klik button 'Halaman Utama' di halaman session expired / auto-logout."""
        self.home_btn.click()
