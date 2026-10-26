# AGENTS.md — BSN Automation Test

> **Baca file ini sebelum melakukan perubahan apapun pada project ini.**
> File ini adalah panduan wajib untuk AI assistant manapun yang bekerja di repo ini.

---

## 1. Overview Project

Automation test untuk dua portal BSN (Bank Syariah Nasional):
- **Internal**: Portal untuk employee/staff BSN (user management, role, office management)
- **External**: Portal publik untuk nasabah (register, login, beranda, profil akun)

**Stack**: Python + Pytest + Playwright + Allure + uv

---

## 2. URL Penting

| Portal | URL |
|--------|-----|
| Internal Login | `https://terasrumah-sandbox.zegen.app/auth/users/login` |
| Internal Dashboard | `https://terasrumah-sandbox.zegen.app/internal` |
| External (Nasabah) | `https://terasrumah-sandbox.zegen.app` |
| Mailpit (dev email) | `https://mailpit.zegen.app` (Basic Auth: lihat `.env`) |

---

## 3. Cara Login & MFA — PENTING!

Kedua portal menggunakan MFA (OTP via email). Di environment development,
semua email dicegat oleh **Mailpit** — bukan dikirim ke email asli.

**Alur login automation (step-by-step):**
1. Robot isi form email + password → klik Masuk
2. BSN backend kirim email OTP ke Mailpit via SMTP
3. Halaman form OTP muncul di browser ← **sinyal bahwa email sudah ada di Mailpit**
4. Robot hit Mailpit REST API → ambil OTP dari body HTML email (regex `\b\d{6}\b`)
5. Robot isi form OTP → klik Verifikasi → redirect ke dashboard
6. Session disimpan ke `.auth/internal_state.json` (atau `external_state.json`)

**Helper tersedia di `helpers/mailpit.py`** → fungsi `get_otp(recipient_email)` sudah handle semuanya.

**Login fixture bersifat `scope="session"`** → login hanya 1x per pytest run,
semua test pakai session yang sama via `storage_state`.

---

## 4. Struktur Folder

```
Automation Test/
├── .auth/                  ← Session files (gitignored, dibuat otomatis saat runtime)
├── helpers/
│   └── mailpit.py          ← Mailpit helper — shared untuk internal & external
├── pages/
│   ├── internal/           ← Page Objects portal internal (employee)
│   └── external/           ← Page Objects portal external (nasabah)
├── tests/
│   ├── internal/
│   │   ├── conftest.py     ← Login fixture KHUSUS internal (logged_in_internal)
│   │   └── test_*.py
│   └── external/
│       ├── conftest.py     ← Login fixture KHUSUS external (logged_in_external)
│       └── test_*.py
├── conftest.py             ← Root: environment safety guardrail
├── pytest.ini              ← Konfigurasi pytest + markers
├── AGENTS.md               ← File ini
└── .env                    ← Credentials (gitignored — copy dari .env.example)
```

**Filosofi:** `conftest.py` di pytest bersifat hierarkis — fixture internal tidak bocor ke test external dan sebaliknya.

---

## 5. Coding Standards (WAJIB)

Mengikuti **Pedoman Standar Koding Dani** (lihat Obsidian: `Automation/09 - Pedoman Standar Kode Automation`).

### Arsitektur POM (Page Object Model)
- **File Test = BOS**: hanya skenario tingkat tinggi + assertion. Tidak ada detail HTML.
- **File Page = PELAYAN**: semua locator dan action methods di sini.
- Semua elemen statis WAJIB didefinisikan di `__init__` sebagai atribut.
- Alur multi-langkah WAJIB dibungkus jadi satu Action Method.

### Pola AAA di setiap test function
```python
# ARRANGE
# ACT
# ASSERT
```

### Prioritas Locator (urutan wajib)
1. `get_by_role()` ← utama
2. `get_by_text()`
3. `get_by_label()`
4. `get_by_placeholder()`
5. `locator()` dengan class/ID sederhana
6. CSS kompleks / XPath ← jalan terakhir, hindari sebisa mungkin

### Assertion
- Selalu pakai `expect()` dari Playwright
- DILARANG if-else di file test untuk cek kondisi hasil

