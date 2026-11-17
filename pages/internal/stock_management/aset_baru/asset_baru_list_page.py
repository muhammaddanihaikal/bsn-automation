from playwright.sync_api import Page

from pages.base_page import BasePage


class AssetBaruListPage(BasePage):
    """Halaman Daftar Aset Baru — Portal Internal BSN."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/stock-management/aset-baru"

        # === 1. TOMBOL AKSI ATAS & FILTER ===
        self.input_aset_baru_btn = self.page.get_by_role(
            "button", name="Input Aset Baru"
        )
        self.search_input = self.page.get_by_role(
            "textbox", name="Cari nama aset, kode aset, atau lokasi"
        )
        self.reset_filter_btn = self.page.get_by_test_id(
            "aset-baru-filter-reset-button"
        )

        # === 2. TAB STATUS ASET ===
        self.tab_all_btn = self.page.get_by_test_id("aset-baru-tab-all")
        self.tab_published_btn = self.page.get_by_test_id("aset-baru-tab-published")
        self.tab_draft_btn = self.page.get_by_test_id("aset-baru-tab-draft")
        self.tab_curation_btn = self.page.get_by_test_id("aset-baru-tab-curation")

        # === 3. TABEL DATA ASET ===
        # Pakai tr.ant-table-row karena AntD punya hidden .ant-table-measure-row di baris 0
        self.table_rows = self.page.locator("tr.ant-table-row")

    def click_input_aset_baru(self):
        """Klik tombol '+ Input Aset Baru' untuk membuka form wizard."""
        self.input_aset_baru_btn.click()

    def click_edit_aset(self, keyword: str):
        """Klik tombol Edit langsung di baris tabel aset yang sesuai kata kunci."""
        # Pakai $= karena tiap baris punya ID aset unik di tengah data-testid
        target_row = self.table_rows.filter(has_text=keyword).first
        edit_btn = target_row.locator("[data-testid$='-edit-button']")
        edit_btn.scroll_into_view_if_needed()
        edit_btn.click()

    def search_aset(self, keyword: str):
        """Mencari aset berdasarkan nama, kode, atau lokasi."""
        # TODO: Dani implementasikan aksi ketik dan enter pencarian
        pass
