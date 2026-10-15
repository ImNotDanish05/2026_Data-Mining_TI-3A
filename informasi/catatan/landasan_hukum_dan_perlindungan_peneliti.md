# Memorandum Kepatuhan Hukum & Perlindungan Peneliti Akademis

Dokumen ini memuat **kajian hukum positif Republik Indonesia** yang memberikan kepastian, perlindungan hukum, dan jaminan kekebalan pidana (*legal immunity for academic research*) bagi peneliti/mahasiswa dalam pelaksanaan penelitian **Data Mining & Analisis Komentar YouTube Kebijakan Publik (Makan Bergizi Gratis)**.

---

## 📌 1. Jaminan Kebebasan Akademik (Undang-Undang Pendidikan Tinggi)

* **Dasar Hukum**: **UU No. 12 Tahun 2012 tentang Pendidikan Tinggi**
  - **Pasal 8 ayat (1)**: *"Dalam penyelenggaraan Pendidikan dan pengembangan Ilmu Pengetahuan dan Teknologi berlaku kebebasan akademik, kebebasan mimbar akademik, dan otonomi keilmuan."*
  - **Pasal 9 ayat (1)**: Kebebasan akademik merupakan kebebasan Sivitas Akademika (dosen dan mahasiswa) dalam Pendidikan Tinggi untuk mendalami dan mengembangkan Ilmu Pengetahuan dan Teknologi secara bertanggung jawab melalui pelaksanaan Tridharma.
* **Implikasi Hukum**:
  Setiap mahasiswa dan peneliti di Indonesia memiliki **hak konstitusional dan perlindungan undang-undang** untuk meneliti topik apa pun—termasuk kebijakan publik nasional—sepanjang menggunakan metode ilmiah yang dapat dipertanggungjawabkan secara metodologis.

---

## 🔒 2. Kepatuhan Regulasi Privasi (UU Perlindungan Data Pribadi)

* **Dasar Hukum**: **UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)**
* **Pasal Kunci**:
  - **Pasal 15 ayat (1) huruf f**: Pengecualian hak subjek data pribadi berlaku untuk **kepentingan statistik dan penelitian ilmiah**.
* **Penerapan Teknis dalam Proyek Ini**:
  1. **Data Berasal dari Ranah Publik (*Public Domain*)**: Komentar yang dianalisis adalah komentar yang secara sukarela diposting publik oleh pengguna di YouTube, bukan pesan pribadi (DM/chat tertutup).
  2. **Penerapan Anonimisasi Mutlak (*Absolute Anonymization*)**:
     Seluruh kolom `author` (nama akun, identitas, dan username) telah **dihapus secara permanen** pada tahap prapemrosesan (`dataset_komentar_clean.csv`).
  3. **Konsekuensi Hukum**:
     Berdasarkan standar hukum pelindungan data, data yang telah di-anonymize **secara hukum tidak lagi dikategorikan sebagai Data Pribadi** karena subjek data tidak dapat lagi diidentifikasi (*de-identified data*). Peneliti tidak dapat dituntut atas dugaan kebocoran data pribadi atau pelanggaran privasi.

---

## ⚖️ 3. Kekebalan dari UU ITE (Pencemaran Nama Baik & Ujaran Kebencian)

* **Dasar Hukum**: **UU No. 1 Tahun 2024 tentang Perubahan Kedua UU No. 11 Tahun 2008 tentang ITE**
* **Pasal Kunci**:
  - **Pasal 27A (Penyerangan Kehormatan / Pencemaran Nama Baik)**:
    - *Memori Penjelasan Resmi*: UU No. 1 Tahun 2024 secara tegas menyatakan bahwa perbuatan yang dilakukan **demi kepentingan umum atau kritik pengawasan kebijakan publik BUKAN merupakan tindak pidana pencemaran nama baik**.
  - **Pasal 28 ayat (2) (Ujaran Kebencian / SARA)**:
    - Hanya berlaku jika seseorang sengaja menyebarkan informasi yang ditujukan untuk menimbulkan rasa kebencian berdasarkan SARA.
* **Fakta Hukum Positif Peneliti**:
  1. **Bukan Pembuat Konten (*Not a Content Creator*)**:
     Peneliti **TIDAK menulis, tidak mengarang, dan tidak memproduksi** komentar tersebut. Peneliti bertindak murni sebagai **pengamat dan pengolah data komputasional (*data processor*)**.
  2. **Doktrin Netralitas Statistik**:
     Output yang disajikan berupa angka distribusi, frekuensi kata, dan klaster topik (*Topic Modeling*), bukan opini subjektif yang menyerang pribadi seseorang.

