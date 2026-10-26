from playwright.sync_api import Page
from pages.base_page import BasePage


class AddUserPage(BasePage):
    """Halaman Form Tambah Pengguna Baru — Portal Internal BSN (Halaman Baru)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/users/create"

        # 1. Locator input form
        # TODO: Dani isi locator input form di sini

        # 2. Tombol aksi
        # TODO: Dani isi locator tombol Simpan / Batal di sini

        # 3. Pesan validasi error
        # TODO: Dani isi locator pesan error saat mandatory kosong

    def fill_form(self, data: dict):
        """Mengisi seluruh field form tambah pengguna."""
        pass

    def save(self):
        """Mengeklik tombol Simpan."""
        pass

    def add_user(self, data: dict):
        """Alur lengkap: mengisi form dan submit simpan data."""
        pass
