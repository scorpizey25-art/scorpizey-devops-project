
*   **`src/`**: Folder untuk kode aplikasi utama.
*   **`scripts/`**: Folder untuk semua script otomatisasi (Python, Bash, dll.).
*   **`infra/`**: Folder untuk kode infrastruktur (Terraform, Ansible, dll.).
*   **`docs/`**: Folder untuk dokumentasi teknis yang lebih mendalam.

---

### Progres Tahap 1: Persiapan Lingkungan Dasar

**1. Instalasi Windows Subsystem for Linux (WSL)**
* **Tujuan:** Menginstal lapisan kompatibilitas yang memungkinkan eksekusi biner Linux secara langsung di Windows, menyediakan lingkungan terminal yang otentik.
* **Langkah yang Dilakukan:** Menggunakan perintah `wsl --install` di PowerShell.

**2. Konfigurasi Sistem Ubuntu Linux**
* **Tujuan:** Menyelesaikan instalasi Ubuntu di dalam WSL dan mengonfigurasi user account default untuk operasi harian.
* **Langkah yang Dilakukan:** Membuat user account `scorpizey` dan menetapkan password.

**3. Pembaruan Sistem Operasi**
* **Tujuan:** Memastikan semua paket sistem operasi terbaru terinstal untuk menjaga keamanan dan stabilitas.
* **Langkah yang Dilakukan:** Menjalankan perintah `sudo apt update && sudo apt upgrade` di terminal Ubuntu.

**4. Instalasi dan Konfigurasi Git**
* **Tujuan:** Menginstal sistem kontrol versi Git dan menghubungkan repositori lokal ke repositori remote di GitHub.
* **Langkah yang Dilakukan:**
    1.  Menginstal Git di Ubuntu dengan `sudo apt install git`.
    2.  Mengonfigurasi identitas pengguna global dengan `git config --global`.
    3.  Membuat repositori baru di GitHub.
    4.  Menghubungkan repositori lokal ke remote dengan `git remote add origin`.
    5.  Membuat Personal Access Token (PAT) di GitHub untuk otentikasi.
    6.  Melakukan _commit_ pertama yang berisi dokumentasi awal.
    7.  Berhasil melakukan `git push` pertama ke branch `main` di GitHub.

---

### Kendala dan Solusi

Selama proses ini, beberapa kendala teknis ditemui. Berikut adalah rincian masalah dan solusi yang diterapkan:

**1. Kendala: `git push` Gagal karena Branch `main` Tidak Ditemukan**
* **Masalah:** Perintah `git push origin main` gagal dengan pesan error `src refspec main does not match any`. Ini terjadi karena branch default di repositori lokal adalah `master`, bukan `main`.
* **Solusi:** Mengubah nama branch lokal dari `master` menjadi `main` menggunakan perintah `git branch -m master main`. Ini menyelaraskan nama branch dengan standar industri saat ini.

**2. Kendala: Otentikasi Gagal saat `git push`**
* **Masalah:** Proses `git push` gagal dengan pesan error `Password authentication is not supported`. Ini karena GitHub tidak lagi mengizinkan penggunaan password akun untuk otentikasi dari terminal.
* **Solusi:** Membuat **Personal Access Token (PAT)** di GitHub dengan izin (`scopes`) yang sesuai (`repo`, `workflow`). PAT ini kemudian digunakan sebagai pengganti password saat terminal memintanya, sehingga otentikasi berhasil.

---

### Rencana Selanjutnya

-   [x] Instalasi dan konfigurasi Git.
-   [ ] Instalasi Python.
-   [ ] Memulai proyek pertama: Alat Otomasi Pencadangan File.