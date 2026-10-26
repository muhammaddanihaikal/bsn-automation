from playwright.sync_api import Page
from pages.base_page import BasePage


class EditUserPage(BasePage):
    """Halaman Form Edit Pengguna — Portal Internal BSN (Halaman Baru)."""

    def __init__(self, page: Page):
        super().__init__(page)
        # Path dinamis bergantung pada user_id (misal: /internal/users/123/edit)
        self.PATH = "/internal/users/edit"

        # === 1. LOCATOR FIELD INPUT FORM EDIT ===
        # TODO: Dani isi locator input edit
        self.full_name_input = page.get_by_label("Nama Lengkap")
        self.role_select = page.get_by_role("combobox", name="Role")
        self.status_toggle = page.get_by_role("checkbox", name="Status Aktif")

        # === 2. TOMBOL AKSI ===
        self.save_btn = page.get_by_role("button", name="Perbarui")
        self.cancel_btn = page.get_by_role("button", name="Batal")

    def update_form(self, data: dict):
        """Mengubah data form pengguna yang sedang diedit."""
        # TODO: Dani isi alur pengubahan data
        pass

    def save(self):
        """Mengeklik tombol Simpan/Perbarui."""
        # TODO: Dani aktifkan aksi klik simpan
        # self.save_btn.click()
        pass

    def edit_user(self, data: dict):
        """Alur lengkap: mengubah data dan submit perbarui."""
        self.update_form(data)
        self.save()
