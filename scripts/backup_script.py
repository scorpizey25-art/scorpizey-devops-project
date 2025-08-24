#!/usr/bin/env python3

import shutil
import os

# Tentukan direktori sumber dan tujuan
# os.path.expanduser('~') adalah cara aman untuk mendapatkan home directory Linux
source_dir = os.path.expanduser('~/my-devops-project/src')
destination_dir = os.path.expanduser('~/my-devops-project/backup')

# Buat direktori tujuan jika belum ada
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

print(f"Memulai proses pencadangan dari {source_dir} ke {destination_dir}")

try:
    # Menyalin isi direktori secara rekursif
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    print("Pencadangan berhasil!")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")