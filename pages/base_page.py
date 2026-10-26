from playwright.sync_api import Page, Locator
from config import BASE_URL_INTERNAL


class BasePage:
    """Kelas induk (parent) untuk semua Page Object di portal BSN."""

    def __init__(self, page: Page):
        self.page = page
        self.PATH = ""

    def open(self, base_url: str = BASE_URL_INTERNAL):
        """Membuka halaman berdasarkan BASE_URL + PATH."""
        self.page.goto(f"{base_url}{self.PATH}")

    def wait_for_url(self, base_url: str = BASE_URL_INTERNAL, timeout: float = 10000):
        """Menunggu URL browser sesuai dengan PATH halaman ini."""
        self.page.wait_for_url(f"{base_url}{self.PATH}**", timeout=timeout)

    def get_toast(self) -> Locator:
        """Mengambil locator alert / toast notifikasi global."""
        return self.page.get_by_role("alert")
