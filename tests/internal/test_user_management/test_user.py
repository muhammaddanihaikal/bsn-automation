"""
Test Suite: Manajemen Pengguna (User Management) — Portal Internal BSN
Mencakup TC-INT-USER-01 s/d TC-INT-USER-10 (Gaya AAA Pattern)
"""
import allure
import pytest
from playwright.sync_api import Page, expect

from config import BASE_URL_INTERNAL
from pages.internal.navbar import Navbar
from pages.internal.user_management.add_user_page import AddUserPage
from pages.internal.user_management.edit_user_page import EditUserPage
from pages.internal.user_management.user_list_page import UserListPage
from utils.data_factory import generate_full_name, generate_username
from utils.read_data import read_data

USER_DATA = read_data("internal/user_data.json")


@allure.title("[TC-INT-USER-01] Membuka halaman Manajemen Pengguna")
@pytest.mark.smoke
def test_open_user_management(logged_in_internal: Page):
    page = logged_in_internal
    navbar = Navbar(page)
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-INT-USER-02] Menampilkan daftar data Pengguna")
@pytest.mark.smoke
def test_display_user_list(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-INT-USER-03] Menambahkan data Pengguna")
@pytest.mark.smoke
def test_add_user(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)
    add_user_page = AddUserPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-INT-USER-04] Menambahkan data Pengguna tanpa mengisi field mandatory")
@pytest.mark.regression
def test_add_user_empty(logged_in_internal: Page):
    page = logged_in_internal
    add_user_page = AddUserPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-INT-USER-05] Mengubah data Pengguna")
@pytest.mark.smoke
def test_edit_user(logged_in_internal: Page, api_create_user: dict):
    page = logged_in_internal
    user_list_page = UserListPage(page)
    edit_user_page = EditUserPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-INT-USER-06] Menghapus data Pengguna")
@pytest.mark.smoke
def test_delete_user(logged_in_internal: Page, api_create_user: dict):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-INT-USER-07] Mencari data Pengguna dengan keyword valid")
@pytest.mark.regression
def test_search_user_valid(logged_in_internal: Page, api_create_user: dict):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-INT-USER-08] Mencari data Pengguna dengan keyword tidak valid")
@pytest.mark.regression
def test_search_user_invalid(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-INT-USER-09] Melakukan filter data Pengguna")
@pytest.mark.regression
def test_filter_user(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-INT-USER-10] Mereset filter Pengguna")
@pytest.mark.regression
def test_reset_filter_user(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass
