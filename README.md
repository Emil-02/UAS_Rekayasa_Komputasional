# Analisis Sentimen Ulasan Aplikasi DANA menggunakan SVM

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan pengguna aplikasi DANA yang diambil (scraping) dari Google Play Store. Analisis ini menggunakan algoritma Support Vector Machine (SVM) untuk mengklasifikasikan ulasan menjadi sentimen positif dan negatif.

## Struktur Direktori

- **`Scraping/`**: Berisi skrip Python (`scrape_dana_reviews.py`) untuk mengambil ulasan dari Google Play Store, serta dataset hasil scraping (`dana_reviews_negatif.csv`, `dana_reviews_positif.csv`, `dana_reviews_semua.csv`).
- **`SVM_Gabungan.ipynb`**: Jupyter Notebook yang berisi alur lengkap prapemrosesan teks (text preprocessing), ekstraksi fitur (TF-IDF), pelatihan model Support Vector Machine (SVM), dan evaluasi model.
- **`Laporan_kelompok4_KelasF.docx`**: Laporan lengkap mengenai metodologi, analisis, dan hasil dari penelitian.
- **`grafik_perbandingan.png`**: Visualisasi alur kerja dan hasil evaluasi.
- **`sampel_untuk_validasi_manual.csv`**: Data sampel yang digunakan untuk keperluan validasi model secara manual.

## Metodologi

1. **Pengumpulan Data**: Scraping ulasan menggunakan `google-play-scraper`.
2. **Prapemrosesan Data (Preprocessing)**: Meliputi Case Folding, Cleaning, Tokenisasi, Normalisasi, Stopword Removal, dan Stemming.
3. **Pembobotan Kata**: Menggunakan TF-IDF (Term Frequency - Inverse Document Frequency).
4. **Pemodelan**: Menggunakan algoritma Support Vector Machine (SVM).
5. **Evaluasi**: Mengukur akurasi, presisi, recall, dan f1-score dari model yang dibuat.

## Cara Menjalankan

1. Lakukan instalasi pustaka yang dibutuhkan (misal: `pandas`, `scikit-learn`, `Sastrawi`, `google-play-scraper`).
2. Jalankan notebook `SVM_Gabungan.ipynb` langkah demi langkah.
3. Untuk melakukan scraping ulang, jalankan skrip di dalam folder `Scraping/`.

## Kontributor
- Kelompok 4 (Kelas F) - UAS Rekayasa Komputasional
