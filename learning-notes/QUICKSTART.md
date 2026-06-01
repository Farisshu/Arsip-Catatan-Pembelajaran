# 🚀 Quick Start Guide

Panduan cepat untuk mulai menggunakan repository ini.

---

## 1️⃣ Langkah Awal

### Setelah Menjalankan Script

```bash
# 1. Lihat struktur yang dibuat
tree -L 3 learning-notes

# 2. Buka dashboard utama
code learning-notes/README.md  # atau editor favoritmu

# 3. Inisialisasi Git (jika belum)
cd learning-notes
git init
git add .
git commit -m "Initial setup: struktur belajar Teknik Elektronika & Kendali"
```

---

## 2️⃣ Mulai Mengisi Catatan

### Opsi A: Mulai dari Semester Tertentu

1. Buka folder `semesters/{tahun}/{kode-matkul}/README.md`
2. Edit bagian:
   - 🗺️ **Peta Topik**: Sesuaikan mindmap dengan pemahamanmu
   - 📌 **Fokus Belajar**: Tentukan prioritas minggu ini
   - 📐 **Konsep & Rumus**: Tulis dengan LaTeX
   - ❓ **Catatan Pertanyaan**: Jangan ragu mencatat hal yang belum dipahami

### Opsi B: Mulai dari Topik Lintas-Matkul

1. Buka folder `topics/`
2. Pilih topik yang menarik atau buat folder baru
3. Hubungkan ke mata kuliah terkait dengan link relatif

### Opsi C: Buat Jalur Belajarmu Sendiri

Repository ini fleksibel! Kamu bisa:
- Membuat folder `deep-dive/` untuk eksplorasi mendalam
- Membuat folder `project-integration/` untuk proyek gabungan
- Menambah file markdown di mana saja

---

## 3️⃣ Tips Efektif

### ✍️ Menulis Catatan yang Baik

- **Gunakan bahasa sendiri**: Jangan copy-paste dari buku
- **Tambahkan contoh**: Rumus tanpa aplikasi sulit dipahami
- **Buat koneksi**: "Oh, ini mirip dengan konsep X di matkul Y!"
- **Review berkala**: Update checklist fokus belajar setiap minggu

### 🔗 Memanfaatkan Link Internal

```markdown
[Lihat konsep Op-Amp](../../2024-2/REC242002-elektronika-analog-1/README.md#konsep-kunci)
[Balik ke dashboard](../../README.md)
[Lanjut ke topik Fourier](../../topics/fourier-transform/README.md)
```

### 📊 Visualisasi dengan Mermaid

Semua diagram di atas bisa kamu edit langsung di Markdown. GitHub akan merendernya otomatis!

---

## 4️⃣ Sync ke GitHub

```bash
# Commit perubahan rutin
git add .
git commit -m "Update: catatan Elektronika Analog + soal latihan"

# Push ke remote (buat repo private jika ingin privasi)
git remote add origin https://github.com/username/repo-name.git
git push -u origin main

# Pull di device lain
git clone https://github.com/username/repo-name.git
```

---

## 5️⃣ Update Daftar Mata Kuliah

Jika ada penambahan/revisi mata kuliah:

1. Edit file `config_kuliah.json`
2. Jalankan ulang script ini (aman, tidak menimpa catatan yang sudah diisi)
3. Folder baru akan ditambahkan, folder lama tetap utuh

---

## ❓ FAQ

**Q: Apakah harus mengisi semua mata kuliah sekaligus?**  
A: Tidak! Mulai dari 1-2 matkul yang paling menarik atau paling mendesak.

**Q: Bolehkah mengubah struktur folder?**  
A: Sangat boleh! Ini ruang belajarmu. Script hanya memberikan starting point.

**Q: Bagaimana cara backup?**  
A: Gunakan GitHub Private Repository atau sync ke cloud storage (Google Drive, Dropbox).

**Q: Bisa kolaborasi dengan teman?**  
A: Bisa! Tapi hati-hati dengan merge conflict. Lebih baik masing-masing punya repo sendiri.

---

**Selamat belajar! 🎓**

_Jangan lupa: konsistensi > intensitas. Lebih baik 30 menit setiap hari daripada 5 jam sekali seminggu._