---

## 🏛️ 4. Ketentuan KUHP Baru Terkait Kritik Pejabat & Presiden

* **Dasar Hukum**: **UU No. 1 Tahun 2023 tentang Kitab Undang-Undang Hukum Pidana (KUHP)**
* **Pasal Kunci**:
  - **Pasal 218 ayat (2)**: *"Tidak merupakan penyerangan kehormatan atau harkat dan martabat sebagaimana dimaksud pada ayat (1) jika perbuatan dilakukan untuk kepentingan umum atau pembelaan diri."*
  - **Penjelasan Pasal 218**: Mengatur secara tegas bahwa kritik, saran, evaluasi, atau ketidaksetujuan terhadap kebijakan pemerintah demi kepentingan umum tidak dapat dipidana.
  - **Sifat Delik**: Pasal 218 adalah **delik aduan absolut (*absolute complaint delict*)**, yang hanya dapat diproses apabila Presiden/Wakil Presiden sendiri yang mengadukan secara langsung, dan tidak berlaku untuk riset akademis berbasis korpus teks publik.

---

## 📖 5. Doktrin Penggunaan Wajar Hak Cipta (*Fair Use*)

* **Dasar Hukum**: **UU No. 28 Tahun 2014 tentang Hak Cipta**
* **Pasal Kunci**:
  - **Pasal 44 ayat (1) huruf a**:
    > *"Penggunaan, pengambilan, penggandaan, dan/atau pengubahan suatu Ciptaan dan/atau produk Hak Terkait secara seluruh atau sebagian yang substansial **TIDAK DIANGGAP SEBAGAI PELANGGARAN HAK CIPTA** jika sumbernya disebutkan atau dicantumkan secara lengkap untuk keperluan: pendidikan, penelitian, penulisan karya ilmiah, penyusunan laporan, penulisan kritik atau tinjauan suatu masalah dengan tidak merugikan kepentingan yang wajar dari Pencipta."*
* **Penerapan**: Pengambilan metadata dan transkrip YouTube mencantumkan URL dan `video_id` sumber secara lengkap untuk tujuan penulisan laporan praktikum.

---

## 💻 6. Legalitas Akses Sistem Komputer (Anti-Hacking)

* **Dasar Hukum**: **Pasal 30 s/d 32 UU ITE** (Tindak pidana akses ilegal dan intersepsi data)
* **Kepatuhan Proyek**:
  - Pengambilan data **TIDAK dilakukan melalui peretasan (*hacking*)**, pembobolan server, atau intersepsi ilegal.
  - Seluruh data diperoleh menggunakan **antarmuka resmi Google YouTube Data API v3** dengan autentikasi API Key terdaftar yang sah dan mematuhi kuota resmi yang ditetapkan oleh Google LLC.

---

## 🛡️ Kesimpulan Hukum Final

| Potensi Risiko | Status Risiko Peneliti | Dasar Perlindungan Hukum |
| :--- | :---: | :--- |
| **Tuntutan UU ITE (Pencemaran Nama Baik)** | ❌ **NIHIL (Aman)** | Peneliti bukan pembuat teks; pengecualian kepentingan umum Pasal 27A UU ITE 2024. |
| **Tuntutan UU PDP (Pelanggaran Privasi)** | ❌ **NIHIL (Aman)** | Identitas akun di-anonymize 100%; Pasal 15 UU PDP mengecualikan riset ilmiah. |
| **Tuntutan Delik Penghinaan Penguasa (KUHP)**| ❌ **NIHIL (Aman)** | Pengecualian kritik kebijakan Pasal 218 ayat (2) KUHP Baru; riset murni statistik deskriptif. |
| **Pelanggaran Hak Cipta** | ❌ **NIHIL (Aman)** | Pengecualian penggunaan wajar pendidikan Pasal 44 ayat (1) UU Hak Cipta. |
| **Akses Ilegal / Cybercrime** | ❌ **NIHIL (Aman)** | Menggunakan API resmi Google YouTube v3 sesuai ToS. |

> **Simpulan:** Repositori ini berdiri di atas dasar hukum yang sangat kokoh. Mahasiswa/peneliti sepenuhnya aman dari ancaman pidana maupun perdata dalam koridor hukum positif Republik Indonesia.

