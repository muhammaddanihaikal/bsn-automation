# Test Cases: Manajemen Pengguna — Portal Internal BSN

> Berdasarkan standar Test Case Template (`tc_template.md`).

---

## [TC-INT-USER-01] Membuka halaman Manajemen Pengguna
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Positive Case
* **Priority:** High

### Steps:
1. Klik menu Manajemen Pengguna pada Sidebar/Navbar.

### Expected Results:
1. Berhasil membuka halaman Manajemen Pengguna.

---

## [TC-INT-USER-02] Menampilkan daftar data Pengguna
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Positive Case
* **Priority:** High

### Steps:
1. Menampilkan daftar data pengguna pada tabel.

### Expected Results:
1. Berhasil menampilkan tabel data pengguna beserta kolom informasi.

---

## [TC-INT-USER-03] Menambahkan data Pengguna
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Positive Case
* **Priority:** Critical

### Steps:
1. Klik button Tambah Pengguna.
2. Mengisi semua field mandatory.
3. Klik button Simpan.

### Expected Results:
1. Berhasil membuka form Tambah Pengguna.
2. Berhasil mengisi semua field mandatory.
3. Berhasil menambahkan data Pengguna dan menampilkan notifikasi sukses.

---

## [TC-INT-USER-04] Menambahkan data Pengguna tanpa mengisi field mandatory
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Negative Case
* **Priority:** Normal

### Steps:
1. Klik button Tambah Pengguna.
2. Mengosongkan semua field mandatory.
3. Klik button Simpan.

### Expected Results:
1. Berhasil membuka form Tambah Pengguna.
2. Berhasil mengosongkan field mandatory.
3. Berhasil menampilkan pesan error validasi pada field wajib.

---

## [TC-INT-USER-05] Mengubah data Pengguna
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Positive Case
* **Priority:** Critical

### Steps:
1. Klik button Edit pada baris pengguna yang dipilih.
2. Mengubah data pada form Edit Pengguna.
3. Klik button Perbarui.

### Expected Results:
1. Berhasil membuka form Edit Pengguna.
2. Berhasil mengubah data pengguna.
3. Berhasil memperbarui data Pengguna dan menampilkan notifikasi sukses.

---

## [TC-INT-USER-06] Menghapus data Pengguna
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Positive Case
* **Priority:** Critical

### Steps:
1. Klik button Hapus pada baris pengguna yang dipilih.
2. Klik button Ya, Hapus pada popup konfirmasi.

### Expected Results:
1. Berhasil menampilkan popup konfirmasi hapus data.
2. Berhasil menghapus data Pengguna dan data tidak lagi muncul di tabel.

---

## [TC-INT-USER-07] Mencari data Pengguna dengan keyword valid
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Positive Case
* **Priority:** High

### Steps:
1. Mengisi field pencarian dengan nama pengguna yang valid.
2. Klik button Cari.

### Expected Results:
1. Berhasil mengisi field pencarian.
2. Berhasil menampilkan data pengguna yang sesuai dengan kata kunci pencarian.

---

## [TC-INT-USER-08] Mencari data Pengguna dengan keyword tidak valid
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Negative Case
* **Priority:** Normal

### Steps:
1. Mengisi field pencarian dengan keyword yang tidak terdaftar.
2. Klik button Cari.

### Expected Results:
1. Berhasil mengisi field pencarian.
2. Berhasil menampilkan pesan data tidak ditemukan.

---

## [TC-INT-USER-09] Melakukan filter data Pengguna
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Positive Case
* **Priority:** Normal

### Steps:
1. Memilih opsi status pada filter.
2. Klik button Cari.

### Expected Results:
1. Berhasil memilih opsi filter.
2. Berhasil menampilkan daftar pengguna sesuai dengan filter status yang dipilih.

---

## [TC-INT-USER-10] Mereset filter Pengguna
* **Module:** Internal
* **Sub Menu:** Manajemen Pengguna
* **Description:** Positive Case
* **Priority:** Normal

### Steps:
1. Klik button Reset.

### Expected Results:
1. Berhasil mereset seluruh opsi filter ke kondisi awal dan memuat kembali semua data.
