# 🚀 BSN Automation Cheatsheet: Commands & Playwright Codegen

Kumpulan perintah praktis siap *copy-paste* untuk pengujian otomatis di portal internal BSN (Terasrumah Sandbox).

---

## 🔑 1. Sesi Login & VIP Pass (`storage_state`)

Framework ini menggunakan konsep **Session Reuse** (`storage_state`). Kamu hanya perlu login **satu kali**, dan tiket login akan disimpan di `.auth/internal_state.json`.

### Refresh Sesi Login (Jika sesi habis / pertama kali)
Jalankan test auth untuk login superadmin + otomatis ambil OTP dari Mailpit:
```powershell
uv run pytest tests/internal/test_auth.py -v
```

---

## 🧪 2. Menjalankan Test Fitur (Tanpa Perlu Login Ulang)

### A. Test Form Input Aset Baru (`TC-INT-STOCK-01`)
* **Mode Cepat (Headless - Default)**:
  ```powershell
  uv run pytest tests/internal/stock_management/aset_baru/test_create_asset_baru.py -v
  ```
* **Mode Visual (Buka Browser Chrome Asli)**:
  ```powershell
  uv run pytest tests/internal/stock_management/aset_baru/test_create_asset_baru.py -v --headed
  ```
* **Mode Slow-Motion (Nonton Pelan Tiap Aksi Jeda 500ms)**:
  ```powershell
  uv run pytest tests/internal/stock_management/aset_baru/test_create_asset_baru.py -v --headed --slowmo 500
  ```

### B. Smoke Test Navigasi Sidebar
Menguji klik menu dan accordion sidebar tanpa membebani test fitur:
```powershell
uv run pytest tests/internal/test_navigation.py -v
```

---

## 🎯 3. Playwright Codegen (Otomatis Sudah Login)

Gunakan perintah ini untuk membuka **Playwright Inspector** dan menangkap locator secara visual tanpa harus mengetik email, password, dan OTP dari awal.

### A. Buka Form Input Aset Baru (Wizard 6 Langkah)
```powershell
uv run playwright codegen https://terasrumah-sandbox.zegen.app/internal/stock-management/aset-baru/create --load-storage=.auth/internal_state.json
```

### B. Buka Tabel Daftar Aset Baru
```powershell
uv run playwright codegen https://terasrumah-sandbox.zegen.app/internal/stock-management/aset-baru --load-storage=.auth/internal_state.json
```

### C. Buka Dashboard Utama Internal
```powershell
uv run playwright codegen https://terasrumah-sandbox.zegen.app/internal/dashboard --load-storage=.auth/internal_state.json
```

---

## 🛠️ 4. Mode Debugging (Playwright Inspector)

Jika ingin menjalankan test sambil menghentikan browser (*pause*) langkah demi langkah untuk melihat elemen di layar:

### Aktifkan Mode Debug Inspector:
```powershell
$env:PWDEBUG="1" ; uv run pytest tests/internal/stock_management/aset_baru/test_create_asset_baru.py
```

### Matikan Mode Debug (Kembali ke Normal):
```powershell
$env:PWDEBUG="0"
```

---

## 📊 5. Trace Viewer & Pelaporan Allure

### Rekam Trace Interaktif Saat Test Berjalan:
```powershell
uv run pytest tests/internal/stock_management/aset_baru/test_create_asset_baru.py --tracing on
```

### Buka Rekaman Trace:
```powershell
uv run playwright show-trace test-results/.../trace.zip
```

### Buka Allure Report:
```powershell
allure serve allure-results
```
