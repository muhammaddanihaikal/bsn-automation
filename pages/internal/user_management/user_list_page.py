from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class UserListPage(BasePage):
    """Halaman daftar pengguna (User List & Filter) — Portal Internal BSN."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/users"

        # 1. Filter section
        # TODO: Dani isi locator filter di sini

        # 2. Tabel section
        # TODO: Dani isi locator tabel di sini

    # Filter methods
    def filter_by_name(self, name: str):
        """Mengisi input pencarian/filter berdasarkan nama pengguna."""
        pass

    def filter_by_role(self, role: str):
        """Memilih opsi filter berdasarkan role."""
        pass

    def filter_by_status(self, status: str):
        """Memilih opsi filter berdasarkan status (Aktif/Nonaktif)."""
        pass

    def search(self):
        """Menekan tombol Cari dan menunggu response API pencarian selesai."""
        pass

    def reset_filter(self):
        """Menekan tombol Reset filter."""
        pass

    # Tabel methods
    def get_user_row(self, identifier: str) -> Locator:
        """Mencari baris pengguna spesifik di tabel berdasarkan nama/email."""
        pass

    def click_add_user(self):
        """Mengeklik tombol Tambah Pengguna untuk membuka halaman form baru."""
        pass

    def click_edit_user(self, identifier: str):
        """Mengeklik tombol edit pada baris pengguna yang dipilih."""
        pass

    def delete_user(self, identifier: str):
        """Mengeklik tombol hapus dan konfirmasi dialog hapus."""
        pass
