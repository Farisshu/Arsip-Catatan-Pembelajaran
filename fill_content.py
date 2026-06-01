#!/usr/bin/env python3
"""
Script untuk mengisi konten spesifik semua mata kuliah
di repository learning-notes Teknik Elektronika & Kendali
"""

from pathlib import Path
import datetime

# Data lengkap semua mata kuliah dengan konten spesifik
MATKUL_DATA = {
    # ========== SEMESTER 1 - 2024-1 ==========
    "REC241001": {
        "nama": "Fisika Elektronika",
        "kategori": "Dasar",
        "topik": [
            "Elektrostatika & Medan Listrik",
            "Hukum Gauss & Potensial Listrik",
            "Kapasitansi & Dielektrikum",
            "Arus & Hambatan Listrik",
            "Rangkaian DC & Hukum Kirchhoff",
            "Medan Magnet & Hukum Biot-Savart",
            "Hukum Faraday & Induktansi",
            "Rangkaian AC & Impedansi",
            "Gelombang Elektromagnetik",
            "Optika & Serat Optik"
        ],
        "rumus_kunci": [
            ("Hukum Coulomb", r"F = k \frac{q_1 q_2}{r^2}"),
            ("Medan Listrik", r"E = \frac{F}{q} = k \frac{Q}{r^2}"),
            ("Hukum Ohm", r"V = I \cdot R"),
            ("Daya Listrik", r"P = V \cdot I = I^2 R = \frac{V^2}{R}"),
            ("Induktansi", r"V_L = L \frac{dI}{dt}"),
            ("Impedansi Kapasitor", r"X_C = \frac{1}{\omega C}"),
            ("Impedansi Induktor", r"X_L = \omega L"),
            ("Frekuensi Gelombang EM", r"c = \lambda \cdot f")
        ],
        "praktikum": [
            "Pengukuran medan listrik dengan elektroskop",
            "Verifikasi hukum Ohm dan Kirchhoff",
            "Pengukuran kapasitansi dan induktansi",
            "Observasi gelombang EM dengan antenna dipole",
            "Eksperimen optika: refleksi, refraksi, interferensi"
        ],
        "referensi": [
            "Fundamentals of Physics - Halliday, Resnick, Walker",
            "University Physics - Young & Freedman",
            "Physics for Scientists and Engineers - Serway",
            "MIT OpenCourseWare: Electricity and Magnetism"
        ]
    },
    
    "REC241002": {
        "nama": "Praktikum Fisika Elektronika",
        "kategori": "Dasar",
        "topik": [
            "Teknik Pengukuran Instrumentasi",
            "Kalibrasi Alat Ukur",
            "Analisis Ketidakpastian Pengukuran",
            "Eksperimen Elektrostatika",
            "Eksperimen Rangkaian DC",
            "Eksperimen Medan Magnet",
            "Eksperimen Induksi Elektromagnetik",
            "Eksperimen Rangkaian AC",
            "Eksperimen Gelombang & Optika",
            "Pelaporan Hasil Praktikum"
        ],
        "rumus_kunci": [
            ("Ketidakpastian Relatif", r"\delta = \frac{\Delta x}{x} \times 100\%"),
            ("Ralat Gabungan", r"\Delta z = \sqrt{\left(\frac{\partial z}{\partial x}\Delta x\right)^2 + \left(\frac{\partial z}{\partial y}\Delta y\right)^2}"),
            ("Regresi Linear", r"y = mx + c, \quad m = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}")
        ],
        "praktikum": [
            "Modul 1: Pengukuran dasar dengan multimeter & osiloskop",
            "Modul 2: Hukum Coulomb dan medan listrik",
            "Modul 3: Rangkaian seri-paralel resistor",
            "Modul 4: Hukum Kirchhoff arus dan tegangan",
            "Modul 5: Medan magnet solenoida",
            "Modul 6: Induksi elektromagnetik",
            "Modul 7: Rangkaian RC, RL, RLC",
            "Modul 8: Gelombang berdiri pada tali",
            "Modul 9: Interferensi dan difraksi cahaya"
        ],
        "referensi": [
            "Manual Praktikum Fisika Dasar - Laboratorium Fisika",
            "The Art of Experimental Physics - Melissinos",
            "Data Reduction and Error Analysis - Bevington"
        ]
    },
    
    "REC241003": {
        "nama": "Matematika 1",
        "kategori": "Dasar",
        "topik": [
            "Sistem Bilangan Real & Pertidaksamaan",
            "Fungsi & Grafik",
            "Limit & Kekontinuan",
            "Turunan & Aturan Diferensiasi",
            "Aplikasi Turunan (Optimasi, Related Rates)",
            "Integral Tentu & Tak Tentu",
            "Teknik Integrasi (Substitusi, Parsial)",
            "Aplikasi Integral (Luas, Volume)",
            "Fungsi Transenden (Exp, Log, Trigonometri)",
            "Deret & Kekonvergenan"
        ],
        "rumus_kunci": [
            ("Definisi Limit", r"\lim_{x \to a} f(x) = L"),
            ("Definisi Turunan", r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}"),
            ("Aturan Rantai", r"\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)"),
            ("Integral Tentu", r"\int_a^b f(x) dx = F(b) - F(a)"),
            ("Integral Parsial", r"\int u dv = uv - \int v du"),
            ("Deret Taylor", r"f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n"),
            ("Deret Geometri", r"\sum_{n=0}^{\infty} ar^n = \frac{a}{1-r}, |r| < 1")
        ],
        "praktikum": [
            "Visualisasi limit dan kekontinuan dengan Python/MATLAB",
            "Simulasi aplikasi turunan untuk optimasi",
            "Perhitungan luas dan volume dengan integral numerik",
            "Plot fungsi transenden dan deret Fourier"
        ],
        "referensi": [
            "Calculus - James Stewart",
            "Calculus: Early Transcendentals - Anton",
            "Pure Mathematics - G.N. Berman",
            "Khan Academy: Calculus",
            "Paul's Online Math Notes"
        ]
    },
    
    "REC241004": {
        "nama": "K3 (Keselamatan & Kesehatan Kerja)",
        "kategori": "Dasar",
        "topik": [
            "Konsep Dasar K3 & Regulasi",
            "Identifikasi Bahaya & Risiko",
            "APD (Alat Pelindung Diri)",
            "K3 Listrik & Sengatan Elektrik",
            "K3 Kebakaran & Sistem Proteksi",
            "K3 Bahan Kimia & MSDS",
            "Ergonomi & Kesehatan Kerja",
            "Prosedur Darurat & Evakuasi",
            "Investigasi Kecelakaan Kerja",
            "Sistem Manajemen K3 (SMK3)"
        ],
        "rumus_kunci": [
            ("Risk Matrix", r"Risk = Probability \times Severity"),
            ("Nilai Ambang Batas", r"TWA = \frac{C_1 T_1 + C_2 T_2 + \dots + C_n T_n}{T_1 + T_2 + \dots + T_n}"),
            ("Tahanan Tubuh Manusia", r"R_{body} \approx 1000\Omega - 100k\Omega (kulit kering)")
        ],
        "praktikum": [
            "Inspeksi K3 laboratorium",
            "Pemilihan dan penggunaan APD yang tepat",
            "Simulasi pemadaman kebakaran (APAR)",
            "Pembacaan MSDS bahan kimia",
            "Penyusunan Job Safety Analysis (JSA)",
            "Drill evakuasi darurat"
        ],
        "referensi": [
            "Undang-Undang No. 1 Tahun 1970 tentang Keselamatan Kerja",
            "Permenaker No. 5 Tahun 2018 tentang K3 Lingkungan Kerja",
            "OSHA Standards",
            "NFPA 70E: Electrical Safety in the Workplace"
        ]
    },
    
    "REC241005": {
        "nama": "Rangkaian Listrik 1",
        "kategori": "Dasar",
        "topik": [
            "Elemen Rangkaian: Sumber & Beban",
            "Hukum Ohm & Hukum Kirchhoff",
            "Rangkaian Seri & Paralel",
            "Transformasi Sumber",
            "Analisis Node (Nodal Analysis)",
            "Analisis Mesh (Mesh Analysis)",
            "Teorema Thevenin & Norton",
            "Teorema Superposisi",
            "Transfer Daya Maksimum",
            "Rangkaian Orde Pertama (RC, RL)"
        ],
        "rumus_kunci": [
            ("Hukum Ohm", r"V = I \cdot R"),
            ("KCL", r"\sum I_{masuk} = \sum I_{keluar}"),
            ("KVL", r"\sum V = 0"),
            ("Resistor Seri", r"R_{eq} = R_1 + R_2 + \dots"),
            ("Resistor Paralel", r"\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots"),
            ("Thevenin", r"V_{th}, R_{th}"),
            ("Norton", r"I_N, R_N = R_{th}"),
            ("Waktu RC", r"\tau = RC"),
            ("Waktu RL", r"\tau = \frac{L}{R}")
        ],
        "praktikum": [
            "Verifikasi hukum Ohm dan Kirchhoff",
            "Analisis rangkaian seri-paralel",
            "Eksperimen teorema Thevenin-Norton",
            "Superposisi pada rangkaian multi-sumber",
            "Respons transient RC dan RL",
            "Simulasi dengan LTspice/Multisim"
        ],
        "referensi": [
            "Electric Circuits - Nilsson & Riedel",
            "Engineering Circuit Analysis - Hayt & Kemmerly",
            "Fundamentals of Electric Circuits - Alexander & Sadiku",
            "All About Circuits (online)"
        ]
    },
    
    "REC241006": {
        "nama": "Praktikum Rangkaian Listrik 1",
        "kategori": "Dasar",
        "topik": [
            "Penggunaan Breadboard & Multimeter",
            "Power Supply DC",
            "Osiloskop Dasar",
            "Generator Fungsi",
            "Karakterisasi Resistor",
            "Verifikasi Hukum Kirchhoff",
            "Eksperimen Thevenin-Norton",
            "Respons Transien RC/RL",
            "Troubleshooting Rangkaian"
        ],
        "rumus_kunci": [
            ("Akurasi Pengukuran", r"\text{Error} = \frac{\text{Nilai Terukur} - \text{Nilai Teori}}{\text{Nilai Teori}} \times 100\%"),
            ("Konstanta Waktu", r"\tau = RC \text{ atau } \tau = L/R"),
            ("Tegangan Kapasitor", r"V_C(t) = V_0(1 - e^{-t/\tau})")
        ],
        "praktikum": [
            "Modul 1: Pengenalan alat ukur",
            "Modul 2: Karakteristik resistor & kode warna",
            "Modul 3: Hukum Ohm & Kirchhoff",
            "Modul 4: Rangkaian seri-paralel",
            "Modul 5: Teorema superposisi",
            "Modul 6: Thevenin & Norton",
            "Modul 7: Transfer daya maksimum",
            "Modul 8: Respons RC",
            "Modul 9: Respons RL"
        ],
        "referensi": [
            "Manual Praktikum Rangkaian Listrik",
            "LTspice Tutorial",
            "NI Multisim User Guide"
        ]
    },
    
    "REC241007": {
        "nama": "Bengkel Mekanik",
        "kategori": "Dasar",
        "topik": [
            "Keselamatan Kerja Bengkel",
            "Alat Tangan & Mesin Perkakas",
            "Pengukuran Dimensi (Mistar, Jangka Sorong, Mikrometer)",
            "Teknik Memotong & Menggergaji",
            "Teknik Mengikir & Meratakan",
            "Teknik Mengebor & Mengetap",
            "Teknik Membubut Dasar",
            "Teknik Mengelas (Las Listrik & Oxy-Acetylene)",
            "Gambar Teknik & Toleransi",
            "Project: Pembuatan Komponen Sederhana"
        ],
        "rumus_kunci": [
            ("Kecepatan Potong", r"V_c = \pi \cdot D \cdot n"),
            ("Kecepatan Pemakanan", r"V_f = f \cdot n"),
            ("Toleransi ISO", r"IT7, IT8, dst."),
            ("Suaian (Fit)", r"H7/g6, H7/h6, dll.")
        ],
        "praktikum": [
            "Praktik pengukuran presisi",
            "Memotong plat dengan gergaji",
            "Mengikir hingga ketelitian 0.05mm",
            "Mengebor & membuat ulir (tap & die)",
            "Membubut poros sederhana",
            "Mengelas kampuh sudut & tumpu",
            "Project akhir: pembuatan tool holder / bracket"
        ],
        "referensi": [
            "Teknik Pemesinan - Pradyana",
            "Machine Tool Practices - Kibbe et al.",
            "Technology of Machine Tools - Krar & Check",
            "ISO 2768: General Tolerances"
        ]
    },
    
    "REC241008": {
        "nama": "Algoritma Pemrograman",
        "kategori": "Dasar",
        "topik": [
            "Konsep Algoritma & Flowchart",
            "Variabel, Tipe Data, Operator",
            "Input/Output Dasar",
            "Struktur Kontrol: Percabangan (if-else, switch)",
            "Struktur Kontrol: Perulangan (for, while, do-while)",
            "Array & String",
            "Fungsi & Prosedur",
            "Pointer & Memori (untuk C/C++)",
            "Struktur Data Dasar (Stack, Queue, Linked List)",
            "Algoritma Sorting & Searching"
        ],
        "rumus_kunci": [
            ("Kompleksitas Waktu", r"O(1), O(n), O(n^2), O(\log n)"),
            ("Bubble Sort", r"O(n^2)"),
            ("Binary Search", r"O(\log n)"),
            ("Rekursif", r"T(n) = T(n-1) + O(1)")
        ],
        "praktikum": [
            "Flowchart algoritma sederhana",
            "Program kalkulator dengan percabangan",
            "Looping untuk pola & deret",
            "Manipulasi array & string",
            "Fungsi rekursif (faktorial, Fibonacci)",
            "Implementasi stack & queue",
            "Sorting: Bubble, Selection, Insertion Sort",
            "Searching: Sequential & Binary Search"
        ],
        "referensi": [
            "Introduction to Algorithms - Cormen et al.",
            "C Programming Language - K&R",
            "Python Crash Course - Eric Matthes",
            "freeCodeCamp, CS50 Harvard"
        ]
    },
    
    # ========== SEMESTER 2 - 2024-2 ==========
    "REC242001": {
        "nama": "Rangkaian Listrik 2",
        "kategori": "Dasar",
        "topik": [
            "Rangkaian AC Steady-State",
            "Fasor & Diagram Fasor",
            "Impedansi & Admitansi Kompleks",
            "Analisis Daya AC (Aktif, Reaktif, Semu)",
            "Faktor Daya & Koreksi",
            "Rangkaian Resonansi (Seri & Paralel)",
            "Rangkaian Kopling Magnetik",
            "Transformator Ideal & Non-Ideal",
            "Rangkaian Tiga Fasa",
            "Filter Pasif (LPF, HPF, BPF, BSF)"
        ],
        "rumus_kunci": [
            ("Fasor", r"V = V_m \angle \theta = V_m e^{j\theta}"),
            ("Impedansi", r"Z = R + jX = |Z|\angle\phi"),
            ("Daya Kompleks", r"S = P + jQ = VI^*"),
            ("Faktor Daya", r"pf = \cos\phi = \frac{P}{S}"),
            ("Resonansi", r"\omega_0 = \frac{1}{\sqrt{LC}}"),
            ("Faktor Kualitas", r"Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 RC}"),
            ("Daya 3-Fasa", r"P = \sqrt{3} V_L I_L \cos\phi")
        ],
        "praktikum": [
            "Analisis fasor dengan osiloskop",
            "Pengukuran daya AC & faktor daya",
            "Eksperimen resonansi RLC",
            "Karakterisasi transformator",
            "Rangkaian tiga fasa bintang-delta",
            "Desain filter pasif",
            "Simulasi dengan LTspice"
        ],
        "referensi": [
            "Electric Circuits - Nilsson & Riedel",
            "Engineering Circuit Analysis - Hayt",
            "AC Circuit Analysis textbooks"
        ]
    },
    
    "REC242002": {
        "nama": "Elektronika Analog 1",
        "kategori": "Inti",
        "topik": [
            "Semikonduktor & Dioda",
            "Rangkaian Dioda (Rectifier, Clipper, Clamper)",
            "Transistor BJT: Struktur & Karakteristik",
            "Biasing BJT (Fixed, Emitter, Voltage Divider)",
            "BJT sebagai Saklar & Amplifier",
            "Model Small-Signal BJT",
            "Konfigurasi Amplifier BJT (CE, CC, CB)",
            "JFET & MOSFET Dasar",
            "Biasing & Amplifier FET",
            "Frequency Response Amplifier"
        ],
        "rumus_kunci": [
            ("Dioda Shockley", r"I_D = I_S(e^{V_D/V_T} - 1)"),
            ("Arus BJT", r"I_E = I_B + I_C, \quad I_C = \beta I_B"),
            ("Transkonduktansi", r"g_m = \frac{I_C}{V_T}"),
            ("Gain CE", r"A_v = -g_m R_C"),
            ("Input Impedance", r"Z_{in} = R_1 || R_2 || \beta r_e"),
            ("MOSFET Saturation", r"I_D = \frac{1}{2}k_n(V_{GS} - V_{th})^2")
        ],
        "praktikum": [
            "Karakterisasi dioda & LED",
            "Rectifier half-wave & full-wave",
            "Clipper & clamper circuits",
            "Biasing BJT & Q-point",
            "Amplifier Common Emitter",
            "Amplifier Common Collector (Emitter Follower)",
            "JFET characteristics",
            "MOSFET switching & amplification"
        ],
        "referensi": [
            "Electronic Devices and Circuit Theory - Boylestad",
            "Microelectronic Circuits - Sedra & Smith",
            "The Art of Electronics - Horowitz & Hill"
        ]
    },
    
    "REC242003": {
        "nama": "Bengkel Elektronika",
        "kategori": "Dasar",
        "topik": [
            "Keselamatan Bengkel Elektronika",
            "Alat Kerja: Solder, Desoldering, Multimeter",
            "Teknik Menyolder & Desoldering",
            "PCB Design & Etching Manual",
            "Komponen Elektronika: Identifikasi & Testing",
            "Power Supply DC Sederhana",
            "Amplifier Audio Mini",
            "Sensor & Aktuator Dasar",
            "Troubleshooting & Repair",
            "Project: Perangkat Elektronika Fungsional"
        ],
        "rumus_kunci": [
            ("Suhu Solder", r"T \approx 300-400^\circ C"),
            ("Waktu Solder", r"t < 3 \text{ detik per joint}"),
            ("Regulator LM78xx", r"V_{out} = \text{fixed}")
        ],
        "praktikum": [
            "Praktik soldering pada PCB latihan",
            "Desain layout PCB dengan software",
            "Etching PCB manual (ferric chloride)",
            "Assembly power supply 5V/12V",
            "Pembuatan amplifier audio 10W",
            "Interfacing sensor LDR, PIR, ultrasonic",
            "Troubleshooting board rusak",
            "Project akhir: alarm, timer, atau robot mini"
        ],
        "referensi": [
            "Practical Electronics for Inventors - Scherz",
            "Make: Electronics - Charles Platt",
            "PCB Design tutorials online"
        ]
    },
    
    "REC242004": {
        "nama": "Sensor & Aktuator",
        "kategori": "Inti",
        "topik": [
            "Prinsip Dasar Sensor & Aktuator",
            "Karakteristik Sensor (Akurasi, Presisi, Resolusi)",
            "Sensor Suhu (Termokopel, RTD, Thermistor, IC)",
            "Sensor Cahaya (LDR, Photodiode, Phototransistor)",
            "Sensor Tekanan & Strain Gauge",
            "Sensor Proximity & Ultrasonik",
            "Sensor Posisi & Encoder",
            "Aktuator: Motor DC, Servo, Stepper",
            "Aktuator: Solenoid, Relay, Pneumatik",
            "Signal Conditioning & Interface"
        ],
        "rumus_kunci": [
            ("Sensitivitas", r"S = \frac{\Delta V_{out}}{\Delta Input}"),
            ("Termokopel", r"V = \alpha(T_{hot} - T_{cold})"),
            ("Strain Gauge", r"\frac{\Delta R}{R} = G \cdot \epsilon"),
            ("Ultrasonik Distance", r"d = \frac{v \cdot t}{2}"),
            ("Stepper Steps", r"\text{Steps/rev} = \frac{360^\circ}{\text{step angle}}")
        ],
        "praktikum": [
            "Kalibrasi sensor suhu",
            "Light meter dengan LDR/photodiode",
            "Load cell dengan strain gauge",
            "Distance measurement dengan HC-SR04",
            "Control motor DC dengan PWM",
            "Control servo dengan Arduino",
            "Stepper motor positioning",
            "Data acquisition dengan DAQ/card"
        ],
        "referensi": [
            "Measurement and Instrumentation - Morris",
            "Sensors and Actuators for Mechatronics - Barthelmes",
            "Datasheet berbagai sensor (DigiKey, Mouser)"
        ]
    },
    
    "REC242005": {
        "nama": "Teknik Digital 1",
        "kategori": "Inti",
        "topik": [
            "Sistem Bilangan & Kode (Binary, Hex, BCD)",
            "Aljabar Boolean & Gerbang Logika",
            "Minimisasi Fungsi (K-Map, Quine-McCluskey)",
            "Kombinasional: Adder, Subtractor, Comparator",
            "Kombinasional: Encoder, Decoder, Multiplexer",
            "Sequential: Latch & Flip-Flop (SR, D, JK, T)",
            "Counter & Register",
            "Memory: ROM, RAM, EEPROM",
            "Logic Families: TTL, CMOS",
            "Introduction to PLD/FPGA"
        ],
        "rumus_kunci": [
            ("De Morgan", r"\overline{A \cdot B} = \overline{A} + \overline{B}"),
            ("Full Adder Sum", r"S = A \oplus B \oplus C_{in}"),
            ("Full Adder Carry", r"C_{out} = AB + C_{in}(A \oplus B)"),
            ("JK Flip-Flop", r"Q_{next} = J\overline{Q} + \overline{K}Q"),
            ("Frekuensi Counter", r"f_{out} = \frac{f_{clk}}{2^n}")
        ],
        "praktikum": [
            "Gerbang logika dasar (AND, OR, NOT, XOR)",
            "Implementasi fungsi Boolean dengan K-Map",
            "Rangkaian adder 4-bit",
            "Decoder 7-segment display",
            "Multiplexer 4-to-1",
            "Counter asynchronous & synchronous",
            "Shift register",
            "Memory addressing sederhana",
            "Simulasi dengan Logisim/Multisim"
        ],
        "referensi": [
            "Digital Design - Mano",
            "Fundamentals of Digital Logic - Brown & Vranesic",
            "The Art of Electronics - Horowitz"
        ]
    },
    
    "REC242006": {
        "nama": "Matematika 2",
        "kategori": "Dasar",
        "topik": [
            "Vektor & Ruang Vektor",
            "Matriks & Determinan",
            "Sistem Persamaan Linear",
            "Eigenvalue & Eigenvector",
            "Fungsi Beberapa Variabel",
            "Turunan Parsial & Gradien",
            "Integral Lipat Dua & Tiga",
            "Integral Garis & Permukaan",
            "Teorema Green, Stokes, Divergensi",
            "Persamaan Diferensial Biasa (ODE)"
        ],
        "rumus_kunci": [
            ("Dot Product", r"\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta"),
            ("Cross Product", r"\mathbf{a} \times \mathbf{b} = |\mathbf{a}||\mathbf{b}|\sin\theta \, \mathbf{n}"),
            ("Determinan", r"\det(A) = ad - bc \text{ (2x2)}"),
            ("Eigenvalue", r"A\mathbf{v} = \lambda\mathbf{v}"),
            ("Gradien", r"\nabla f = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j}"),
            ("Divergensi", r"\nabla \cdot \mathbf{F}"),
            ("Curl", r"\nabla \times \mathbf{F}"),
            ("ODE Orde-1", r"\frac{dy}{dx} + P(x)y = Q(x)")
        ],
        "praktikum": [
            "Operasi vektor & matriks dengan Python/NumPy",
            "Solusi SPL dengan eliminasi Gauss",
            "Visualisasi medan vektor",
            "Perhitungan integral lipat dengan MATLAB",
            "Solusi ODE dengan metode Euler & Runge-Kutta"
        ],
        "referensi": [
            "Advanced Engineering Mathematics - Kreyszig",
            "Linear Algebra - Gilbert Strang",
            "Calculus Vol. 3 - Stewart"
        ]
    },
    
    "REC242007": {
        "nama": "Gambar Teknik",
        "kategori": "Dasar",
        "topik": [
            "Standar Gambar Teknik (ISO, ANSI)",
            "Alat Gambar Manual & CAD",
            "Proyeksi Ortogonal (First & Third Angle)",
            "Proyeksi Aksonometri (Isometri, Dimetri)",
            "Potongan & Penampang",
            "Dimensioning & Tolerancing",
            "Surface Finish & Simbol Las",
            "Assembly Drawing",
            "Electrical Schematic Symbols",
            "CAD 2D Dasar (AutoCAD/QCAD)"
        ],
        "rumus_kunci": [
            ("Skala", r"\text{Skala} = \frac{\text{Ukuran Gambar}}{\text{Ukuran Asli}}"),
            ("Toleransi", r"D = d \pm \Delta d"),
            ("Ra Surface", r"Ra = \frac{1}{l}\int_0^l |y(x)|dx")
        ],
        "praktikum": [
            "Menggambar proyeksi ortogonal manual",
            "Isometric drawing",
            "Sectional views",
            "Dimensioning practice",
            "Assembly drawing komponen mekanik",
            "Electrical schematic diagram",
            "CAD: AutoCAD 2D basics",
            "Project: Gambar lengkap suatu device"
        ],
        "referensi": [
            "Technical Drawing - Giesecke et al.",
            "Engineering Drawing - N.D. Bhatt",
            "ISO 128: Technical Drawings",
            "AutoCAD tutorials"
        ]
    },
    
    # ========== SEMESTER 3 - 2025-1 ==========
    "REC243001": {
        "nama": "Elektronika Analog 2",
        "kategori": "Inti",
        "topik": [
            "Amplifier Diferensial",
            "Operational Amplifier (Op-Amp) Ideal",
            "Konfigurasi Op-Amp (Inverting, Non-Inverting, Buffer)",
            "Aplikasi Op-Amp (Summing, Integrator, Differentiator)",
            "Op-Amp Non-Ideal (Offset, Bandwidth, Slew Rate)",
            "Feedback & Stabilitas",
            "Oscillator (RC, LC, Crystal)",
            "Active Filters (Butterworth, Chebyshev)",
            "Voltage Regulator (Linear, Switching)",
            "PLL & Applications"
        ],
        "rumus_kunci": [
            ("Gain Inverting", r"A_v = -\frac{R_f}{R_{in}}"),
            ("Gain Non-Inverting", r"A_v = 1 + \frac{R_f}{R_g}"),
            ("Integrator", r"V_{out} = -\frac{1}{RC}\int V_{in} dt"),
            ("Differentiator", r"V_{out} = -RC\frac{dV_{in}}{dt}"),
            ("Bandwidth", r"GBW = A_v \cdot f_c"),
            ("Slew Rate", r"SR = \frac{dV_{out}}{dt}|_{max}"),
            ("Wien Bridge", r"f_0 = \frac{1}{2\pi RC}")
        ],
        "praktikum": [
            "Characterization Op-Amp 741/LM358",
            "Inverting & non-inverting amplifier",
            "Summing amplifier (mixer audio)",
            "Integrator & differentiator",
            "Active LPF/HPF design",
            "Wien bridge oscillator",
            "Voltage regulator LM317",
            "Function generator dengan Op-Amp"
        ],
        "referensi": [
            "Op-Amps for Everyone - Mancini",
            "Microelectronic Circuits - Sedra/Smith",
            "Analog Devices tutorials"
        ]
    },
    
    "REC243002": {
        "nama": "Sistem Mikrokontroler",
        "kategori": "Inti",
        "topik": [
            "Arsitektur Mikrokontroler (Harvard vs Von Neumann)",
            "ARM Cortex-M / AVR Architecture",
            "GPIO & Interrupts",
            "Timer & Counter",
            "PWM & Motor Control",
            "ADC & DAC",
            "Serial Communication (UART, SPI, I2C)",
            "Watchdog Timer & Low Power Modes",
            "Embedded C Programming",
            "RTOS Basics (FreeRTOS)"
        ],
        "rumus_kunci": [
            ("PWM Duty Cycle", r"D = \frac{T_{on}}{T_{total}} \times 100\%"),
            ("ADC Resolution", r"V_{step} = \frac{V_{ref}}{2^n}"),
            ("UART Baud Rate", r"Baud = \frac{f_{clk}}{16 \cdot UBRR}"),
            ("SPI Clock", r"f_{SPI} = \frac{f_{clk}}{2 \cdot prescaler}")
        ],
        "praktikum": [
            "LED blinking & GPIO input",
            "External interrupt dengan button",
            "Timer interrupt & millis()",
            "PWM untuk LED dimming & servo",
            "ADC membaca sensor analog",
            "UART communication dengan PC",
            "I2C: LCD & sensor (MPU6050, BMP280)",
            "SPI: SD card & display",
            "Project: Data logger / weather station"
        ],
        "referensi": [
            "Making Embedded Systems - Elecia White",
            "ARM Cortex-M Microcontroller Manuals",
            "Arduino & STM32 documentation",
            "FreeRTOS kernel guide"
        ]
    },
    
    "REC243003": {
        "nama": "Instrumentasi Industri",
        "kategori": "Spesialisasi",
        "topik": [
            "Sistem Instrumentasi & Kontrol Proses",
            "Pressure Measurement (Manometer, Bourdon, Pressure Transmitter)",
            "Flow Measurement (Orifice, Venturi, Magnetic, Ultrasonic)",
            "Level Measurement (Float, Capacitive, Radar)",
            "Temperature Transmitters",
            "Control Valve & Actuators",
            "I/P Converter & Positioner",
            "Process Calibrator",
            "Industrial Communication (4-20mA, HART, Foundation Fieldbus)",
            "Safety Instrumented Systems (SIS)"
        ],
        "rumus_kunci": [
            ("Orifice Flow", r"Q = C_d A \sqrt{\frac{2\Delta P}{\rho}}"),
            ("Venturi", r"Q = \frac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}}\sqrt{2g\Delta h}"),
            ("Hydrostatic Level", r"P = \rho g h"),
            ("4-20mA Scaling", r"PV = \frac{I - 4}{16} \times (Range_{max} - Range_{min}) + Range_{min}")
        ],
        "praktikum": [
            "Kalibrasi pressure transmitter",
            "Flow measurement dengan orifice plate",
            "Level measurement capacitive",
            "Control valve characterization",
            "Loop checking 4-20mA",
            "HART communicator usage",
            "P&ID reading & interpretation"
        ],
        "referensi": [
            "Process Control Instrumentation - Curtis Johnson",
            "Instrument Engineers' Handbook - Bela Liptak",
            "ISA Standards"
        ]
    },
    
    "REC243004": {
        "nama": "PLC (Programmable Logic Controller)",
        "kategori": "Spesialisasi",
        "topik": [
            "PLC Architecture & Components",
            "I/O Modules (Digital, Analog)",
            "Ladder Logic Programming",
            "Function Block Diagram (FBD)",
            "Structured Text (ST)",
            "Timer & Counter Instructions",
            "Compare & Math Operations",
            "Data Handling (Move, Shift)",
            "Sequencer & Program Control",
            "HMI Integration & SCADA Basics"
        ],
        "rumus_kunci": [
            ("Scan Time", r"T_{scan} = T_{input} + T_{program} + T_{output}"),
            ("Resolution ADC PLC", r"12-bit = 4096 steps")
        ],
        "praktikum": [
            "Wiring input/output PLC",
            "Ladder: start-stop motor",
            "Timer ON/OFF delay",
            "Counter up/down",
            "Sequence control conveyor",
            "Analog scaling (4-20mA to engineering units)",
            "HMI: button, indicator, trend",
            "Project: Traffic light / sorting system"
        ],
        "referensi": [
            "Programmable Logic Controllers - Frank Petruzella",
            "Siemens S7-1200/1500 manuals",
            "Allen-Bradley RSLogix tutorials",
            "IEC 61131-3 standard"
        ]
    },
    
    "REC243005": {
        "nama": "Sistem Kendali Kontinyu",
        "kategori": "Inti",
        "topik": [
            "Introduction to Control Systems",
            "Mathematical Modeling (Transfer Function)",
            "Block Diagram & Signal Flow Graph",
            "Time Response Analysis (1st & 2nd Order)",
            "Steady-State Error Analysis",
            "Routh-Hurwitz Stability Criterion",
            "Root Locus Method",
            "Frequency Response (Bode Plot)",
            "Nyquist Stability Criterion",
            "PID Controller Design"
        ],
        "rumus_kunci": [
            ("Transfer Function", r"G(s) = \frac{Y(s)}{X(s)}"),
            ("1st Order Step", r"y(t) = K(1 - e^{-t/\tau})"),
            ("2nd Order", r"\frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}"),
            ("Overshoot", r"\%OS = e^{-\pi\zeta/\sqrt{1-\zeta^2}} \times 100\%"),
            ("Settling Time", r"T_s \approx \frac{4}{\zeta\omega_n}"),
            ("PID", r"u(t) = K_p e(t) + K_i \int e(t)dt + K_d \frac{de(t)}{dt}"),
            ("Margin Stabilitas", r"GM, PM dari Bode")
        ],
        "praktikum": [
            "Modeling DC motor transfer function",
            "Step response analysis",
            "Routh-Hurwitz stability",
            "Root locus plotting (MATLAB)",
            "Bode plot analysis",
            "PID tuning (Ziegler-Nichols)",
            "Simulation: inverted pendulum, ball-beam",
            "Hardware: temperature/position control"
        ],
        "referensi": [
            "Automatic Control Systems - Kuo",
            "Modern Control Engineering - Ogata",
            "Control Systems Engineering - Nise"
        ]
    },
    
    "REC243006": {
        "nama": "Elektronika Digital",
        "kategori": "Inti",
        "topik": [
            "Review Aljabar Boolean & Minimisasi",
            "Kombinasional Lanjut (ALU, Shifter)",
            "Sequential Lanjut (State Machine)",
            "Finite State Machine (Moore & Mealy)",
            "Memory Systems (SRAM, DRAM, Flash)",
            "Programmable Logic Devices (PAL, GAL, CPLD)",
            "FPGA Architecture (LUT, CLB, IOB)",
            "VHDL/Verilog HDL Basics",
            "Timing Analysis & Constraints",
            "System-on-Chip Introduction"
        ],
        "rumus_kunci": [
            ("Setup Time", r"t_{setup}"),
            ("Hold Time", r"t_{hold}"),
            ("Max Frequency", r"f_{max} = \frac{1}{t_{prop} + t_{setup}}"),
            ("State Equation", r"Q_{next} = f(Q_{current}, Inputs)")
        ],
        "praktikum": [
            "Design ALU 4-bit",
            "FSM: vending machine, traffic light",
            "Memory addressing & decoding",
            "VHDL/Verilog: combinational logic",
            "VHDL/Verilog: FSM implementation",
            "Synthesis dengan Xilinx Vivado/Intel Quartus",
            "Implementation on FPGA board",
            "Timing analysis & optimization"
        ],
        "referensi": [
            "Digital System Design - John Wakerly",
            "FPGA Prototyping by Verilog Examples - Chu",
            "Xilinx/Intel FPGA documentation"
        ]
    }
}


