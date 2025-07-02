
Judul: Prediksi Popularitas Meme Berdasarkan Caption dan Metadata Menggunakan Machine Learning
Nama : [Isi Nama Anda]
NIM  : [Isi NIM Anda]
Kelas: [Isi Kelas Anda]

1. Ringkasan dan Tujuan
Proyek ini bertujuan untuk memprediksi popularitas meme berdasarkan teks caption dan metadata numerik.
Permasalahan: belum ada model prediktif sederhana berbasis teks untuk mengukur popularitas meme.
Tujuan: membuat pipeline machine learning yang mampu membedakan meme populer dan tidak populer.

Model yang digunakan:
- Logistic Regression (baseline)
- Random Forest (non-linear model)
- XGBoost (boosted tree)

2. Dataset dan Fitur
Dataset: dankmemes_top_1000.csv dari Kaggle (subreddit r/dankmemes)
Label:
- Populer (1) jika upvote_ratio >= 0.95
- Tidak Populer (0) jika kurang

Fitur yang digunakan:
- TF-IDF dari caption (max 500 fitur)
- num_comments (jumlah komentar)
- caption_length (panjang caption)
- word_count (jumlah kata dalam caption)
- has_me_when (cek apakah caption mengandung 'me', 'when', atau 'you')

3. Alur Pemrosesan
1. Load dan eksplorasi dataset
2. Buat label biner dari upvote_ratio
3. Tambahkan fitur baru (feature engineering)
4. Buat pipeline preprocessing (TF-IDF + scaler)
5. Uji 3 model (LogReg, RF, XGBoost)
6. Evaluasi dan analisis hasil

4. Hasil Performa Model

Logistic Regression:
- Accuracy: 0.57
- F1-score Populer: 0.72
- F1-score Tidak Populer: 0.05

Random Forest:
- Accuracy: 0.56
- F1-score Populer: 0.68
- F1-score Tidak Populer: 0.29

XGBoost:
- Accuracy: 0.52
- F1-score Populer: 0.60
- F1-score Tidak Populer: 0.38

5. Analisis dan Diskusi
- Logistic Regression sangat bias ke kelas populer, recall kelas tidak populer rendah.
- Random Forest menunjukkan distribusi prediksi lebih seimbang.
- XGBoost memberikan prediksi yang lebih adil terhadap kedua kelas, namun akurasi keseluruhan sedikit lebih rendah.

Tantangan utama adalah ketidakseimbangan data (label tidak seimbang) dan keterbatasan fitur teks.
Model kesulitan memahami meme tidak populer karena teks tidak cukup representatif.

6. Kesimpulan dan Saran
Model machine learning mampu digunakan untuk prediksi popularitas meme berbasis caption dan metadata,
namun performanya dapat ditingkatkan dengan:
- Teknik balancing data seperti SMOTE
- Penambahan fitur emosional dan semantik (emoji, sentimen lanjutan)
- Pendekatan multimodal (menggabungkan caption + gambar)

Visualisasi tambahan yang direkomendasikan:
- Bar chart distribusi label
- Confusion matrix dari masing-masing model
- Alur pipeline model (diagram dataset → preprocessing → model → evaluasi)

---
Disiapkan sebagai dokumentasi proyek UAS Machine Learning.
