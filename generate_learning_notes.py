#!/usr/bin/env python3
"""
Script untuk menghasilkan struktur folder dan template Markdown
untuk arsip catatan belajar pribadi Teknik Elektronika & Kendali.

Fitur:
- Struktur folder fleksibel per semester & mata kuliah
- Template README dengan Mermaid, LaTeX, checklist
- File konfigurasi JSON untuk mudah update daftar matkul
- .gitignore aman untuk proyek teknik
- Root README dengan navigasi visual dan grafik alur belajar
"""

import json
from pathlib import Path
from datetime import datetime

# =============================================================================
# KONFIGURASI DAFTAR MATA KULIAH (Edit di sini atau load dari JSON eksternal)
# =============================================================================

DATA_KULIAH = {
    "2024-1": [
        {"kode": "REC241001", "nama": "Fisika Elektronika", "kategori": "Dasar"},
        {"kode": "REC241002", "nama": "Praktikum Fisika Elektronika", "kategori": "Praktikum"},
        {"kode": "REC241003", "nama": "Matematika 1", "kategori": "Dasar"},
        {"kode": "REC241004", "nama": "K3 (Keselamatan & Kesehatan Kerja)", "kategori": "Dasar"},
        {"kode": "REC241005", "nama": "Rangkaian Listrik 1", "kategori": "Inti"},
        {"kode": "REC241006", "nama": "Praktikum Rangkaian Listrik 1", "kategori": "Praktikum"},
        {"kode": "REC241007", "nama": "Bengkel Mekanik", "kategori": "Praktikum"},
        {"kode": "REC241008", "nama": "Algoritma Pemrograman", "kategori": "Dasar"},
    ],
    "2024-2": [
        {"kode": "REC242001", "nama": "Rangkaian Listrik 2", "kategori": "Inti"},
        {"kode": "REC242002", "nama": "Elektronika Analog 1", "kategori": "Inti"},
        {"kode": "REC242003", "nama": "Bengkel Elektronika", "kategori": "Praktikum"},
        {"kode": "REC242004", "nama": "Sensor & Aktuator", "kategori": "Inti"},
        {"kode": "REC242005", "nama": "Teknik Digital 1", "kategori": "Inti"},
        {"kode": "REC242006", "nama": "Matematika 2", "kategori": "Dasar"},
        {"kode": "REC242007", "nama": "Gambar Teknik", "kategori": "Dasar"},
    ],
    "2025-1": [
        {"kode": "REC243001", "nama": "Elektronika Analog 2", "kategori": "Inti"},
        {"kode": "REC243002", "nama": "Sistem Mikrokontroler", "kategori": "Spesialisasi"},
        {"kode": "REC243003", "nama": "Instrumentasi Industri", "kategori": "Spesialisasi"},
        {"kode": "REC243004", "nama": "PLC", "kategori": "Spesialisasi"},
        {"kode": "REC243005", "nama": "Sistem Kendali Kontinyu", "kategori": "Spesialisasi"},
        {"kode": "REC243006", "nama": "Elektronika Digital", "kategori": "Inti"},
    ],
}

# =============================================================================
# TEMPLATE MARKDOWN
# =============================================================================

