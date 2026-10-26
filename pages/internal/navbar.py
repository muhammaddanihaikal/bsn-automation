from playwright.sync_api import Page


class Navbar:
    """Komponen Navbar / Sidebar navigasi untuk Portal Internal BSN."""

    def __init__(self, page: Page):
        self.page = page

        # 1. Menu navigasi
        # TODO: Dani isi locator menu navigasi di sini

        # 2. Profil & logout
        # TODO: Dani isi locator dropdown & tombol keluar di sini

    def go_to_user_management(self):
        """Klik menu navigasi ke Manajemen Pengguna."""
        pass

    def logout(self):
        """Melakukan proses logout melalui dropdown user profile."""
        pass
