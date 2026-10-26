from playwright.sync_api import Page
from config import BASE_URL_INTERNAL


class BasePage:
    """Induk class untuk semua Page Object."""

    def __init__(self, page: Page):
        self.page = page
        self.PATH = ""

    def open(self, base_url: str = BASE_URL_INTERNAL):
        """Buka halaman berdasarkan rute PATH."""
        self.page.goto(f"{base_url}{self.PATH}")
