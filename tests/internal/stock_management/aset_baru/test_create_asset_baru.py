import allure
import pytest
from playwright.sync_api import Page, expect

from pages.internal.sidebar import Sidebar
from pages.internal.stock_management.aset_baru.asset_baru_list_page import (
    AssetBaruListPage,
)
from pages.internal.stock_management.aset_baru.create_asset_baru_page import (
    CreateAssetBaruPage,
)
from utils.read_data import read_data


class TestAssetBaru:
    @allure.title("[TC-INT-STOCK-01] Berhasil membuat dan mengajukan aset baru")
    @pytest.mark.smoke
    def test_create_asset_baru_valid(self, logged_in_internal: Page):
        page = logged_in_internal
        aset_baru_list_page = AssetBaruListPage(page)
        create_asset_baru_page = CreateAssetBaruPage(page)
        sidebar = Sidebar(page)

        # 1. Arrange (Navigasi via Sidebar)
        sidebar.go_to_aset_baru()
        aset_baru_list_page.click_input_aset_baru()

        # 2. Act (Eksekusi Langkah 1 menggunakan data JSON)
        asset_data = read_data("internal/asset_baru_data.json")
        create_asset_baru_page.fill_step_1_informasi(
            asset_data["step_1_informasi"]
        )

        # 3. Assert (Berhasil berpindah ke Langkah 2 Harga)
        expect(create_asset_baru_page.harga_button).to_be_visible()
