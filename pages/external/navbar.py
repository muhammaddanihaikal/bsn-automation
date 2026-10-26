from playwright.sync_api import Page


class NavbarExternal:
    """Komponen Navbar navigasi untuk Portal External BSN (Nasabah/Publik)."""

    def __init__(self, page: Page):
        self.page = page

        # === 1. MENU NAVIGASI ===
        # TODO: Dani isi locator navigasi portal external di sini
