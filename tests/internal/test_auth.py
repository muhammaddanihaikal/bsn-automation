import allure
from playwright.sync_api import Page, expect

from config import (
    BASE_URL_INTERNAL,
    INTERNAL_SUPERADMIN_EMAIL,
    INTERNAL_SUPERADMIN_PASSWORD,
)
from helpers.mailpit import get_otp
from pages.internal.dashboard.dashboard_page import DashboardPage
from pages.internal.login_page import LoginPage


class TestAuthInternal:
    @allure.title("[TC-INT-AUTH-01] Login valid berhasil masuk dashboard")
    def test_login_valid(self, page: Page):
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)

        # 1. Arrange
        login_page.open()

        # 2. Act
        login_page.login(INTERNAL_SUPERADMIN_EMAIL, INTERNAL_SUPERADMIN_PASSWORD)
        otp = get_otp(INTERNAL_SUPERADMIN_EMAIL)
        login_page.fill_otp(otp)

        # 3. Assert
        expect(page).to_have_url(f"{BASE_URL_INTERNAL}{dashboard_page.PATH}")
        expect(dashboard_page.heading).to_be_visible()
