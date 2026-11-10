from playwright.sync_api import Page

from pages.base_page import BasePage


class CreateAssetBaruPage(BasePage):
    """Halaman Form Input Aset Baru (Wizard 6 Langkah) — Portal Internal BSN."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/stock-management/aset-baru/create"

        # === 1. LOCATOR LANGKAH 1 (INFORMASI ASET) ===
        self.informasi_button = self.page.get_by_role("button", name="1 Informasi")
        self.developer_select = self.page.locator("#developer_id")
        self.asset_type_select = self.page.locator("#asset_type")
        self.project_select = self.page.locator("#project_id")
        self.cluster_select = self.page.locator("#cluster_id")
        self.unit_type_select = self.page.locator("#unit_type")
        self.stock_unit_input = self.page.locator("#stock_unit")
        self.subsidi_btn = self.page.get_by_role("button", name="Subsidi", exact=True)
        self.non_subsidi_btn = self.page.get_by_role("button", name="Non Subsidi")

        self.land_area_input = self.page.locator("#land_area")
        self.floors_input = self.page.locator("#floors")
        self.bedrooms_input = self.page.locator("#bedrooms")
        self.bathrooms_input = self.page.locator("#bathrooms")

        self.description_input = self.page.get_by_role(
            "textbox", name="Ceritakan keunggulan lokasi,"
        )

        # === 2. LOCATOR LANGKAH 2 (HARGA) ===
        self.harga_button = self.page.get_by_role("button", name="2 Harga")

        # TODO: Dani isi locator textbox Harga Aset (Netto)
        # TODO: Dani isi locator textbox Persentase DP (%)

        # === 3. LOCATOR LANGKAH 3 (GALERI FOTO & DENAH) ===
        self.galeri_button = self.page.get_by_role("button", name="3 Galeri")
        # TODO: Dani isi locator input upload foto & denah (set_input_files)
        # TODO: Dani isi locator dropdown kategori foto (Wajib: Fasad Depan)

        # === 4. LOCATOR LANGKAH 4 (LEGALITAS) ===
        self.legalitas_button = self.page.get_by_role("button", name="4 Legalitas")

        # TODO: Dani isi locator checklist dokumen (opsional)

        # === 5. LOCATOR LANGKAH 5 (LOKASI & GEOSPASIAL) ===
        self.lokasi_button = self.page.get_by_role("button", name="5 Lokasi")
        # TODO: Dani isi locator textarea Alamat Lengkap
        # TODO: Dani isi locator dropdown Provinsi, Kota, Kecamatan, Kelurahan
        # TODO: Dani isi locator textbox Kode Pos dan Koordinat GPS Lat/Long

        # === 6. LOCATOR LANGKAH 6 (FASILITAS & SPESIFIKASI) ===
        self.fasilitas_button = self.page.get_by_role("button", name="6 Fasilitas")

        # TODO: Dani isi locator textbox Jalan Depan & Daya Listrik
        # TODO: Dani isi locator toggle switch fasilitas unit & kawasan

        # === 7. TOMBOL NAVIGASI WIZARD ===
        self.selanjutnya_btn = self.page.get_by_test_id("aset-baru-form-next-button")

    # =========================================================================
    # ACTION METHODS
    # =========================================================================

    def fill_step_1_informasi(self, data: dict):
        """Mengisi data informasi dasar aset pada Langkah 1."""
        # 1. Pilih Developer
        self.developer_select.click()
        self.page.get_by_text(data["developer"]).click()

        # 2. Pilih Tipe Aset
        self.asset_type_select.click()
        # Scroll dropdown ke bawah biar opsi 'Rumah' muncul di HTML
        dropdown = self.page.locator(".ant-select-dropdown").filter(
            has_text="Apartemen"
        )
        dropdown.locator(".rc-virtual-list-holder").evaluate("el => el.scrollTop = 500")
        dropdown.get_by_text(data["asset_type"], exact=True).click()

        # 3. Pilih Proyek & Klaster
        self.project_select.click()
        self.page.get_by_text(data["project"]).click()
        self.cluster_select.click()
        self.page.get_by_text(data["cluster"]).click()

        # 4. Pilih Tipe Unit
        self.unit_type_select.click()
        self.page.get_by_text(data["unit_type"]).nth(1).click()

        # 5. Isi Stok Unit & Subsidi
        self.stock_unit_input.fill(data["stock_unit"])
        self.subsidi_btn.click() if data["subsidi"] else self.non_subsidi_btn.click()

        # 6. Isi Dimensi & Spesifikasi
        self.land_area_input.fill(data["land_area"])
        self.floors_input.fill(data["floors"])
        self.bedrooms_input.fill(data["bedrooms"])
        self.bathrooms_input.fill(data["bathrooms"])
        self.description_input.fill(data["description"])

        # 7. Klik Selanjutnya
        self.selanjutnya_btn.click()

    def fill_step_2_harga(self, harga: str, persen_dp: str = "5.0"):
        """Mengisi data harga transaksi dan simulasi DP pada Langkah 2."""
        # TODO: Dani ketik langkah pengisian Langkah 2 lalu klik Selanjutnya
        pass

    def upload_step_3_galeri(self, foto_paths: list[str], denah_path: str):
        """Mengunggah 4 foto aset dan 1 denah pada Langkah 3."""
        # TODO: Dani ketik langkah upload 5 file gambar dan klik Selanjutnya
        pass

    def fill_step_4_legalitas(self):
        """Memproses Langkah 4: Legalitas (opsional)."""
        # TODO: Dani cukup klik tombol Selanjutnya untuk melewati langkah ini
        pass

    def fill_step_5_lokasi(self, data: dict):
        """Mengisi data alamat dan wilayah geospasial pada Langkah 5."""
        # TODO: Dani ketik langkah pengisian alamat & wilayah lalu klik Selanjutnya
        pass

    def fill_step_6_fasilitas(self):
        """Mengisi fasilitas properti dan submit akhir pada Langkah 6."""
        # TODO: Dani aktifkan fasilitas yang diinginkan lalu klik 'Simpan dan Ajukan Perubahan'
        pass
