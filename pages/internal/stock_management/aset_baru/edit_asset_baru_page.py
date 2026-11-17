from playwright.sync_api import Page

from pages.internal.stock_management.aset_baru.create_asset_baru_page import (
    CreateAssetBaruPage,
)


class EditAssetBaruPage(CreateAssetBaruPage):
    """Halaman Edit Aset Baru — mewarisi seluruh locator wizard Langkah 1-6 dari CreateAssetBaruPage."""

    def __init__(self, page: Page):
        super().__init__(page)
        # Seluruh locator form Langkah 1-6 & tombol submit_btn diwarisi otomatis (95% DOM identik)
        self.PATH_PREFIX = "/internal/stock-management/aset-baru/edit/"
        self.heading = self.page.get_by_role("heading", level=1)

        # === A. NAVIGASI WIZARD TAMBAHAN (MODE EDIT) ===
        # Semua tab Langkah 1-6 langsung aktif di mode Edit sehingga bisa lompat tab bebas
        self.sebelumnya_btn = self.page.get_by_test_id("aset-baru-form-prev-button")
        self.simpan_draft_btn = self.page.get_by_test_id(
            "aset-baru-form-save-draft-button"
        )

        # === B. LOCATOR KHUSUS LANGKAH 3 (GALERI FOTO TERSIMPAN) ===
        # Tombol aksi pada setiap kartu foto yang sudah tersimpan di server
        self.hapus_foto_btn = self.page.get_by_role("button", name="Hapus foto")
        self.ganti_foto_btn = self.page.get_by_role("button", name="Ganti foto")

        # === C. LOCATOR KHUSUS LANGKAH 4 (DOKUMEN LEGALITAS TERSIMPAN) ===
        # Dokumen yang sudah terunggah tombolnya berubah dari 'Unggah File' menjadi 'Lihat File'
        self.lihat_file_btn = self.page.get_by_role("button", name="Lihat File")

        # === D. LOCATOR KHUSUS LANGKAH 5 (DESTINASI TERSIMPAN) ===
        # Kecualikan -delete-button agar hanya menangkap elemen baris tabel destinasinya saja
        self.destinasi_rows = self.page.locator(
            "[data-testid^='aset-baru-lokasi-destinasi-row-']:not([data-testid$='-delete-button'])"
        )

    # =========================================================================
    # ACTION METHODS KHUSUS EDIT
    # =========================================================================

    def delete_dokumen_legalitas(self, nama_dokumen: str):
        """Menghapus berkas PDF yang sudah tersimpan pada card dokumen tertentu."""
        # Tombol ikon sampah merah di card tersimpan berada di posisi terakhir setelah 'Lihat File'
        card = (
            self.page.locator(".rounded-lg.border").filter(has_text=nama_dokumen).first
        )
        card.locator("button").last.click()

    def delete_destinasi(self, nama_destinasi: str):
        """Menghapus satu baris destinasi strategis tersimpan berdasarkan namanya."""
        self.page.get_by_role("button", name=f"Hapus {nama_destinasi}").click()

    def submit_perubahan(self):
        """Menekan tombol submit akhir ('Simpan dan Ajukan Perubahan')."""
        # Pakai submit_btn warisan karena data-testid sama persis dengan mode Create
        self.submit_btn.click()
