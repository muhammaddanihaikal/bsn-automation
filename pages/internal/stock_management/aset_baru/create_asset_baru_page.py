from pathlib import Path

from playwright.sync_api import Page, expect

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
        self.price = self.page.locator("#price")
        self.promo_switch = self.page.locator("#promo_enabled")
        self.normal_price = self.page.locator("#normal_price")
        self.dp_percentage = self.page.locator("#dp_percent")

        # === 3. LOCATOR LANGKAH 3 (GALERI FOTO & DENAH) ===
        self.galeri_button = self.page.get_by_role("button", name="3 Galeri")
        self.file_input = self.page.locator("input[type='file']")

        # === 4. LOCATOR LANGKAH 4 (LEGALITAS) ===
        self.legalitas_button = self.page.get_by_role("button", name="4 Legalitas")

        # TODO: Dani isi locator checklist dokumen (opsional)

        # === 5. LOCATOR LANGKAH 5 (LOKASI & GEOSPASIAL) ===
        self.lokasi_button = self.page.get_by_role("button", name="5 Lokasi")
        self.alamat_input = self.page.locator("#address")
        self.provinsi_select = self.page.locator("#province")
        self.kota_select = self.page.locator("#city")
        self.kecamatan_select = self.page.locator("#district")
        self.kelurahan_select = self.page.locator("#sub_district")
        self.kode_pos_input = self.page.locator("#postal_code")
        self.koordinat_input = self.page.locator("#coordinate")

        # === 5b. LOCATOR MODAL DESTINASI STRATEGIS (LANGKAH 5) ===
        self.tambah_destinasi_btn = self.page.get_by_test_id("aset-baru-lokasi-destinasi-add-button")
        self.destinasi_modal_name_input = self.page.get_by_test_id("aset-baru-destinasi-modal-name-input")
        self.destinasi_modal_access_point_input = self.page.get_by_test_id("aset-baru-destinasi-modal-access-point-input")
        self.destinasi_modal_category_select = self.page.get_by_test_id("aset-baru-destinasi-modal-category-select")
        self.destinasi_modal_coordinate_input = self.page.get_by_test_id("aset-baru-destinasi-modal-coordinate-input")
        self.destinasi_modal_distance_input = self.page.get_by_test_id("aset-baru-destinasi-modal-distance-input")
        self.destinasi_modal_duration_input = self.page.get_by_test_id("aset-baru-destinasi-modal-duration-input")
        self.destinasi_modal_submit_btn = self.page.get_by_test_id("aset-baru-destinasi-modal-submit-button")

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

    def fill_step_2_harga(self, data: dict):
        """Mengisi data harga transaksi dan simulasi DP pada Langkah 2."""
        # 1. Isi harga aset (netto)
        self.price.fill(data["price"])

        # 2. Atur switch promo coret & isi harga normal jika aktif
        if data.get("promo_coret", False):
            self.promo_switch.check()
            self.normal_price.fill(data["normal_price"])
        else:
            self.promo_switch.uncheck()

        # 3. Isi persentase DP
        self.dp_percentage.fill(data["persen_dp"])

        # 4. Klik Selanjutnya
        self.selanjutnya_btn.click()

    def upload_step_3_galeri(self, data: dict):
        """Mengunggah 4 foto aset dan 1 denah pada Langkah 3 serta mengatur kategori masing-masing."""
        # 1. Konversi path gambar relatif ke absolute path lokal
        file_paths = [str(Path(p).resolve()) for p in data["images"]]

        # 2. Upload sekaligus seluruh file via set_input_files
        self.file_input.set_input_files(file_paths)
        self.page.wait_for_timeout(2000)

        # 3. Atur kategori foto kartu ke-2 s/d ke-5 secara manual satu per satu
        selects = self.page.locator(".ant-select").all()
        dropdown = self.page.locator(
            ".ant-select-dropdown:not(.ant-select-dropdown-hidden)"
        )

        # Card 2 (Index 1): Interior / Ruang Tamu
        selects[1].click()
        dropdown.get_by_text("Interior / Ruang Tamu", exact=True).click()
        dropdown.wait_for(state="hidden")

        # Card 3 (Index 2): Interior / Dapur
        selects[2].click()
        dropdown.get_by_text("Interior / Dapur", exact=True).click()
        dropdown.wait_for(state="hidden")

        # Card 4 (Index 3): Interior / Kamar Tidur
        selects[3].click()
        dropdown.get_by_text("Interior / Kamar Tidur", exact=True).click()
        dropdown.wait_for(state="hidden")

        # Card 5 (Index 4): Denah / Site Plan
        selects[4].click()
        dropdown.get_by_text("Denah / Site Plan", exact=True).click()
        dropdown.wait_for(state="hidden")

        # Jeda 5 detik untuk inspeksi visual di layar
        self.page.wait_for_timeout(5000)

        # 4. Klik tombol Selanjutnya untuk lanjut ke Langkah 4
        self.selanjutnya_btn.click()

    def upload_dokumen_legalitas(self, nama_dokumen: str, file_path: str):
        """Mengunggah berkas PDF ke kotak dokumen tertentu menggunakan Scoped Locator dan Smart Timeout."""
        card = self.page.locator(".rounded-lg.border").filter(has_text=nama_dokumen).first
        # 1. Centang checkbox dokumen
        card.locator("input[type='checkbox']").check()
        # 2. Upload file PDF ke input file dalam card tersebut
        resolved_path = Path(file_path).resolve()
        card.locator("input[type='file']").set_input_files(str(resolved_path))
        # 3. Smart Timeout: Tunggu hingga nama file PDF muncul di dalam card
        card.get_by_text(resolved_path.name).wait_for(state="visible")

    def fill_step_4_legalitas(self, data: dict):
        """Memproses Langkah 4: Legalitas dengan mengunggah dokumen yang dipilih."""
        dokumen_list = data.get("dokumen", [])
        for doc in dokumen_list:
            self.upload_dokumen_legalitas(doc["nama"], doc["file"])

        # Jeda 3 detik untuk inspeksi visual dokumen di layar
        self.page.wait_for_timeout(3000)

        # Klik tombol Selanjutnya untuk lanjut ke Langkah 5
        self.selanjutnya_btn.click()

    def add_destinasi(self, data: dict):
        """Menambahkan satu destinasi strategis melalui modal pop-up."""
        self.tambah_destinasi_btn.scroll_into_view_if_needed()
        self.tambah_destinasi_btn.click()

        # 1. Isi nama destinasi dan rute akses
        self.destinasi_modal_name_input.fill(data["name"])
        self.destinasi_modal_access_point_input.fill(data["access_point"])

        # 2. Pilih kategori destinasi
        self.destinasi_modal_category_select.click()
        dropdown = self.page.locator(
            ".ant-select-dropdown:not(.ant-select-dropdown-hidden)"
        )
        dropdown.get_by_text(data["category"], exact=True).click()
        dropdown.wait_for(state="hidden")

        # 3. Isi koordinat, jarak (km), dan durasi (menit)
        self.destinasi_modal_coordinate_input.fill(data["coordinate"])
        self.destinasi_modal_distance_input.fill(data["distance_km"])
        self.destinasi_modal_duration_input.fill(data["duration_minutes"])

        # 4. Klik Tambah untuk menyimpan ke tabel
        self.destinasi_modal_submit_btn.click()
        self.page.wait_for_timeout(500)

    def fill_step_5_lokasi(self, data: dict):
        """Mengisi data alamat, wilayah bertingkat, dan destinasi pada Langkah 5."""
        # 1. Isi Alamat Lengkap
        self.alamat_input.fill(data["alamat_lengkap"])

        # 2. Dropdown Bertingkat Wilayah dengan Smart Wait
        dropdown = self.page.locator(
            ".ant-select-dropdown:not(.ant-select-dropdown-hidden)"
        )

        # Pilih Provinsi
        self.provinsi_select.click()
        dropdown.get_by_text(data["provinsi"], exact=True).click()
        dropdown.wait_for(state="hidden")

        # Pilih Kota / Kabupaten (menunggu enabled)
        expect(self.kota_select).to_be_enabled()
        self.kota_select.click()
        dropdown.get_by_text(data["kota"], exact=True).click()
        dropdown.wait_for(state="hidden")

        # Pilih Kecamatan (menunggu enabled)
        expect(self.kecamatan_select).to_be_enabled()
        self.kecamatan_select.click()
        dropdown.get_by_text(data["kecamatan"], exact=True).click()
        dropdown.wait_for(state="hidden")

        # Pilih Kelurahan (menunggu enabled)
        expect(self.kelurahan_select).to_be_enabled()
        self.kelurahan_select.click()
        dropdown.get_by_text(data["kelurahan"], exact=True).click()
        dropdown.wait_for(state="hidden")

        # 3. Isi Kode Pos dan Koordinat Peta
        self.kode_pos_input.fill(data["kode_pos"])
        self.koordinat_input.fill(data["koordinat"])

        # 4. Tambah Destinasi Strategis (jika ada)
        destinasi_list = data.get("destinasi", [])
        for dest in destinasi_list:
            self.add_destinasi(dest)

        # Jeda 3 detik untuk inspeksi visual tabel di layar
        self.page.wait_for_timeout(3000)

        # 5. Klik tombol Selanjutnya untuk lanjut ke Langkah 6 (Fasilitas)
        self.selanjutnya_btn.click()

    def fill_step_6_fasilitas(self, data: dict):
        """Mengisi fasilitas properti dan submit akhir pada Langkah 6."""
        # TODO: Dani aktifkan fasilitas yang diinginkan lalu klik 'Simpan dan Ajukan Perubahan'
        pass