TEMPLATE_README_MAKUL = """# {nama_matkul} ({kode})
> Bidang: {kategori} | Target Pemahaman: _Saya isi sendiri_

---

## 🗺️ Peta Topik

```mermaid
mindmap
  root(({nama_singkat}))
    Topik A
      Subtopik A.1
      Subtopik A.2
    Topik B
      Subtopik B.1
```

> 💡 **Tips**: Edit mindmap di atas sesuai pemahamanmu. Tambahkan cabang baru saat mempelajari konsep tambahan.

---

## 📌 Fokus Belajar Saat Ini

- [ ] Topik prioritas pertama
- [ ] Topik prioritas kedua
- [ ] Latihan soal terkait
- [ ] Review konsep yang belum dipahami

---

## 📐 Konsep & Rumus Kunci

> Saya tulis rumus, derivasi, atau penjelasan konsep di sini.

### Contoh Format Rumus LaTeX

$$ \\int x \\, dx = 0.5 x^2 + C $$

$$ V = I \\cdot R $$

$$ H(s) = \\frac{{Y(s)}}{{X(s)}} = \\frac{{b_0}}{{a_n s^n + a_{{n-1}} s^{{n-1}} + \\dots + a_0}} $$

### Catatan Konsep

| Konsep | Penjelasan | Contoh Aplikasi |
|--------|------------|-----------------|
| ...    | ...        | ...             |

---

## 🔧 Praktikum / Simulasi

### Eksperimen Pertama: _Judul Percobaan_

- [ ] Skema rangkaian / flowchart
- [ ] Kode program / pseudocode
- [ ] Hasil pengamatan & analisis

```python
# Contoh kode simulasi
def contoh_fungsi():
    pass
```

### Hasil Pengamatan

| Variabel | Nilai | Satuan | Keterangan |
|----------|-------|--------|------------|
| ...      | ...   | ...    | ...        |

---

## ❓ Catatan Pertanyaan & Insight

> Tempat mencatat: "Kenapa begini?", "Bagaimana jika...?", "Hubungan dengan topik X?"

- 🔍 **Pertanyaan**: Mengapa tegangan output tidak stabil?
- 💡 **Insight**: Ternyata ada pengaruh temperatur pada komponen semiconductor.
- 🔗 **Koneksi ke topik lain**: Lihat juga di [Sensor & Aktuator](../../2024-2/REC242004-sensor-aktuator/README.md)

---

## 🔗 Referensi Saya

### Buku
- [ ] _Judul Buku_, Penulis, Tahun

### Video
- [ ] [Judul Video](URL)

### Datasheet / Manual
- [ ] [Nama Komponen](URL)

### Link Eksternal
- [ ] [Artikel / Tutorial](URL)

---

## 🔄 Riwayat Update

| Tanggal | Perubahan |
|---------|-----------|
| {tanggal} | Initial setup |

---

**[⬅️ Kembali ke Dashboard Semester](../README.md)** | **[🏠 Ke Dashboard Utama](../../README.md)**
"""

TEMPLATE_README_SEMESTER = """# Semester {semester} - {tahun_akademik}

> 📚 Daftar mata kuliah dan progres belajar semester ini.

---

## 📊 Ringkasan Semester

| Kode | Mata Kuliah | Kategori | Status |
|------|-------------|----------|--------|
{tabel_matkul}

> ✅ **Status**: Isi manual sesuai progresmu (Belum Mulai / Dalam Proses / Dipahami / Perlu Review)

---

## 🗺️ Alur Belajar Semester Ini

```mermaid
graph LR
  subgraph Dasar
    A[Matematika] --> B[Fisika]
    B --> C[Rangkaian Listrik]
  end
  
  subgraph Inti
    C --> D[Elektronika Analog]
    C --> E[Teknik Digital]
    D --> F[Sensor & Aktuator]
  end
  
  subgraph Praktikum
    G[Lab Fisika] --> H[Lab Rangkaian]
    H --> I[Bengkel Elektronika]
  end
```

---

## 🎯 Target Pembelajaran Semester Ini

1. **Pemahaman Konsep**: Kuasai fondasi teori di setiap mata kuliah
2. **Keterampilan Praktis**: Selesaikan minimal 1 proyek kecil per matkul praktikum
3. **Koneksi Antar Topik**: Identifikasi hubungan antara mata kuliah (misal: Matematika → Rangkaian → Kontrol)

---

## 📁 Struktur Folder

```
{semester}/
├── {folder_matkul_1}/
│   ├── README.md       # Template belajar fleksibel
│   ├── notes/          # Catatan harian, konsep, ringkasan
│   ├── problems/       # Soal latihan & pembahasan
│   ├── labs/           # Laporan praktikum, skema, hasil simulasi
│   └── references/     # Link buku, video, paper, datasheet
├── ...
└── (lihat navigasi cepat di bawah)
```

---

## 🔗 Navigasi Cepat

{link_matkul}

---

**[⬅️ Kembali ke Dashboard Utama](../../README.md)** | **[➡️ Lanjut ke Topik Lintas-Matkul](../../topics/README.md)**
"""

