from playwright.sync_api import Page


class NavbarExternal:
    """Komponen Navbar navigasi untuk Portal External BSN (Nasabah/Publik)."""

    def __init__(self, page: Page):
        self.page = page

        # TODO: Dani isi selector navigasi portal external setelah portal internal stabil
        self.menu_beranda = page.get_by_role("link", name="Beranda")
        self.menu_login = page.get_by_role("link", name="Masuk")
