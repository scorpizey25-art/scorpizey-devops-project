
*   **`src/`**: Folder untuk kode aplikasi utama.
*   **`scripts/`**: Folder untuk semua script otomatisasi (Python, Bash, dll.).
*   **`infra/`**: Folder untuk kode infrastruktur (Terraform, Ansible, dll.).
*   **`docs/`**: Folder untuk dokumentasi teknis yang lebih mendalam.

### Progres Harian: Sabtu, 23 Agustus 2025

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

### Progres Harian: Minggu, 24 Agustus 2025

**Tujuan**
Hari ini, kami berfokus untuk menerapkan alur kerja _**feature branching**_ yang merupakan praktik standar industri. Tujuannya adalah untuk bekerja pada fitur baru (`skrip backup`) secara terisolasi sebelum menggabungkannya ke _branch_ utama (`main`).

**Langkah-langkah yang Dilakukan**
1.  Membuat _branch_ fitur baru: `git checkout -b fitur/backup-otomasi`.
2.  Menambahkan _file_ `backup_script.py` dan melakukan _commit_ pertama di _branch_ fitur.
3.  Berhasil melakukan _push_ pertama dari _branch_ fitur ke GitHub.
4.  Berpindah ke _branch_ utama (`main`) dengan `git checkout main`.
5.  Menggabungkan _branch_ fitur ke _branch_ utama dengan `git merge fitur/backup-otomasi`.
6.  Mengunggah (_push_) hasil _merge_ ke _remote_ (`main`) dengan `git push origin main`.
7.  Menghapus _branch_ fitur lokal dengan `git branch -d fitur/backup-otomasi`.
8.  Menghapus _branch_ fitur dari _remote_ dengan `git push origin --delete fitur/backup-otomasi`.

**Pencapaian**
* Berhasil membuat _branch_ fitur baru (`fitur/backup-otomasi`) untuk pengembangan.
* Melakukan _commit_ pertama dari skrip Python di _branch_ fitur.
* Berhasil menggabungkan (_merge_) perubahan dari _branch_ fitur ke _branch_ utama (`main`).
* Berhasil menghapus _branch_ fitur dari repositori lokal dan _remote_ setelah digabungkan.

**Masalah/Kendala**
* **Masalah:** Terdapat kesalahan pengetikan saat membuat _branch_ fitur, yang mengakibatkan terbentuknya dua _branch_ yang berbeda.
* **Solusi:** Mengatasi masalah pengetikan _branch_ dengan menghapus _branch_ yang salah menggunakan perintah `git branch -d`.
* **Masalah:** Terjadi kebingungan mengenai _file_ yang sudah di-_merge_ secara lokal namun tidak langsung muncul di _repository_ _remote_.
* **Solusi:** Memahami bahwa `git push` diperlukan untuk menyinkronkan perubahan dari _repository_ lokal ke _repository_ _remote_.

**Kesimpulan**
Semua fondasi sudah lengkap. Lingkungan pengembangan, _tools_, dan alur kerja Git sudah siap dan terverifikasi. Kami sekarang siap untuk melanjutkan ke tahap _coding_ fungsional.

---

### Rencana Selanjutnya

-   [x] Instalasi dan konfigurasi Git.
-   [x] Instalasi Python.
-   [ ] Memulai proyek pertama: Alat Otomasi Pencadangan File.

Setelah Anda memperbarui file README.md tersebut di VS Code, jangan lupa untuk menyimpan dan mengunggahnya dengan commit baru.
Bash

git add README.md
git commit -m "docs: menambahkan progres harian dan ringkasan"
git push origin main


Gemini dapat membuat kesalahan, jadi periksa kembali responsnya