TEMPLATE_README_ROOT = """# 📘 Personal Learning Archive — M Faris

> _"Belajar bukan tentang menghafal, tapi tentang memahami pola dan membangun koneksi."_

---

## 🎯 Tentang Repository Ini

Repository ini adalah **arsip catatan belajar pribadi** untuk bidang **Teknik Elektronika & Kendali**. 
Dibuat sebagai ruang fleksibel untuk:
- 📝 Mencatat konsep, rumus, dan insight
- 🔬 Mendokumentasikan eksperimen dan simulasi
- 🧩 Menghubungkan antar topik lintas mata kuliah
- 📈 Melacak progres pemahaman secara mandiri

> ⚠️ **Bukan portofolio nilai** — tidak ada IPK, status kelulusan, atau target akademik formal.

---

## 🗺️ Peta Belajar Besar

```mermaid
graph LR
  subgraph Fondasi
    A1[Matematika 1-2] --> A2[Fisika Elektronika]
    A2 --> A3[Rangkaian Listrik 1-2]
    A3 --> A4[Algoritma Pemrograman]
  end
  
  subgraph "Inti Keilmuan"
    A3 --> B1[Elektronika Analog 1-2]
    A3 --> B2[Teknik Digital 1]
    B2 --> B3[Elektronika Digital]
    B1 --> B4[Sensor & Aktuator]
  end
  
  subgraph "Sistem & Kendali"
    B4 --> C1[Sistem Mikrokontroler]
    B4 --> C2[Instrumentasi Industri]
    C1 --> C3[PLC]
    C1 --> C4[Sistem Kendali Kontinyu]
  end
  
  subgraph "Praktikum & Bengkel"
    D1[Praktikum Fisika] --> D2[Praktikum Rangkaian]
    D2 --> D3[Bengkel Mekanik]
    D3 --> D4[Bengkel Elektronika]
  end
  
  A1 -.-> B1
  B1 -.-> C1
  C1 -.-> C3
```

---

## 📚 Navigasi Per Semester

| Semester | Tahun Akademik | Jumlah Matkul | Link |
|----------|----------------|---------------|------|
{tabel_semester}

---

## 🔍 Topik Lintas-Matkul

Jelajahi topik yang menghubungkan beberapa mata kuliah sekaligus:

- ⚡ **Fourier Transform**: Matematika 2 → Elektronika Analog → Sistem Kendali
- 🔁 **PID Control**: Rangkaian Listrik → Sistem Kendali → PLC
- 💻 **Embedded Systems**: Algoritma → Mikrokontroler → Instrumentasi
- 📡 **Signal Processing**: Elektronika Digital → Sensor → Kendali

👉 **[Lihat semua topik lintas-matkul](topics/README.md)**

---

## 🛠️ Cara Menggunakan Repository Ini

1. **Pilih starting point**: Mulai dari semester mana saja atau topik yang paling menarik
2. **Isi template fleksibel**: Setiap mata kuliah punya struktur yang bisa kamu sesuaikan
3. **Buat koneksi**: Gunakan link internal untuk menghubungkan konsep antar matkul
4. **Update progres**: Checklist dan mindmap bisa diedit kapan saja

📖 **[Panduan lengkap](QUICKSTART.md)**

---

## 🔄 Update Terakhir

| Tanggal | Perubahan |
|---------|-----------|
| {tanggal} | Initial setup oleh script |

---

## 📬 Kontak & Kolaborasi

Repository ini bersifat **pribadi**, tapi jika kamu ingin berdiskusi atau berbagi sumber belajar:

- 📧 Email: _[isi sendiri]_
- 💬 GitHub Issues: _Untuk diskusi terbuka (opsional)_

---

_Dibuat dengan ❤️ untuk perjalanan belajar mandiri di Teknik Elektronika & Kendali_
"""

