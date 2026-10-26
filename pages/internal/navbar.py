from playwright.sync_api import Page


class Navbar:
    """Komponen Navbar / Sidebar navigasi untuk Portal Internal BSN."""

    def __init__(self, page: Page):
        self.page = page

        # === MENU NAVIGASI UTAMA ===
        # TODO: Dani isi nama accessible link atau role setelah reconnaisance
        self.menu_dashboard = page.get_by_role("link", name="Dashboard")
        self.menu_user_management = page.get_by_role("link", name="Manajemen Pengguna")

        # === USER PROFIL & LOGOUT ===
        # TODO: Dani sesuaikan selector dropdown profile & menu keluar
        self.profile_dropdown = page.get_by_role("button", name="Profile")
        self.logout_menu_item = page.get_by_role("menuitem", name="Keluar")

    def go_to_user_management(self):
        """Klik menu navigasi ke Manajemen Pengguna."""
        # TODO: Dani aktifkan aksi navigasi
        self.menu_user_management.click()

    def logout(self):
        """Melakukan proses logout melalui dropdown user profile."""
        # TODO: Dani aktifkan aksi logout
        self.profile_dropdown.click()
        self.logout_menu_item.click()
