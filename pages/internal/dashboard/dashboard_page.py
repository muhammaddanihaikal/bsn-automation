"""Page Object untuk halaman Dashboard Portal Internal BSN."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Halaman Dashboard Portal Internal BSN."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/dashboard"

        # Locator elemen dashboard
        self.heading = self.page.get_by_role("heading", name="Dashboard")
