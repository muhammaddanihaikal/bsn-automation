import os

import allure
import pytest
from playwright.sync_api import Page, expect

from config import BASE_URL_INTERNAL
from pages.internal.login_page import LoginPage


class TestAuthInternal:
    @allure.title("[TC-INT-AUTH-01] Login valid berhasil masuk dashboard")
    def test_login_valid(self, page: Page):
        page = LoginPage(page)

        # 1. Arrange
        email = os.getenv("INTERNAL_SUPERADMIN_EMAIL")
        password = os.getenv("INTERNAL_SUPERADMIN_PASSWORD")

        # 2. Act
        page.login(email, password)

        # 3. Assert

    @allure.title("[TC-INT-AUTH-02] Logout redirect ke halaman Login")
    def test_logout(self, logged_in_internal: Page):
        page = logged_in_internal

        # 1. Arrange
        pass

        # 2. Act
        pass

        # 3. Assert
        pass

    @allure.title(
        "[TC-INT-AUTH-03] Button 'Masuk dengan akun lain' kembali ke form login"
    )
    @pytest.mark.regression
    def test_other_account_btn(self, page: Page):
        login_page = LoginPage(page)

        # 1. Arrange
        pass

        # 2. Act
        pass

        # 3. Assert
        pass

    @allure.title(
        "[TC-INT-AUTH-04] Button 'Halaman Utama' di auto-logout redirect ke Login internal"
    )
    @pytest.mark.regression
    def test_home_btn_redirect(self, page: Page):
        login_page = LoginPage(page)

        # 1. Arrange
        pass

        # 2. Act
        pass

        # 3. Assert
        pass
