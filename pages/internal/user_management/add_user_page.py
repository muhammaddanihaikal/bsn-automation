from playwright.sync_api import Page
from pages.base_page import BasePage


class AddUserPage(BasePage):
    """Halaman Form Tambah Pengguna Baru — Portal Internal BSN (Halaman Baru)."""

    def __init__(self, page: Page):
        super().__init__(page)
        # TODO: Dani tentukan PATH form tambah user setelah reconnaisance
        self.PATH = "/internal/users/create"

        # === 1. LOCATOR FIELD INPUT FORM ===
        # TODO: Dani isi locator input form sesuai atribut di browser
        self.full_name_input = page.get_by_label("Nama Lengkap")
        self.email_input = page.get_by_label("Email")
        self.role_select = page.get_by_role("combobox", name="Role")
        self.password_input = page.get_by_label("Kata Sandi")
        self.confirm_password_input = page.get_by_label("Konfirmasi Kata Sandi")

        # === 2. TOMBOL AKSI ===
        self.save_btn = page.get_by_role("button", name="Simpan")
        self.cancel_btn = page.get_by_role("button", name="Batal")

        # === 3. LOCATOR VALIDASI / ERROR MESSAGE MANDATORY ===
        # TODO: Dani tentukan locator error saat field wajib dikosongkan
        self.error_name = page.get_by_text("Nama wajib diisi")
        self.error_email = page.get_by_text("Email wajib diisi")

    def fill_form(self, data: dict):
        """Mengisi seluruh field form tambah pengguna."""
        # TODO: Dani isi urutan pengetikan form
        pass

    def save(self):
        """Mengeklik tombol Simpan."""
        # TODO: Dani aktifkan aksi klik simpan
        # self.save_btn.click()
        pass

    def add_user(self, data: dict):
        """Alur lengkap: mengisi form dan submit simpan data."""
        self.fill_form(data)
        self.save()
