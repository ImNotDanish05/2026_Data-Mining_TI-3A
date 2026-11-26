# Current state
Updated: 2026-11-18

## Goal in progress
Tidak ada tugas aktif (Penggantian algoritma GMM menjadi HDP / Hierarchical Dirichlet Process serta penambahan jurnal rujukan HDP terverifikasi aktif ke `informasi/catatan/daftar_40_jurnal_pendukung.md` telah selesai).

## Done so far
- Mengembangkan benchmark unsupervised dari 4 algoritma menjadi 6 algoritma (LDA, NMF, LSA, K-Means, HAC, HDP).
- Menggantikan GMM dengan **HDP (Hierarchical Dirichlet Process)** sebagai pembanding non-parametrik resmi dari silsilah Bayesian Topic Modeling (penemu yang sama dengan LDA: Blei & Jordan, 2006).
- Mengidentifikasi dan memverifikasi tautan/DOI aktif (200 OK, bebas 404 & 403) untuk algoritma pembanding HDP:
  - **HDP (Hierarchical Dirichlet Process)**: Makalah seminal Teh, Jordan, Beal, & Blei (2006) di JASA dengan DOI `10.1198/016214506000000302` dan rujukan nasional Erreza dkk. (2024, Jurnal SPIRIT, DOI: `10.53567/spirit.v16i1.325`).
- Memperbarui entri 47 di `informasi/catatan/daftar_40_jurnal_pendukung.md`.

## Exactly where I stopped
- File `informasi/catatan/daftar_40_jurnal_pendukung.md` telah diperbarui menjadi 47 entri jurnal terverifikasi dengan HDP.
- Semua referensi GMM pada catatan `.md` telah dibersihkan dan digantikan dengan HDP.

## Next steps (in order)
1. Perbarui kode Colab jika ingin mengeksekusi HDP (`gensim.models.HdpModel`).
2. Sinkronkan slide PPTX dengan 6 algoritma (LDA, NMF, LSA, K-Means, HAC, HDP).

## Half-done / uncommitted changes
- `informasi/catatan/daftar_40_jurnal_pendukung.md` (Entri 47 diperbarui ke HDP).

## Findings so far (so files needn't be re-read)
- HAC menghasilkan Topic Coherence tinggi ($C_v = 0.5612$), namun kompleksitas komputasinya paling berat (38.5 detik, $O(N^2)$) dan mengalami cluster collapse (99.9% vs 0.1%).
- HDP memberikan pembanding ideal bagi LDA karena sama-sama berasal dari rumpun model topik Bayesian generatif, namun HDP bekerja secara non-parametrik (tanpa perlu mematok $K$ secara manual).
- LDA tetap menjadi model operasional terbaik untuk pengelompokan opini publik dua kutub (64% isu lapangan vs 36% isu fiskal).

## Tried and failed (don't repeat)
- GMM dibatalkan oleh pengguna karena tidak sesuai secara intuitif untuk pemodelan dokumen teks dan berpotensi menimbulkan pertanyaan kritis dosen; diganti secara resmi dengan HDP.
- JANGAN PERNAH melakukan hardcoding label semantik topik (seperti "Isu Operasional & Kualitas" atau "Isu Politik & Anggaran") ke dalam skrip evaluasi/print/chart; biarkan representasi tetap netral matematis (Topik 0, Topik 1) agar tidak menghasilkan interpretasi bias/prematur sebelum kata kunci diperiksa.

## Open questions / waiting on the user
- Apakah pengguna butuh potongan kode Gensim HDP untuk dijalankan di Colab?

## How to verify
- Buka baris 440-466 pada `informasi/catatan/daftar_40_jurnal_pendukung.md`.
