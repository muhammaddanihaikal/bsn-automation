from playwright.sync_api import Page


class Sidebar:
    """Komponen Sidebar navigasi menu utama Portal Internal BSN."""

    def __init__(self, page: Page):
        self.page = page

        self.stock_management_menu = self.page.get_by_test_id(
            "sidebar-submenu-stock-management"
        )
        self.aset_baru_submenu = self.page.get_by_test_id(
            "sidebar-menu-stock-management-aset-baru"
        )

    def go_to_aset_baru(self):
        """Navigasi ke menu Stock Management -> Aset Baru."""
        self.stock_management_menu.click()
        self.aset_baru_submenu.click()