TEMPLATE_README_TOPICS = """# 🧩 Topik Lintas-Matkul

> Koleksi topik yang menghubungkan konsep dari berbagai mata kuliah.

---

## 📋 Daftar Topik

| Topik | Mata Kuliah Terkait | Status |
|-------|---------------------|--------|
| Transformasi Fourier | Matematika 2, Elektronika Analog, Sistem Kendali | 🟡 Dalam Proses |
| PID Control | Rangkaian Listrik, Sistem Kendali, PLC | ⚪ Belum Mulai |
| Embedded Systems | Algoritma, Mikrokontroler, Instrumentasi | ⚪ Belum Mulai |
| Signal Conditioning | Sensor & Aktuator, Elektronika Analog, Instrumentasi | ⚪ Belum Mulai |

---

## 🗺️ Peta Koneksi Topik

```mermaid
graph TD
  A[Transformasi Fourier] --> B[Analisis Frekuensi]
  A --> C[Filter Design]
  
  D[PID Control] --> E[Stabilitas Sistem]
  D --> F[Tuning Parameter]
  
  G[Embedded Systems] --> H[Real-time Programming]
  G --> I[Hardware-Software Integration]
```

---

## 📝 Template Topik Baru

### Nama Topik

**Mata Kuliah Terkait:**
- Matkul 1
- Matkul 2

**Konsep Kunci:**
- Konsep A
- Konsep B

**Aplikasi:**
- Deskripsi aplikasi di dunia nyata

**Referensi:**
- [Link 1]()
- [Link 2]()

---

**[⬅️ Kembali ke Dashboard Utama](../README.md)**
"""

TEMPLATE_QUICKSTART = """# 🚀 Quick Start Guide

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
"""

GITIGNORE_CONTENT = """# === Files to Ignore for Engineering Learning Notes ===

# Binary & Document files (keep source, not compiled/exported)
*.pdf
*.docx
*.doc
*.pptx
*.ppt
*.xlsx
*.xls

# Build artifacts
build/
dist/
*.o
*.so
*.exe
*.out

# Python cache & virtual environments
__pycache__/
*.py[cod]
*$py.class
.Python
venv/
env/
.env
*.egg-info/

# IDE & Editor
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Logs & temporary files
*.log
tmp/
temp/
*.tmp

# Large files (>50MB should be stored elsewhere)
*.iso
*.img
*.bin
*.hex
firmware/*.bin
firmware/*.hex

# Simulation project files (keep only reports, not entire projects)
*.psproj
*.asc
*.raw
*.trn
*.log

# Jupyter checkpoints
.ipynb_checkpoints/

# OS generated files
Thumbs.db
ehthumbs.db
Desktop.ini

# Secrets & credentials (important!)
*.key
*.pem
credentials.json
secrets.yaml
.env.local
"""

# =============================================================================
# FUNGSI HELPER
# =============================================================================

def slugify(text):
    """Ubah teks menjadi slug lowercase dengan hyphen."""
    return text.lower().replace(" ", "-").replace("&", "dan").replace("(", "").replace(")", "")

def generate_folder_name(kode, nama):
    """Generate nama folder: KODE-nama-lowercase."""
    return f"{kode}-{slugify(nama)}"

def create_readme_matkul(kode, nama, kategori, tanggal):
    """Generate konten README untuk satu mata kuliah."""
    nama_singkat = "".join(word[0].upper() for word in nama.split() if word[0].isalpha())[:8]
    
    return TEMPLATE_README_MAKUL.format(
        nama_matkul=nama,
        kode=kode,
        kategori=kategori,
        nama_singkat=nama_singkat,
        tanggal=tanggal
    )

