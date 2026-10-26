"""Page Object untuk halaman Login Portal Internal BSN (employee/staff)."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Halaman login portal internal BSN (employee/staff)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/auth/users/login"

        self.email = self.page.get_by_role("textbox", name="Email")
        self.password = self.page.get_by_role("textbox", name="Password")
        self.login_button = self.page.get_by_role("button", name="Masuk ke Akun BSN")

    def login(self, email: str, password: str):
        """Isi form login dan submit."""
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()

    def click_other_account(self):
        """Klik button Masuk dengan akun lain."""
        pass

    def click_home_button(self):
        """Klik button Halaman Utama."""
        pass
