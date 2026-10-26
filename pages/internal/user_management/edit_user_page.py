from playwright.sync_api import Page
from pages.base_page import BasePage


class EditUserPage(BasePage):
    """Halaman Form Edit Pengguna — Portal Internal BSN (Halaman Baru)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/users/edit"  # TODO: Dani sesuaikan rute URL jika berbeda

        # === 1. LOCATOR FIELD INPUT FORM EDIT ===
        # TODO: Dani isi locator input form edit di sini

        # === 2. TOMBOL AKSI ===
        # TODO: Dani isi locator tombol Simpan / Perbarui / Batal di sini

    def update_form(self, data: dict):
        """Mengubah data form pengguna yang sedang diedit."""
        pass

    def save(self):
        """Mengeklik tombol Simpan/Perbarui."""
        pass

    def edit_user(self, data: dict):
        """Alur lengkap: mengubah data dan submit perbarui."""
        pass
