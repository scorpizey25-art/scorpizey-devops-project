# Proyek DevOps: Membangun Lingkungan Pengembangan Lokal

### Deskripsi
Dokumen ini merangkum langkah-langkah yang diambil untuk menyiapkan lingkungan pengembangan DevOps lokal menggunakan Windows Subsystem for Linux (WSL). Lingkungan ini berfungsi sebagai pondasi untuk proyek-proyek otomatisasi, containerization, dan cloud di masa depan.

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

---

### Rencana Selanjutnya

-   [ ] Instalasi dan konfigurasi Git.
-   [ ] Instalasi Python.
-   [ ] Memulai proyek pertama: Alat Otomasi Pencadangan File.