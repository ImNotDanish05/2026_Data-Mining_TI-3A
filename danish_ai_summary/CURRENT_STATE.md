# Current state
Updated: 2026-11-12

## Goal in progress
Tidak ada tugas aktif (semua target pembaruan slide PPTX telah selesai dan disetujui).

## Done so far
- Mem-backup file presentasi ke `informasi/materi/Danish Mahdi - Analisis Opini Publik MBG - Data Mining TI-3A.pptx.backup_20261112`.
- Memperbarui slide deck `informasi/materi/Danish Mahdi - Analisis Opini Publik MBG - Data Mining TI-3A.pptx` (dari 17 menjadi 19 slide):
  1. **Slide 11 (Cluster Balance Check)**: Menambahkan kotak validasi keseimbangan klaster (Disparity Gap = 28,56% < 40%, membuktikan data seimbang dan bebas mode collapse).
  2. **Slide 14 (Benchmark 4 Algoritma)**: Menyisipkan slide komparasi LDA vs NMF vs LSA vs K-Means lengkap dengan skor Coherence ($C_v$), waktu training, sebaran klaster, dan gambar Donut Chart (`fig4`).
  3. **Slide 15 (Landasan 3 Jurnal Pembanding & LDA)**: Menyisipkan slide rujukan ilmiah terverifikasi (Blei 2003, Wiranto SINTA 2 2022, Lee & Seung Nature 1999, Deerwester JASIS 1990, Sari SINTA 2 2019, Huang 2008) dengan DOI dan link aktif.
- Mempertahankan integritas notebook utama `Analisis_Data_Video_Topic_Modeling_LDA.ipynb` tanpa modifikasi.

## Exactly where I stopped
- File PPTX (19 slide) telah selesai diperbarui dan disetujui oleh pengguna.
- Catatan state `DANISH_AI_SUMMARY.md`, `CURRENT_STATE.md`, dan `CHANGELOG.md` telah disinkronkan.

## Next steps (in order)
1. Latihan presentasi atau ekspor slide ke format PDF/presentasi saat hari ujian.
2. (Opsional) Tempelkan kode dual-plot Donut + Bar Chart keseimbangan data ke Cell 20 pada `Analisis_Data_Video_Topic_Modeling_LDA.ipynb` jika dibutuhkan.
3. Melanjutkan persiapan manuskrip jurnal SINTA 2 jika sudah menentukan target jurnal.

## Half-done / uncommitted changes
- Tidak ada.

## Findings so far (so files needn't be re-read)
- Disparity gap pada pemodelan LDA murni di `Analisis_Data_Video_Topic_Modeling_LDA.ipynb` adalah 28,56% (64,28% vs 35,72%), memenuhi syarat batas toleransi <= 40%.
- Pada eksperimen 4 algoritma di `Komparasi_4_Algoritma_NLP_Topic_Modeling_SINTA2.ipynb`, LDA adalah satu-satunya algoritma yang mencapai sebaran seimbang (gap 4,53%), sedangkan NMF (gap 58,7%), LSA (gap 66,4%), dan K-Means (gap 71,1%) mengalami ketimpangan berat/klaster hampa.

## Tried and failed (don't repeat)
- Notebook `_v1.0` sudah dihapus oleh pengguna; gunakan `Analisis_Data_Video_Topic_Modeling_LDA.ipynb` sebagai notebook utama.

## Open questions / waiting on the user
- Tidak ada.

## How to verify
- `informasi/materi/Danish Mahdi - Analisis Opini Publik MBG - Data Mining TI-3A.pptx` berisi tepat 19 slide.
