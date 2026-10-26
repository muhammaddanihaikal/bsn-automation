# BSN Automation Test

Automation test untuk BSN Portal Internal & External menggunakan Python + Pytest + Playwright + Allure.

**Repo**: https://github.com/muhammaddanihaikal/bsn-automation

## Setup

```bash
# 1. Copy env dan isi credentials
copy .env.example .env

# 2. Install dependencies
uv sync

# 3. Install Playwright browser
uv run playwright install chromium
```

## Jalankan Test

```bash
# Internal smoke test
uv run pytest tests/internal/ -m smoke -v

# External smoke test
uv run pytest tests/external/ -m smoke -v

# Semua test
uv run pytest tests/ -v

# Spesifik file / fungsi
uv run pytest tests/internal/test_auth.py::TestAuthInternal::test_login_valid -v

# Dengan Allure report
uv run pytest tests/ --alluredir=allure-results -v
allure serve allure-results
```

## Struktur Folder

```
├── helpers/            Shared utilities (Mailpit OTP helper)
├── pages/
│   ├── internal/       Page Objects portal internal (employee)
│   └── external/       Page Objects portal external (nasabah)
├── tests/
│   ├── internal/       Test cases portal internal
│   └── external/       Test cases portal external
├── conftest.py         Root: safety guardrail (environment lock)
├── pytest.ini          Konfigurasi pytest
├── AGENTS.md           Panduan untuk AI assistant
└── .env.example        Template environment variables
```

> ⚠️ Baca `AGENTS.md` sebelum melakukan perubahan apapun.