### Wait Strategy
- Gunakan: `page.wait_for_selector()`, `page.wait_for_url()`, `page.expect_response()`
- **DILARANG KERAS**: `page.wait_for_timeout()`, `time.sleep()`

### Naming Convention (PEP 8)
- File & folder: `snake_case` (misal: `login_page.py`, `test_auth.py`)
- Class: `PascalCase` (misal: `LoginPage`, `RolePage`)
- Fungsi & variabel: `snake_case`

### Docstring
- WAJIB ada di setiap fungsi Page dan fungsi Test (1 baris ringkas)
- Di file test yang pakai `@allure.title`, docstring BOLEH dihapus agar tidak redundan

---

## 6. TC ID Convention

Format: `TC-[PORTAL]-[MODUL]-[NOMOR]`

| Portal | Modul | Contoh ID |
|--------|-------|-----------|
| Internal | AUTH | `TC-INT-AUTH-01` |
| Internal | ROLE | `TC-INT-ROLE-01` |
| Internal | USER | `TC-INT-USER-01` |
| External | AUTH | `TC-EXT-AUTH-01` |
| External | BERANDA | `TC-EXT-BRNDA-01` |
| External | PROFIL | `TC-EXT-PROF-01` |

Dipakai di `@allure.title("[TC-INT-AUTH-01] Judul test case yang deskriptif")`.

---

## 7. Markers

```python
@pytest.mark.smoke      # Fitur kritis, wajib pass sebelum deploy
@pytest.mark.regression # Pengujian menyeluruh + edge cases
```

---

## 8. Perintah Umum

```bash
# Install dependencies
uv sync
uv run playwright install chromium

# Jalankan test (SELALU spesifik saat dev/debug)
uv run pytest tests/internal/test_auth.py::TestAuthInternal::test_login_valid -v  # 1 fungsi
uv run pytest tests/internal/ -m smoke -v                                           # smoke internal
uv run pytest tests/external/ -m smoke -v                                           # smoke external
uv run pytest tests/ -v                                                             # semua

# Dengan Allure report
uv run pytest tests/ --alluredir=allure-results -v
allure serve allure-results
```

---

## 9. Yang DILARANG

- ❌ Hardcode password/credentials di kode — pakai `.env`
- ❌ `time.sleep()` atau `page.wait_for_timeout()` — pakai dynamic wait
- ❌ Locator CSS kompleks / XPath jika ada alternatif semantic
- ❌ If-else di file test untuk cek kondisi hasil
- ❌ Satu test function yang test banyak hal sekaligus (test harus atomic)
- ❌ Assert di file Page Object — assert hanya di file test
- ❌ Commit file `.env` atau `.auth/` ke git

---

## 10. Env Variables

Copy `.env.example` → `.env`, lalu isi nilainya:
```
AUTO_EMAIL_INTERNAL=...
AUTO_PASSWORD_INTERNAL=...
AUTO_EMAIL_EXTERNAL=...
AUTO_PASSWORD_EXTERNAL=...
MAILPIT_URL=https://mailpit.zegen.app
MAILPIT_USER=admin
MAILPIT_PASS=...
```

---

## 11. ⚠️ PERATURAN KERAS: Data Isolation (Data Tumbal)

**DILARANG** memodifikasi atau menghapus data yang sudah ada di sistem (data asli/existing).
Setiap test yang membutuhkan aksi edit atau delete **WAJIB** membuat **data tumbal** terlebih dahulu via API.

### Kenapa?
- Test delete pada data asli → data hilang selamanya jika test berhasil
- Test gagal di tengah → data asli bisa corrupt
- Test harus bisa dijalankan ulang kapanpun tanpa efek samping

### Standar Penamaan Data Uji
Format wajib: `[AUTO-QA] <Nama> <Timestamp>`
Contoh: `[AUTO-QA] Role Auditor 20261026_1100`

Ini memudahkan tim membedakan data robot vs data asli, dan aman dibersihkan sewaktu-waktu.

### Blacklist Master Data (DILARANG disentuh)
- **User**: `Superadmin`, `Terasrumah Admin`, akun PIC QA
- **Role**: `Superadmin`, `Admin`, default system roles
- **Kantor**: `Root`, `Kantor Pusat`

