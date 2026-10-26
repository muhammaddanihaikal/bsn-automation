from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class UserListPage(BasePage):
    """Halaman daftar pengguna (User List & Filter) — Portal Internal BSN."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/users"  # TODO: Dani sesuaikan rute URL jika berbeda

        # === 1. FILTER SECTION ===
        # TODO: Dani isi locator field filter & tombol cari / reset di sini

        # === 2. TABEL SECTION ===
        # TODO: Dani isi locator tabel, baris data, tombol tambah, dan tombol konfirmasi di sini

    # =========================================================================
    # ACTION METHODS: FILTER & SEARCH
    # =========================================================================

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

    # =========================================================================
    # ACTION METHODS: TABEL & MANAJEMEN USER
    # =========================================================================

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
