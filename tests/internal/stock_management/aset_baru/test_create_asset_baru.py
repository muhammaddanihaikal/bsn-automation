import allure
import pytest
from playwright.sync_api import Page, expect

from pages.internal.stock_management.aset_baru.asset_baru_list_page import (
    AssetBaruListPage,
)
from pages.internal.stock_management.aset_baru.create_asset_baru_page import (
    CreateAssetBaruPage,
)


class TestAssetBaru:
    @allure.title("[TC-INT-STOCK-01] Berhasil membuat dan mengajukan aset baru")
    @pytest.mark.smoke
    def test_create_asset_baru_valid(self, logged_in_internal: Page):
        page = logged_in_internal
        list_page = AssetBaruListPage(page)
        create_page = CreateAssetBaruPage(page)

        # 1. Arrange
        # TODO: Dani buka halaman list aset baru dan klik button '+ Input Aset Baru'
        pass

        # 2. Act
        # TODO: Dani panggil method pengisian langkah 1 sampai langkah 6
        pass

        # 3. Assert
        # TODO: Dani lakukan validasi notifikasi sukses dan kemunculan data di list
        pass
