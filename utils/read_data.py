import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def read_data(file_name: str) -> dict:
    """Membaca file JSON dari folder data/ dan mengembalikannya sebagai dict."""
    file_path = DATA_DIR / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"File data tidak ditemukan: {file_path}")

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)
