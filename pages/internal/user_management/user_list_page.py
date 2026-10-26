from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class UserListPage(BasePage):
    """Halaman daftar pengguna (User List & Filter) — Portal Internal BSN."""

    def __init__(self, page: Page):
        super().__init__(page)
        # TODO: Dani tentukan PATH spesifik setelah reconnaisance
        self.PATH = "/internal/users"

        # === 1. FILTER SECTION ===
        # TODO: Dani isi locator input filter (misal: filter nama, filter role, filter status)
        self.name_filter = page.get_by_placeholder("Cari nama...")
        self.role_filter = page.get_by_role("combobox", name="Role")
        self.status_filter = page.get_by_role("combobox", name="Status")
        self.search_btn = page.get_by_role("button", name="Cari")
        self.reset_btn = page.get_by_role("button", name="Reset")

        # === 2. TABEL SECTION ===
        # TODO: Dani sesuaikan locator tabel & baris data
        self.user_table = page.get_by_role("table")
        self.table_rows = self.user_table.locator("tbody tr")
        self.add_user_btn = page.get_by_role("button", name="Tambah Pengguna")
        self.confirm_delete_btn = page.get_by_role("button", name="Ya, Hapus")

    # =========================================================================
    # ACTION METHODS: FILTER & SEARCH
    # =========================================================================

    def filter_by_name(self, name: str):
        """Mengisi input pencarian/filter berdasarkan nama pengguna."""
        # TODO: Dani isi implementasi aksi
        pass

    def filter_by_role(self, role: str):
        """Memilih opsi filter berdasarkan role."""
        # TODO: Dani isi implementasi aksi
        pass

    def filter_by_status(self, status: str):
        """Memilih opsi filter berdasarkan status (Aktif/Nonaktif)."""
        # TODO: Dani isi implementasi aksi
        pass

    def search(self):
        """Menekan tombol Cari (gunakan expect_response jika ada network request)."""
        # TODO: Dani aktifkan network wait & klik tombol
        # with self.page.expect_response("**/api/**"):
        #     self.search_btn.click()
        pass

    def reset_filter(self):
        """Menekan tombol Reset filter."""
        # TODO: Dani isi implementasi aksi
        pass

    # =========================================================================
    # ACTION METHODS: TABEL & MANAJEMEN USER
    # =========================================================================

    def get_user_row(self, identifier: str) -> Locator:
        """Mencari baris pengguna spesifik di tabel berdasarkan nama/email."""
        return self.user_table.get_by_role("row").filter(has_text=identifier)

    def click_add_user(self):
        """Mengeklik tombol Tambah Pengguna untuk membuka halaman form baru."""
        # TODO: Dani isi implementasi aksi
        pass

    def click_edit_user(self, identifier: str):
        """Mengeklik tombol edit pada baris pengguna yang dipilih."""
        # TODO: Dani isi implementasi aksi
        pass

    def delete_user(self, identifier: str):
        """Mengeklik tombol hapus dan konfirmasi dialog hapus."""
        # TODO: Dani isi implementasi aksi
        pass
