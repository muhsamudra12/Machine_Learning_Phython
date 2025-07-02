
# Prediksi Popularitas Meme Berdasarkan Caption dan Metadata Menggunakan Machine Learning

**Nama:** [Muhammad Afrille Samudra]  
**NIM:** [A11.2023.15200]  
**Kelas:** [A11.4402]  

---

## 1. Ringkasan dan Tujuan

Proyek ini bertujuan untuk memprediksi popularitas meme berdasarkan teks caption dan metadata numerik.  
Permasalahan: belum ada model prediktif sederhana berbasis teks untuk mengukur popularitas meme.  
Tujuan: membuat pipeline machine learning yang mampu membedakan meme populer dan tidak populer.

**Model yang digunakan:**
- Logistic Regression (baseline)
- Random Forest (non-linear model)
- XGBoost (boosted tree)

---

## 2. Dataset dan Fitur

**Dataset:** `dankmemes_top_1000.csv` (Kaggle, subreddit r/dankmemes)  
**Label:**
- Populer (1) jika `upvote_ratio >= 0.95`
- Tidak Populer (0) jika kurang

**Fitur:**
- TF-IDF dari caption (max 500 fitur)
- `num_comments`
- `caption_length`
- `word_count`
- `has_me_when` (apakah caption mengandung kata 'me', 'when', atau 'you')

---

## 3. Alur Pemrosesan

1. Load dan eksplorasi dataset  
2. Buat label biner dari `upvote_ratio`  
3. Tambahkan fitur tambahan  
4. Pipeline preprocessing (TF-IDF + scaler)  
5. Modeling dengan 3 algoritma  
6. Evaluasi dan analisis hasil  

---

## 4. Hasil Performa Model

| Model               | Accuracy | F1-score Populer | F1-score Tidak Populer |
|---------------------|----------|------------------|-------------------------|
| Logistic Regression | 0.57     | 0.72             | 0.05                    |
| Random Forest       | 0.56     | 0.68             | 0.29                    |
| XGBoost             | 0.52     | 0.60             | 0.38                    |

---

## 5. Analisis dan Diskusi

- Logistic Regression sangat bias ke kelas populer (F1 rendah untuk tidak populer).  
- Random Forest memberikan prediksi yang lebih seimbang.  
- XGBoost relatif stabil di kedua kelas namun dengan akurasi total sedikit lebih rendah.  

**Tantangan:** ketidakseimbangan data dan keterbatasan fitur teks menyebabkan model kesulitan mengenali meme tidak populer.

---

## 6. Kesimpulan dan Saran

Model machine learning mampu digunakan untuk prediksi popularitas meme berbasis caption dan metadata.  
**Saran pengembangan lanjutan:**
- Teknik balancing (SMOTE, resampling)
- Penambahan fitur semantik dan emosional (emoji, sentimen lanjut)
- Pendekatan multimodal (menggabungkan teks + gambar)

---

*Dokumentasi Proyek UAS Machine Learning*
