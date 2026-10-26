# Template & Panduan Standar Test Case — BSN Automation

> Diadaptasi dari standar tim (`tc_template_v3.md`).

---

## 1. Aturan Format Test Case (.md)
Setiap test case ditulis dengan format:
- **Module:** Nama modul (contoh: Internal / External)
- **Sub Menu:** Nama sub menu (contoh: Manajemen Pengguna)
- **Description:** Positive Case / Negative Case
- **Priority:** Critical / High / Normal / Low

### Format Steps & Expected Results (Atomic):
- **1 langkah = 1 aksi pengguna** (DILARANG menggabungkan 2 aksi dalam 1 nomor).
- **Jumlah baris Steps HARUS sama persis dengan jumlah baris Expected Results**.
- Penulisan Expected Results selalu diawali kata **"Berhasil"** untuk positive case.

---

## 2. Urutan Alur Bisnis (Business Flow)
Penyusunan Test Case selalu mengikuti urutan alur bisnis:
1. Membuka halaman (`test_open_*`)
2. Menampilkan data tabel (`test_display_*`)
3. Menambahkan data (`test_add_*`)
4. Validasi field wajib / empty (`test_add_*_empty`)
5. Mengubah data (`test_edit_*`)
6. Menghapus data (`test_delete_*`)
7. Mencari data valid (`test_search_*_valid`)
8. Mencari data tidak valid (`test_search_*_invalid`)
9. Filter data (`test_filter_*`)
10. Reset filter (`test_reset_filter_*`)

---

## 3. Template Kerangka Page Object Baru (Wajib Dikosongkan)

Saat membuat Page Object baru, gunakan format kosong ini:

```python
from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class NamaPage(BasePage):
    """Halaman <Nama Fitur> — Portal Internal BSN."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.PATH = "/internal/<rute_fitur>"

        # === 1. LOCATOR ELEMEN ===
        # TODO: Dani isi locator di sini

        # === 2. TOMBOL AKSI ===
        # TODO: Dani isi tombol di sini

    # =========================================================================
    # ACTION METHODS
    # =========================================================================

    def method_aksi(self, parameter):
        """Docstring deskripsi aksi."""
        pass
```

---

## 4. Template Kerangka Test Baru (Pola AAA Wajib Dikosongkan)

Saat membuat Test baru, gunakan format AAA kosong ini:

```python
import allure
import pytest
from playwright.sync_api import Page, expect
from config import BASE_URL_INTERNAL

@allure.title("[TC-INT-MODUL-01] Judul test case spesifik")
@pytest.mark.smoke
def test_nama_skenario(logged_in_internal: Page):
    page = logged_in_internal
    # Inisialisasi Page Object

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass
```

---

## 5. Aturan Penulisan Komentar Kode
- **DILARANG membuat komentar panjang/bertele-tele.**
- Komentar kode **cukup 1 baris saja**, simpel, ringkas, dan *to the point*.
- Contoh yang dianjurkan:
  ```python
  # 1. Arrange
  # Buka halaman tambah user
  # 2. Act
  # Simpan form
  # 3. Assert
  # Pastikan alert sukses muncul
  ```

