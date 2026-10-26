# Test Cases: Autentikasi — Portal Internal BSN

> Berdasarkan standar Test Case Template (`tc_template.md`).

---

## [TC-INT-AUTH-01] Melakukan login menggunakan data yang valid
* **Module:** Internal
* **Sub Menu:** Autentikasi
* **Description:** Positive Case
* **Priority:** Critical

### Steps:
1. Masuk ke halaman Login Internal BSN.
2. Mengisi field Email dengan data valid.
3. Mengisi field Password dengan data valid.
4. Klik button Masuk ke Akun BSN.
5. Mengisi 6 kotak kode OTP dari Mailpit.
6. Klik button Lanjutkan.

### Expected Results:
1. Berhasil membuka halaman Login Internal BSN.
2. Berhasil mengisi field Email.
3. Berhasil mengisi field Password.
4. Berhasil menampilkan form verifikasi OTP Konfirmasi Identitas.
5. Berhasil mengisi 6 kotak kode OTP.
6. Berhasil masuk ke halaman Dashboard Internal BSN.

---

## [TC-INT-AUTH-02] Melakukan logout dari aplikasi
* **Module:** Internal
* **Sub Menu:** Autentikasi
* **Description:** Positive Case
* **Priority:** High

### Steps:
1. Klik dropdown profil pengguna.
2. Klik menu Keluar.

### Expected Results:
1. Berhasil membuka dropdown profil pengguna.
2. Berhasil logout dan diarahkan kembali ke halaman Login Internal.

---

## [TC-INT-AUTH-03] Mengklik button 'Masuk dengan akun lain' pada halaman Konfirmasi Identitas
* **Module:** Internal
* **Sub Menu:** Autentikasi
* **Description:** Positive Case
* **Priority:** Normal

### Steps:
1. Klik button Masuk dengan akun lain.

### Expected Results:
1. Berhasil kembali ke tampilan form input email dan kata sandi awal.

---

## [TC-INT-AUTH-04] Mengklik button 'Halaman Utama' pada tampilan sesi berakhir
* **Module:** Internal
* **Sub Menu:** Autentikasi
* **Description:** Positive Case
* **Priority:** Normal

### Steps:
1. Klik button Halaman Utama.

### Expected Results:
1. Berhasil diarahkan ke halaman Login Internal BSN.