def generate_mindmap(topics, short_name):
    """Generate mermaid mindmap dari topik"""
    if not topics:
        return ""
    
    # Group topics into categories (max 5 main branches)
    mindmap = "```mermaid\nmindmap\n"
    mindmap += f"  root(({short_name}))\n"
    
    # Simple grouping: first 5 topics as main branches
    for i, topic in enumerate(topics[:6]):
        # Clean topic name for mindmap
        clean_topic = topic.split(" ")[0] if len(topic.split()) > 1 else topic[:15]
        mindmap += f"    {clean_topic}\n"
        if i < len(topics) and len(topics) > 6:
            mindmap += f"      {topic}\n"
    
    if len(topics) > 6:
        mindmap += "    Topik Lain\n"
        mindmap += "      (lihat notes/)\n"
    
    mindmap += "```\n"
    return mindmap


def generate_rumus_table(rumus_list):
    """Generate tabel rumus LaTeX"""
    if not rumus_list:
        return ""
    
    table = "| Nama | Rumus |\n|------|-------|\n"
    for nama, rumus in rumus_list[:8]:  # Max 8 rumus
        table += f"| {nama} | `$$ {rumus} $$` |\n"
    
    return table


def update_matkul_readme(base_path, kode, data, folder_override=None):
    """Update README.md untuk satu mata kuliah"""
    if folder_override:
        folder = base_path / folder_override
    else:
        folder = base_path / f"{kode}-{data['nama'].lower().replace(' ', '-').replace('&', 'dan')}"
    readme_path = folder / "README.md"
    
    if not folder.exists():
        print(f"⚠️ Folder tidak ditemukan: {folder}")
        return
    
    # Generate content
    short_name = "".join([word[0] for word in data['nama'].split()[:3]])
    mindmap = generate_mindmap(data['topik'], short_name)
    rumus_table = generate_rumus_table(data['rumus_kunci'])
    
    # Build praktikum list
    praktikum_items = ""
    for prakt in data['praktikum'][:6]:
        praktikum_items += f"- [ ] {prakt}\n"
    
    # Build referensi list
    referensi_items = ""
    for ref in data['referensi'][:4]:
        referensi_items += f"- [ ] {ref}\n"
    
    # Build topik list untuk checklist
    topik_checklist = ""
    for topik in data['topik'][:10]:
        topik_checklist += f"- [ ] {topik}\n"
    
    today = datetime.date.today().isoformat()
    
    content = f"""# {data['nama']} ({kode})
> Bidang: {data['kategori']} | Target Pemahaman: _Saya isi sendiri_

---

## 🗺️ Peta Topik

{mindmap}

> 💡 **Tips**: Edit mindmap di atas sesuai pemahamanmu. Tambahkan cabang baru saat mempelajari konsep tambahan.

---

## 📌 Fokus Belajar Saat Ini

- [ ] Review daftar topik di bawah
- [ ] Pilih 1-2 topik untuk dipelajari minggu ini
- [ ] Kerjakan latihan soal terkait
- [ ] Dokumentasikan insight di notes/

### Daftar Topik Lengkap

{topik_checklist}

---

## 📐 Konsep & Rumus Kunci

> Tulis penjelasan konsep dengan bahasamu sendiri di sini.

{rumus_table}

### Catatan Pemahaman

| Konsep | Pemahaman Saya | Contoh Aplikasi | Masih Bingung? |
|--------|----------------|-----------------|----------------|
| ... | ... | ... | [ ] Ya / [x] Tidak |

---

## 🔧 Praktikum / Simulasi

### Eksperimen yang Tersedia

{praktikum_items}

### Template Laporan Praktikum

```markdown
## Judul Percobaan: ________________

### Tujuan
- 

### Alat & Bahan
- 

### Skema Rangkaian / Setup
```mermaid
graph LR
  A[Input] --> B[Proses]
  B --> C[Output]
```

### Langkah Kerja
1. 
2. 
3. 

### Hasil Pengamatan

| No | Parameter | Nilai Teori | Nilai Praktik | Error (%) |
|----|-----------|-------------|---------------|-----------|
| 1  |           |             |               |           |

### Analisis & Kesimpulan


```

---

## ❓ Catatan Pertanyaan & Insight

> Tempat mencatat: "Kenapa begini?", "Bagaimana jika...?", "Hubungan dengan topik X?"

### 💡 Insight Hari Ini
- 

### 🔍 Pertanyaan yang Belum Terjawab
- 

### 🔗 Koneksi ke Topik Lain
- Lihat juga: [Matkul Terkait](../../README.md)

---

## 🔗 Referensi Saya

### Buku Wajib
{referensi_items}

### Video Tutorial
- [ ] YouTube: Cari channel "GreatScott!", "EEVblog", "The Engineering Mindset"
- [ ] Coursera / edX courses

### Datasheet & Manual
- [ ] [DigiKey](https://www.digikey.com/)
- [ ] [Mouser](https://www.mouser.com/)
- [ ] [AllAboutCircuits](https://www.allaboutcircuits.com/)

### Simulator Online
- [ ] [Falstad Circuit Simulator](https://falstad.com/circuit/)
- [ ] [LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)
- [ ] [Tinkercad](https://www.tinkercad.com/)

---

## 🔄 Riwayat Update

| Tanggal | Progress | Catatan |
|---------|----------|---------|
| {today} | Initial setup | Script auto-fill konten |

---

**[⬅️ Kembali ke Dashboard Semester](../README.md)** | **[🏠 Ke Dashboard Utama](../../README.md)**

---

> 📝 **Catatan**: Template ini sudah diisi dengan konten spesifik {data['nama']}. 
> Edit sesuai kebutuhan, tambah catatan pribadi, dan lengkapi dengan pemahamanmu sendiri!
"""
    
    # Write file
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated: {readme_path}")