def create_readme_semester(semester, tahun, matkul_list):
    """Generate konten README untuk satu semester."""
    # Tabel matkul
    tabel_rows = []
    for m in matkul_list:
        folder = generate_folder_name(m["kode"], m["nama"])
        tabel_rows.append(
            f"| {m['kode']} | [{m['nama']}](./{folder}/README.md) | {m['kategori']} | ⚪ Belum Mulai |"
        )
    tabel_matkul = "\n".join(tabel_rows)
    
    # Link navigasi
    links = []
    for m in matkul_list:
        folder = generate_folder_name(m["kode"], m["nama"])
        links.append(f"- 📘 [{m['nama']}](./{folder}/README.md)")
    link_matkul = "\n".join(links)
    
    # Folder pertama untuk preview struktur
    folder_matkul_1 = generate_folder_name(matkul_list[0]["kode"], matkul_list[0]["nama"]) if matkul_list else "..."
    
    return TEMPLATE_README_SEMESTER.format(
        semester=semester,
        tahun_akademik=tahun,
        tabel_matkul=tabel_matkul,
        link_matkul=link_matkul,
        folder_matkul_1=folder_matkul_1
    )

def create_readme_root(tanggal):
    """Generate konten README root."""
    tabel_semester_rows = []
    for semester, matkul_list in DATA_KULIAH.items():
        tahun = semester.replace("-", " / ")
        jumlah = len(matkul_list)
        tabel_semester_rows.append(
            f"| {semester} | {tahun} | {jumlah} | [Lihat matkul](./semesters/{semester}/README.md) |"
        )
    tabel_semester = "\n".join(tabel_semester_rows)
    
    return TEMPLATE_README_ROOT.format(
        tanggal=tanggal,
        tabel_semester=tabel_semester
    )

# =============================================================================
# FUNGSI UTAMA
# =============================================================================

