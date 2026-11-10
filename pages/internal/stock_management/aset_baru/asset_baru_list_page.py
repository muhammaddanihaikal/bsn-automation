from playwright.sync_api import Page

from pages.base_page import BasePage


class AssetBaruListPage(BasePage):
    """Halaman Daftar Aset Baru — Portal Internal BSN."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/stock-management/aset-baru"

        self.input_aset_baru_btn = self.page.get_by_role(
            "button", name="Input Aset Baru"
        )
        self.search_input = self.page.get_by_role(
            "textbox", name="Cari nama aset, kode aset, atau lokasi"
        )

    def click_input_aset_baru(self):
        """Klik tombol '+ Input Aset Baru' untuk membuka form wizard."""
        self.input_aset_baru_btn.click()

    def search_aset(self, keyword: str):
        """Mencari aset berdasarkan nama, kode, atau lokasi."""
        # TODO: Dani implementasikan aksi ketik dan enter pencarian
        pass
