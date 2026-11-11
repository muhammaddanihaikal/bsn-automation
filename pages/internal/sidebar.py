from playwright.sync_api import Page


class Sidebar:
    """Komponen Sidebar navigasi menu utama Portal Internal BSN."""

    def __init__(self, page: Page):
        self.page = page

        # === 1. LOCATOR MENU UTAMA SIDEBAR ===
        self.dashboard_menu = self.page.get_by_test_id("sidebar-menu-dashboard")
        self.customer_management_menu = self.page.get_by_test_id(
            "sidebar-menu-customer-management"
        )
        self.stock_management_menu = self.page.get_by_test_id(
            "sidebar-submenu-stock-management"
        )
        self.developer_menu = self.page.get_by_test_id("sidebar-menu-developer")
        self.user_management_menu = self.page.get_by_test_id(
            "sidebar-menu-user-management"
        )

        # === 2. LOCATOR SUB-MENU STOCK MANAGEMENT ===
        self.aset_baru_submenu = self.page.get_by_test_id(
            "sidebar-menu-stock-management-aset-baru"
        )
        self.aset_lelang_submenu = self.page.get_by_test_id(
            "sidebar-menu-stock-management-aset-lelang"
        )

    # =========================================================================
    # NAVIGATION METHODS
    # =========================================================================

    def go_to_dashboard(self):
        """Navigasi ke menu Dashboard."""
        self.dashboard_menu.click()

    def go_to_aset_baru(self):
        """Navigasi ke menu Stock Management -> Aset Baru."""
        self.stock_management_menu.click()
        self.aset_baru_submenu.click()

    def go_to_aset_lelang(self):
        """Navigasi ke menu Stock Management -> Aset Lelang."""
        self.stock_management_menu.click()
        self.aset_lelang_submenu.click()

    def go_to_user_management(self):
        """Navigasi ke menu User Management."""
        self.user_management_menu.click()

    def go_to_developer(self):
        """Navigasi ke menu Developer."""
        self.developer_menu.click()

