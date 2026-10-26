from playwright.sync_api import Page
from pages.base_page import BasePage


class AddUserPage(BasePage):
    """Halaman Form Tambah Pengguna Baru — Portal Internal BSN (Halaman Baru)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/users/create"  # TODO: Dani sesuaikan rute URL jika berbeda

        # === 1. LOCATOR FIELD INPUT FORM ===
        # TODO: Dani isi locator input form di sini

        # === 2. TOMBOL AKSI ===
        # TODO: Dani isi locator tombol Simpan / Batal di sini

        # === 3. LOCATOR VALIDASI / ERROR MESSAGE MANDATORY ===
        # TODO: Dani isi locator pesan error saat field mandatory dikosongkan

    def fill_form(self, data: dict):
        """Mengisi seluruh field form tambah pengguna."""
        pass

    def save(self):
        """Mengeklik tombol Simpan."""
        pass

    def add_user(self, data: dict):
        """Alur lengkap: mengisi form dan submit simpan data."""
        pass
