from playwright.sync_api import Page


class Sidebar:
    """Komponen Sidebar navigasi menu utama Portal Internal BSN."""

    def __init__(self, page: Page):
        self.page = page

        # === 1. LOCATOR MENU UTAMA SIDEBAR ===
        # TODO: Dani isi locator menu Dashboard
        # TODO: Dani isi locator menu Customer Management
        # TODO: Dani isi locator menu Stock Management
        # TODO: Dani isi locator menu Developer
        # TODO: Dani isi locator menu Media & Information
        # TODO: Dani isi locator menu User Management

        # === 2. LOCATOR SUB-MENU STOCK MANAGEMENT ===
        # TODO: Dani isi locator sub-menu Aset Baru
        # TODO: Dani isi locator sub-menu Aset Lelang

    # =========================================================================
    # NAVIGATION METHODS
    # =========================================================================

    def go_to_dashboard(self):
        """Navigasi ke menu Dashboard."""
        # TODO: Dani implementasikan klik menu Dashboard
        pass

    def go_to_aset_baru(self):
        """Navigasi ke menu Stock Management -> Aset Baru."""
        # TODO: Dani implementasikan klik menu Stock Management lalu klik Aset Baru
        pass

    def go_to_user_management(self):
        """Navigasi ke menu User Management."""
        # TODO: Dani implementasikan klik menu User Management
        pass
