"""Page Object untuk halaman Login Portal Internal BSN (employee/staff)."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Halaman login portal internal BSN (employee/staff)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/auth/users/login"

        # locator login form
        self.email = self.page.get_by_role("textbox", name="Email")
        self.password = self.page.get_by_role("textbox", name="Password")
        self.login_button = self.page.get_by_role("button", name="Masuk ke Akun BSN")

        # locator konfirmasi OTP
        self.otp_1 = self.page.get_by_role(
            "textbox", name="Please enter OTP character 1"
        )
        self.otp_2 = self.page.get_by_role(
            "textbox", name="Please enter OTP character 2"
        )
        self.otp_3 = self.page.get_by_role(
            "textbox", name="Please enter OTP character 3"
        )
        self.otp_4 = self.page.get_by_role(
            "textbox", name="Please enter OTP character 4"
        )
        self.otp_5 = self.page.get_by_role(
            "textbox", name="Please enter OTP character 5"
        )
        self.otp_6 = self.page.get_by_role(
            "textbox", name="Please enter OTP character 6"
        )
        self.lanjutkan_btn = self.page.get_by_role("button", name="Lanjutkan")
        self.kirim_ulang_kode_btn = self.page.get_by_role(
            "button", name="Kirim ulang kode"
        )

    def login(self, email: str, password: str):
        """Isi form login dan submit."""
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()

    def fill_otp(self, otp: str):
        """Isi form OTP dan submit."""
        if len(otp) != 6:
            raise ValueError("OTP harus 6 digit")
        self.otp_1.fill(otp[0])
        self.otp_2.fill(otp[1])
        self.otp_3.fill(otp[2])
        self.otp_4.fill(otp[3])
        self.otp_5.fill(otp[4])
        self.otp_6.fill(otp[5])
        self.lanjutkan_btn.click()

    def click_other_account(self):
        """Klik button Masuk dengan akun lain."""
        pass

    def click_home_button(self):
        """Klik button Halaman Utama."""
        pass