### Cara Buat Data Tumbal via API
```python
@pytest.fixture
def role_tumbal(logged_in_internal: Page):
    """Buat role tumbal via API sebelum test, cleanup setelah test."""
    from datetime import datetime
    nama = f"[AUTO-QA] Role Test {datetime.now().strftime('%Y%m%d_%H%M')}"

    resp = logged_in_internal.request.post(
        "https://terasrumah-sandbox.zegen.app/api/roles",
        data={"name": nama}
    )
    assert resp.ok, f"Gagal buat role tumbal: {resp.text()}"
    role_id = resp.json()["id"]

    yield role_id

    # Teardown: hapus tumbal via API jika masih ada
    logged_in_internal.request.delete(
        f"https://terasrumah-sandbox.zegen.app/api/roles/{role_id}"
    )
```

### Cara Cari API Endpoint (tanpa tanya developer)
1. Buka fitur di browser → isi form → **JANGAN klik Save dulu**
2. Klik kanan → Inspect → tab **Network** → filter Fetch/XHR → clear log
3. Klik Save di UI → lihat request POST/PUT yang muncul
4. Buka tab **Payload** → catat endpoint & body JSON

---

## 12. 🛡️ AI Safety Guardrails & Testing Boundaries

AI yang bekerja di repo ini **WAJIB** mematuhi pagar pembatas berikut:

### Aturan 1 — Environment Lock
- **HANYA** boleh menembak URL yang berlabel `sandbox` atau `localhost`.
- **DILARANG** mengubah `base_url` ke domain lain tanpa izin eksplisit dari user.
- Root `conftest.py` sudah menyertakan autouse fixture yang memblokir run jika target bukan sandbox/local.

### Aturan 2 — Eksekusi Terarah (No Blind/Mass Runs)
- Saat dev/debug, jalankan **spesifik** hingga level 1 fungsi test.
- **DILARANG** menjalankan `uv run pytest` tanpa filter saat sedang debugging.
- **DILARANG** loop pengulangan besar (`--repeat-each=50+`) atau parallel worker banyak tanpa instruksi user.

### Aturan 3 — Anti Fake-Green (Integritas Laporan QA)
- Jika test **FAIL** karena bug aplikasi (misal Error 415), **DILARANG mengubah assertion** agar test jadi pass.
- Biarkan test tetap MERAH, atau gunakan `@pytest.mark.xfail(reason="Bug: ...")` jika diminta user.
- Integritas laporan QA adalah prioritas tertinggi.

### Aturan 4 — Dilarang Self-Healing Otomatis Tanpa Izin
- **JANGAN PERNAH** mengubah locator, selector, atau logika test secara sepihak dan diam-diam ketika test gagal.
- Jika elemen tidak ditemukan atau alur UI berubah:
  1. Hentikan eksekusi dan catat error trace secara lengkap.
  2. Laporkan ke user: elemen apa yang hilang, dugaan penyebabnya (bug UI atau selector usang).
  3. **Tunggu persetujuan user** sebelum mengubah kode/selector apapun.

### Aturan 5 — Pembuatan Modul Baru WAJIB Model Skeleton (Dikosongkan)
- Ketika user meminta membuat Page Object atau Test baru, AI **DILARANG** langsung menebak-nebak locator atau mengisi alur implementasi secara penuh tanpa instruksi eksplisit.
- AI **WAJIB** membuat format **Skeleton (Kerangka Siap Isi)**:
  1. **Page Object**: Mewarisi `BasePage`, atribut locator diberi nilai placeholder atau komentar `# TODO: Dani isi locator`, dan body fungsi aksi diisi `pass` / `# TODO`.
  2. **Test Function**: Menggunakan struktur **AAA (Arrange, Act, Assert)** dengan komentar nomor `1. Arrange`, `2. Act`, `3. Assert` di mana isinya dikosongkan dengan `pass` / `# TODO`.
  3. **Tujuan**: Memberikan ruang belajar bagi user (Dani) untuk mengisi locator dan logika pengujian sendiri setelah melakukan inspeksi/reconnaisance UI langsung.
