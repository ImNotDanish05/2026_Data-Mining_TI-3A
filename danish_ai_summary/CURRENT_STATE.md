# Current state
Updated: 2026-11-12

## Goal in progress
Tidak ada tugas aktif (Penambahan 2 rujukan jurnal ilmiah SINTA 2 untuk algoritma HAC dan GMM ke `informasi/catatan/daftar_40_jurnal_pendukung.md` telah selesai dan terverifikasi).

## Done so far
- Mengembangkan benchmark unsupervised dari 4 algoritma menjadi 6 algoritma (LDA, NMF, LSA, K-Means, HAC, GMM) di `Komparasi_4_Algoritma_NLP_Topic_Modeling_SINTA2.ipynb`.
- Mengidentifikasi dan memverifikasi tautan/DOI aktif (200 OK, bebas 404 & 403) untuk 2 algoritma pembanding baru:
  1. **HAC (Hierarchical Agglomerative Clustering)**: Jurnal *Sinkron* (SINTA 2, 2023) oleh Sujadi dkk. dengan DOI `10.33395/sinkron.v8i3.12616` dan rujukan seminal Ward (1963).
  2. **GMM (Gaussian Mixture Model)**: Jurnal *RESTI* (SINTA 2, 2022) oleh Raditya dkk. dengan DOI `10.29207/resti.v6i5.4459` dan rujukan seminal Dempster et al. (1977).
- Memasukkan kedua entri baru (Entri 46 dan 47) ke dalam file katalog literatur `informasi/catatan/daftar_40_jurnal_pendukung.md`.

## Exactly where I stopped
- File `informasi/catatan/daftar_40_jurnal_pendukung.md` telah diperbarui menjadi 47 entri jurnal terverifikasi.
- Tidak ada tugas tertunda.

## Next steps (in order)
1. Perbarui judul dan pembahasan di `Komparasi_4_Algoritma_NLP_Topic_Modeling_SINTA2.ipynb` jika diperlukan.
2. Sinkronkan slide PPTX jika dosen menghendaki 6 algoritma ditampilkan di slide ujian.

## Half-done / uncommitted changes
- `informasi/catatan/daftar_40_jurnal_pendukung.md` (+2 entri jurnal 46 & 47).

## Findings so far (so files needn't be re-read)
- HAC menghasilkan Topic Coherence tertinggi ($C_v = 0.5612$), namun kompleksitas komputasinya paling berat (38.5 detik, $O(N^2)$).
- GMM menghasilkan efisiensi tinggi (0.09 detik) dengan $C_v = 0.4428$ saat dilatih pada komponen dekomposisi laten SVD.
- LDA tetap menjadi model utama terbaik untuk pemodelan topik karena sifat probabilistik campuran topik dokumen (*topic mixture* via Dirichlet prior) dan skalabilitas online.

## Tried and failed (don't repeat)
- Jangan gunakan metrik cosine pada matriks sparse yang memuat zero rows tanpa regularisasi epsilon (bisa memicu ValueError pada linkage tree).

## Open questions / waiting on the user
- Apakah slide PPTX perlu ditambahkan 2 algoritma baru ini (HAC & GMM)?

## How to verify
- Buka baris 440-466 pada `informasi/catatan/daftar_40_jurnal_pendukung.md`.
