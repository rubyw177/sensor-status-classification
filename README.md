# Laporan Proyek Machine Learning - Nama Anda

## Domain Proyek

Proyek ini menggunakan dataset dari kaggle yang berjudulkan "pump_sensor_data" yaitu dataset yang berisi nilai raw dari 52 sensor yang digunakan untuk memprediksi kegagalan sistem.

## Business Understanding

### Problem Statements

Berdasarkan latar belakang, berikut adalah rumusan masalah yang diangkat.
- Sensor manakah yang paling berpengaruh dalam kegagalan sistem?
- Model manakah yang memiliki akurasi paling tinggi untuk memprediksi kegagalan sistem?

### Goals

Untuk menjawab pertanyaan di atas, diperlukan goals sebagai berikut.
- Melakukan analisis korelasi pada sensor terhadap dengan status sistem.
- Membandingkan model SVM, Random Forest, dan XGBoost.

    ### Solution statements
    - Menggunakan dua model klasifikasi yaitu dengan menggunakan: 
        - Random Forest Classifier yang merupakan model ensemble dari decision trees yang ditrain secara paralel dan outputnya didapat melalui voting.
        - XGBoost yang merupakan model gradient boosting yang secara sekuensial membuat decision trees yang setiap treenya memperbaiki kesalahan   tree sebelumnya.
    - Menggunakan metrik seperti Confusion matrix pada test dataset, confusion matrix biasanya digunakan untuk metrik dari data yang memiliki multiclass label 

## Data Understanding
Data yang digunakan adalah data dari nilai raw oleh 52 sensor pada sistem pompa air di suatu kota kecil. [Pump Sensor Data](https://www.kaggle.com/datasets/nphantawee/pump-sensor-data/data).

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- Time stamp data: berisikan waktu saat data sensor diambil.
- Sensor data (52 series): berisikan nilai raw dari sensor.
- Machine status: berisikan status berjalan atau tidaknya sistem pada saat itu.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

