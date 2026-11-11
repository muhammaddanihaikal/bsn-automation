import allure
import pytest
from playwright.sync_api import Page, expect

from config import BASE_URL_INTERNAL
from pages.internal.sidebar import Sidebar


@allure.epic("Portal Internal BSN")
@allure.feature("Sidebar Navigation")
class TestSidebarNavigation:
    """Smoke Test: Menguji interaksi dan navigasi seluruh menu sidebar."""

    # -------------------------------------------------------------------------
    # 1. UJI MENU INDUK (ACCORDION BEHAVIOR)
    # -------------------------------------------------------------------------
    @allure.title(
        "[TC-INT-NAV-01] Accordion Stock Management dapat membuka dan menutup sub-menu"
    )
    @pytest.mark.smoke
    def test_stock_management_accordion_toggle(self, logged_in_internal: Page):
        page = logged_in_internal
        sidebar = Sidebar(page)

        # 1. Klik menu induk untuk membuka accordion
        sidebar.stock_management_menu.click()

        # 2. Asersi: Sub-menu wajib muncul di layar
        expect(sidebar.aset_baru_submenu).to_be_visible()
        expect(sidebar.aset_lelang_submenu).to_be_visible()

        # 3. Klik lagi untuk menutup (toggle close)
        sidebar.stock_management_menu.click()

        # 4. Asersi: Sub-menu wajib tersembunyi kembali
        expect(sidebar.aset_baru_submenu).not_to_be_visible()

    # -------------------------------------------------------------------------
    # 2. UJI SUB-MENU (CHILD ROUTING)
    # -------------------------------------------------------------------------
    @allure.title(
        "[TC-INT-NAV-02] Navigasi sub-menu Aset Baru mengarahkan ke URL yang benar"
    )
    @pytest.mark.smoke
    def test_navigate_to_aset_baru(self, logged_in_internal: Page):
        page = logged_in_internal
        sidebar = Sidebar(page)

        # Klik menu induk lalu sub-menu Aset Baru
        sidebar.go_to_aset_baru()

        # Asersi: URL berpindah ke halaman Aset Baru
        expect(page).to_have_url(
            f"{BASE_URL_INTERNAL}/internal/stock-management/aset-baru"
        )

    # -------------------------------------------------------------------------
    # 3. UJI MENU TUNGGAL (DIRECT ROUTING)
    # -------------------------------------------------------------------------
    @allure.title(
        "[TC-INT-NAV-03] Navigasi menu tunggal User Management mengarahkan ke URL yang benar"
    )
    @pytest.mark.smoke
    def test_navigate_to_user_management(self, logged_in_internal: Page):
        page = logged_in_internal
        sidebar = Sidebar(page)

        # Klik menu User Management
        sidebar.go_to_user_management()

        # Asersi: URL berpindah ke halaman User Management
        expect(page).to_have_url(f"{BASE_URL_INTERNAL}/internal/users")
