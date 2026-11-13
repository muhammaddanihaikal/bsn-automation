import re
import allure
import pytest
from playwright.sync_api import Page, expect

from pages.internal.stock_management.aset_baru.asset_baru_list_page import (
    AssetBaruListPage,
)
from pages.internal.stock_management.aset_baru.create_asset_baru_page import (
    CreateAssetBaruPage,
)
from utils.read_data import read_data

asset_data = read_data("internal/asset_baru_data.json")


class TestAssetBaru:
    @allure.title("[TC-INT-STOCK-01] Berhasil membuat dan mengajukan aset baru")
    @pytest.mark.smoke
    def test_create_asset_baru_valid(self, logged_in_internal: Page):
        page = logged_in_internal
        aset_baru_list_page = AssetBaruListPage(page)
        create_asset_baru_page = CreateAssetBaruPage(page)

        # 1. Arrange (Masuk via Direct URL pintu gerbang modul)
        aset_baru_list_page.open()
        aset_baru_list_page.click_input_aset_baru()

        # 2. Act & Checkpoints (Langkah 1 s/d 4)
        # --- LANGKAH 1: INFORMASI DASAR ---
        create_asset_baru_page.fill_step_1_informasi(asset_data["step_1_informasi"])
        expect(create_asset_baru_page.price).to_be_visible()

        # --- LANGKAH 2: HARGA ---
        create_asset_baru_page.fill_step_2_harga(asset_data["step_2_harga"])
        expect(create_asset_baru_page.galeri_btn).to_be_visible()

        # --- LANGKAH 3: GALERI FOTO & DENAH ---
        create_asset_baru_page.upload_step_3_galeri(asset_data["step_3_galeri"])
        expect(create_asset_baru_page.legalitas_btn).to_be_visible()

        # --- LANGKAH 4: DOKUMEN & LEGALITAS ---
        create_asset_baru_page.fill_step_4_legalitas(asset_data["step_4_legalitas"])
        expect(create_asset_baru_page.lokasi_btn).to_be_visible()

        # --- LANGKAH 5: LOKASI & GEOSPASIAL ---
        create_asset_baru_page.fill_step_5_lokasi(asset_data["step_5_lokasi"])
        expect(create_asset_baru_page.fasilitas_btn).to_be_visible()

        # --- LANGKAH 6: FASILITAS & SUBMIT AKHIR ---
        create_asset_baru_page.fill_step_6_fasilitas(asset_data["step_6_fasilitas"])

        # 3. Assert (Validasi Halaman Detail Aset Baru - The Golden Anchors)
        # Anchor 1: URL berhasil beralih ke halaman detail unik
        expect(page).to_have_url(
            re.compile(r".*/stock-management/aset-baru/detail/.*"),
            timeout=60000,
        )

        # Anchor 2: Judul H1 aset sesuai data yang diinput
        expected_title = f"{asset_data['step_1_informasi']['project']} - {asset_data['step_1_informasi']['unit_type']}"
        expect(page.get_by_role("heading", level=1)).to_contain_text(expected_title)

        # Anchor 3: Status badge awal adalah VERIFIKASI & Unpublished
        expect(page.locator("h1 + span")).to_contain_text("Verifikasi", ignore_case=True)
        expect(page.get_by_text("Unpublished")).to_be_visible()
