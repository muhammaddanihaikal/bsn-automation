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
    # User diasumsikan sudah login via fixture logged_in_internal

    # 2. Act (aksi navigasi)
    navbar.go_to_user_management()

    # 3. Assert (validasi)
    # TODO: Dani aktifkan validasi URL dan header tabel saat reconnaisance
    # expect(page).to_have_url(f"{BASE_URL_INTERNAL}{user_list_page.PATH}**")
    # expect(user_list_page.user_table).to_be_visible()
    pass


@allure.title("[TC-INT-USER-02] Menampilkan daftar data Pengguna")
@pytest.mark.smoke
def test_display_user_list(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    user_list_page.open()

    # 2. Act (aksi)
    # Data termuat secara otomatis saat halaman dibuka

    # 3. Assert (validasi)
    # TODO: Dani pastikan baris tabel terlihat
    # expect(user_list_page.table_rows.first).to_be_visible()
    pass


@allure.title("[TC-INT-USER-03] Menambahkan data Pengguna")
@pytest.mark.smoke
def test_add_user(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)
    add_user_page = AddUserPage(page)

    # 1. Arrange (persiapan)
    user_list_page.open()
    user_list_page.click_add_user()

    # Siapkan data tumbal unik
    new_user_name = generate_full_name("User Baru")
    user_payload = {
        "name": new_user_name,
        "username": generate_username("usr"),
        # TODO: Dani lengkapi payload data uji
    }

    # 2. Act (aksi)
    # add_user_page.add_user(user_payload)

    # 3. Assert (validasi)
    # expect(page.get_by_text("Berhasil")).to_be_visible()
    # user_list_page.open()
    # expect(user_list_page.get_user_row(new_user_name)).to_be_visible()
    pass


@allure.title("[TC-INT-USER-04] Menambahkan data Pengguna tanpa mengisi field mandatory")
@pytest.mark.regression
def test_add_user_empty(logged_in_internal: Page):
    page = logged_in_internal
    add_user_page = AddUserPage(page)

    # 1. Arrange (persiapan)
    add_user_page.open()

    # 2. Act (aksi langsung simpan tanpa isi field)
    # add_user_page.save()

    # 3. Assert (validasi pesan error muncul)
    # expect(add_user_page.error_name).to_be_visible()
    pass


@allure.title("[TC-INT-USER-05] Mengubah data Pengguna")
@pytest.mark.smoke
def test_edit_user(logged_in_internal: Page, api_create_user: dict):
    page = logged_in_internal
    user_list_page = UserListPage(page)
    edit_user_page = EditUserPage(page)
    tumbal = api_create_user

    # 1. Arrange (persiapan navigasi ke user tumbal)
    user_list_page.open()
    # user_list_page.click_edit_user(tumbal["name"])

    # 2. Act (aksi update data)
    updated_name = generate_full_name("User Update")
    update_payload = {"name": updated_name}
    # edit_user_page.edit_user(update_payload)

    # 3. Assert (validasi perubahan data)
    # expect(page.get_by_text("Berhasil")).to_be_visible()
    # user_list_page.open()
    # expect(user_list_page.get_user_row(updated_name)).to_be_visible()
    pass


@allure.title("[TC-INT-USER-06] Menghapus data Pengguna")
@pytest.mark.smoke
def test_delete_user(logged_in_internal: Page, api_create_user: dict):
    page = logged_in_internal
    user_list_page = UserListPage(page)
    tumbal = api_create_user

    # 1. Arrange (persiapan)
    user_list_page.open()

    # 2. Act (aksi hapus user tumbal)
    # user_list_page.delete_user(tumbal["name"])

    # 3. Assert (validasi user tidak ada lagi di tabel)
    # expect(user_list_page.get_user_row(tumbal["name"])).to_be_hidden()
    pass


@allure.title("[TC-INT-USER-07] Mencari data Pengguna dengan keyword valid")
@pytest.mark.regression
def test_search_user_valid(logged_in_internal: Page, api_create_user: dict):
    page = logged_in_internal
    user_list_page = UserListPage(page)
    tumbal = api_create_user

    # 1. Arrange (persiapan)
    user_list_page.open()

    # 2. Act (aksi pencarian dengan keyword nama tumbal)
    # user_list_page.filter_by_name(tumbal["name"])
    # user_list_page.search()

    # 3. Assert (validasi hasil pencarian)
    # expect(user_list_page.get_user_row(tumbal["name"])).to_be_visible()
    pass


@allure.title("[TC-INT-USER-08] Mencari data Pengguna dengan keyword tidak valid")
@pytest.mark.regression
def test_search_user_invalid(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    user_list_page.open()

    # 2. Act (aksi pencarian dengan teks acak yang tidak ada di sistem)
    # user_list_page.filter_by_name("DataPalsuTidakAda123XYZ")
    # user_list_page.search()

    # 3. Assert (validasi pesan data kosong / tidak ditemukan)
    # expect(page.get_by_text("Data tidak ditemukan")).to_be_visible()
    pass


@allure.title("[TC-INT-USER-09] Melakukan filter data Pengguna")
@pytest.mark.regression
def test_filter_user(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan)
    user_list_page.open()

    # 2. Act (aksi filter role atau status)
    # user_list_page.filter_by_status("Aktif")
    # user_list_page.search()

    # 3. Assert (validasi baris tabel sesuai filter)
    pass


@allure.title("[TC-INT-USER-10] Mereset filter Pengguna")
@pytest.mark.regression
def test_reset_filter_user(logged_in_internal: Page):
    page = logged_in_internal
    user_list_page = UserListPage(page)

    # 1. Arrange (persiapan filter terisi)
    user_list_page.open()
    # user_list_page.filter_by_name("Test")
    # user_list_page.search()

    # 2. Act (aksi reset)
    # user_list_page.reset_filter()

    # 3. Assert (validasi input pencarian kosong kembali)
    # expect(user_list_page.name_filter).to_have_value("")
    pass
