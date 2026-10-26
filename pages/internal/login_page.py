"""Page Object untuk halaman Login Portal Internal BSN (employee/staff)."""
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Halaman login portal internal BSN (employee/staff)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/auth/users/login"

        # === 1. LOCATOR FORM LOGIN ===
        # TODO: Dani isi locator email, kata sandi, dan tombol masuk di sini

        # === 2. LOCATOR KONFIRMASI IDENTITAS & SESI BERAKHIR ===
        # TODO: Dani isi locator tombol akun lain & halaman utama di sini

    # =========================================================================
    # ACTION METHODS
    # =========================================================================

    def login(self, email: str, password: str):
        """Isi form login dan submit."""
        pass

    def click_other_account(self):
        """Klik button Masuk dengan akun lain."""
        pass

    def click_home_button(self):
        """Klik button Halaman Utama."""
        pass