def main():
    """Fungsi utama untuk generate struktur folder dan template."""
    
    # Setup root directory
    root_dir = Path("learning-notes")
    root_dir.mkdir(exist_ok=True)
    
    tanggal_sekarang = datetime.now().strftime("%Y-%m-%d")
    
    print("🚀 Memulai pembuatan struktur learning notes...\n")
    
    # Counter untuk statistik
    total_folders = 0
    total_files = 0
    
    # 1. Buat file .gitignore
    gitignore_path = root_dir / ".gitignore"
    gitignore_path.write_text(GITIGNORE_CONTENT, encoding="utf-8")
    total_files += 1
    print(f"✅ Dibuat: .gitignore")
    
    # 2. Buat file config JSON (agar mudah update nanti)
    config_path = root_dir / "config_kuliah.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(DATA_KULIAH, f, indent=2, ensure_ascii=False)
    total_files += 1
    print(f"✅ Dibuat: config_kuliah.json")
    
    # 3. Buat folder assets dengan .gitkeep
    assets_dir = root_dir / "assets"
    assets_dir.mkdir(exist_ok=True)
    (assets_dir / ".gitkeep").write_text("", encoding="utf-8")
    total_folders += 1
    total_files += 1
    print(f"✅ Dibuat: assets/")
    
    # 4. Buat folder topics dengan README
    topics_dir = root_dir / "topics"
    topics_dir.mkdir(exist_ok=True)
    (topics_dir / "README.md").write_text(TEMPLATE_README_TOPICS, encoding="utf-8")
    total_folders += 1
    total_files += 1
    print(f"✅ Dibuat: topics/")
    
    # 5. Buat folder semesters dan subfolder per semester
    semesters_dir = root_dir / "semesters"
    semesters_dir.mkdir(exist_ok=True)
    total_folders += 1
    
    for semester, matkul_list in DATA_KULIAH.items():
        semester_dir = semesters_dir / semester
        semester_dir.mkdir(exist_ok=True)
        total_folders += 1
        
        # README semester
        readme_semester = create_readme_semester(semester, semester.replace("-", " / "), matkul_list)
        (semester_dir / "README.md").write_text(readme_semester, encoding="utf-8")
        total_files += 1
        
        print(f"   📁 Semester {semester}:")
        
        # Buat folder untuk setiap mata kuliah
        for matkul in matkul_list:
            folder_name = generate_folder_name(matkul["kode"], matkul["nama"])
            matkul_dir = semester_dir / folder_name
            matkul_dir.mkdir(exist_ok=True)
            total_folders += 1
            
            # Subfolder: notes, problems, labs, references
            for subfolder in ["notes", "problems", "labs", "references"]:
                (matkul_dir / subfolder).mkdir(exist_ok=True)
                (matkul_dir / subfolder / ".gitkeep").write_text("", encoding="utf-8")
                total_folders += 1
                total_files += 1
            
            # README mata kuliah
            readme_matkul = create_readme_matkul(
                matkul["kode"], 
                matkul["nama"], 
                matkul["kategori"],
                tanggal_sekarang
            )
            (matkul_dir / "README.md").write_text(readme_matkul, encoding="utf-8")
            total_files += 1
        
        print(f"      └─ {len(matkul_list)} mata kuliah dibuat")
    
    # 6. Buat QUICKSTART.md
    quickstart_path = root_dir / "QUICKSTART.md"
    quickstart_path.write_text(TEMPLATE_QUICKSTART, encoding="utf-8")
    total_files += 1
    print(f"✅ Dibuat: QUICKSTART.md")
    
    # 7. Buat README root
    readme_root = create_readme_root(tanggal_sekarang)
    (root_dir / "README.md").write_text(readme_root, encoding="utf-8")
    total_files += 1
    print(f"✅ Dibuat: README.md (dashboard utama)")
    
    # Print ringkasan
    print("\n" + "="*60)
    print("🎉 SELESAI! Struktur learning notes berhasil dibuat.")
    print("="*60)
    print(f"\n📊 Ringkasan:")
    print(f"   Total folder dibuat: {total_folders}")
    print(f"   Total file dibuat:   {total_files}")
    print(f"   Lokasi root:         {root_dir.absolute()}")
    
    print("\n📂 Struktur folder (3 level pertama):")
    print("""
learning-notes/
├── README.md                 # Dashboard pribadi
├── QUICKSTART.md             # Panduan cepat
├── .gitignore                # Konfigurasi Git
├── config_kuliah.json        # Daftar mata kuliah (editable)
├── assets/                   # Gambar, diagram, file pendukung
├── topics/                   # Topik lintas-matkul
│   └── README.md
└── semesters/
    ├── 2024-1/
    │   ├── README.md
    │   ├── REC241001-fisika-elektronika/
    │   │   ├── README.md
    │   │   ├── notes/
    │   │   ├── problems/
    │   │   ├── labs/
    │   │   └── references/
    │   └── ... (7 matkul lainnya)
    ├── 2024-2/
    │   └── ... (7 matkul)
    └── 2025-1/
        └── ... (6 matkul)
    """)
    
    print("\n🔗 Preview README untuk 'Sistem Mikrokontroler':")
    print("-"*60)
    preview = TEMPLATE_README_MAKUL.format(
        nama_matkul="Sistem Mikrokontroler",
        kode="REC243002",
        kategori="Spesialisasi",
        nama_singkat="SISMIKRO",
        tanggal=tanggal_sekarang
    )
    print(preview[:800] + "...")
    print("-"*60)
    
    print("\n📋 LANGKAH SELANJUTNYA:")
    print("""
1️⃣  Jalankan script ini:
    python generate_learning_notes.py

2️⃣  Masuk ke folder dan inisialisasi Git:
    cd learning-notes
    git init
    git add .
    git commit -m "Initial setup: learning notes Teknik Elektronika & Kendali"

3️⃣  Mulai isi catatan:
    - Buka learning-notes/README.md untuk overview
    - Pilih semester atau topik yang menarik
    - Edit template sesuai kebutuhanmu

4️⃣  Sync ke GitHub (opsional):
    git remote add origin https://github.com/username/repo-name.git
    git push -u origin main

💡 Tips: Repo ini fleksibel! Kamu bisa mulai dari mana saja, 
   tambah folder baru, atau modifikasi struktur sesuai keinginan.
    """)
    
    print("="*60)

if __name__ == "__main__":
    main()