def main():
    base_path = Path("/workspace/learning-notes/semesters")
    
    # Mapping kode ke folder semester
    semester_map = {
        "REC241": base_path / "2024-1",
        "REC242": base_path / "2024-2",
        "REC243": base_path / "2025-1"
    }
    
    # Nama folder aktual (tanpa tanda kurung)
    folder_nama_map = {
        "REC241004": "REC241004-k3-keselamatan-dan-kesehatan-kerja",
        "REC243004": "REC243004-plc"
    }
    
    print("🚀 Mulai mengisi konten semua mata kuliah...\n")
    
    for kode, data in MATKUL_DATA.items():
        # Determine semester folder
        prefix = kode[:6]  # e.g., "REC241"
        semester_folder = semester_map.get(prefix)
        
        # Check if folder override needed
        folder_override = folder_nama_map.get(kode)
        
        if semester_folder:
            update_matkul_readme(semester_folder, kode, data, folder_override)
        else:
            print(f"⚠️ Semester tidak ditemukan untuk {kode}")
    
    print("\n✨ Selesai! Semua README.md sudah diisi dengan konten spesifik.")
    print("\n📌 Next steps:")
    print("1. Buka folder mata kuliah yang ingin dipelajari")
    print("2. Edit README.md sesuai pemahamanmu")
    print("3. Isi notes/, problems/, labs/ dengan catatan detail")
    print("4. Commit & push ke GitHub")


if __name__ == "__main__":
    main()
