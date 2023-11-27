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
- Membandingkan model Random Forest dan XGBoost.

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

### Exploratory Analysis
Pada dataset terdapat banyak missing values pada kolom sensor dan terdapat satu kolom sensor yang bernilai nol pada setiap barisnya, dan masih banyak lagi hal-hal yang harus dibersihkan seperti:
- Mendrop kolom yang tidak bergitu relevan dalam proses prediksi, kolom-kolom tersebut dapat dilihat dengan correlation matrix di bawah
![correlation matrix](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/corr_matrix_zoomed.png)
- Melakukan pengisian missing values dengan forward fill
- Melakukan one hot encoding untuk keperluan training 
- Melihat distribusi data pada label
![grafik label](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/labels.png)
Pada grafik tersebut dapat terlihat data untuk label NORMAL sangatlah banyak dan perlu dilakukan preprocessing agar distribusi antar label setara.

## Data Preparation
Pada bagian data preparation dilakukan beberapa metode preprocessing sebelum memasukan data training pada model seperti:
- Melakukan PCA atau pereduksian dimensi pada fitur (sensor_0 - sensor terakhir pada data). Pada tahapan ini dilakukan pereduksian dimensi dengan jumlah komponen sebanyak dua. Pereduksian dimensi dilakukan karena data fitur sangat banyak yaitu bisa mencapai 14 fitur setelah dilakukan pengedropan kolom yang tidak begitu relevan.
```python
pca = PCA(n_components=2)
pca.fit(encoded_df[pca_column])
princ_comp = pca.transform(encoded_df[pca_column])
princ_comp_df = pd.DataFrame(princ_comp, columns=["sensor_pca_1", "sensor_pca_2"])
```
- Setelah melakukan PCA, dilakukan pembagian dataset train dan test dengan perbandingan 80:20 menggunakan fungsi train_test_split dari sklearn. Pemilihan 80:20 dilakukan karena merupakan rasio standar dalam pembagian dataset.
- Kemudian dilakukan juga Standarisasi dengan StandardScaler, alasan dilakukan standarisasi bukan normalisasi karena setiap fitur pada dataset mengandung besaran dan skala yang berbeda-beda.
- Setelah itu dilakukan oversampling untuk menambah jumlah data pada label yang merupakan minoritas agar sama dengan minoritas jumlahnya (BROKEN status dan RECOVERING status), hal ini dilakukan agar akurasi prediksi dari model dapat meningkat karena tidak hanya terlatih pada satu label saja. Untuk melakukan oversampling digunakan fungsi resample() dari library sklearn
```python
oversampled_broken_class = resample(
    broken,
    replace=True,
    n_samples=len(normal),
    random_state=3
)
```

## Modeling
Pada tahapan modeling, digunakan dua jenis model yaitu Random Forest Classifier dan XGBoost Classifier.
- Pada saat training, model XGBoost memiliki waktu training yang jauh lebih cepat (10,7 s) daripada waktu training dari model Random Forest (1 menit lebih)
- Dari kedua algoritma ini hasil prediksi (dengan jumlah tree dan max depth yang sama), algoritma Random Forest memiliki tingkat kesalahan prediksi yang lebih kecil daripada XGBoost walaupun waktu trainingnya jauh lebih lama.

## Evaluation
Untuk tahap evaluasi digunakan metrik confusion matrix yang cocok digunakan pada kasus klasifikasi. Confusion matrix sendiri merupakan matriks yang terdiri dari jumlah false positive, false negative, true positive, dan true negative. 

- True Positive (TP): Jumlah instansi yang diprediksi dengan benar sebagai positif.
- False Positive (FP): Jumlah instansi yang diprediksi sebagai positif padahal sebenarnya negatif.
- False Negative (FN): Jumlah instansi yang diprediksi sebagai negatif padahal sebenarnya positif.
- True Negative (TN): Jumlah instansi yang diprediksi dengan benar sebagai negatif.

|                    | Actual Positive               | Actual Negative               |
|--------------------|-------------------------------|-------------------------------|
| Predicted Positive | TP (True Positive)            | FP (False Positive)           |
| Predicted Negative | FN (False Negative)           | TN (True Negative)            |


| Metric                   | Formula                                                   | Description                                      |
|--------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **Accuracy**             | $$ \frac{TP + TN}{TP + FP + FN + TN} $$                   | Tingkat kebenaran keseluruhan dari model.         |
| **Precision**            | $$ \frac{TP}{TP + FP} $$                                  | Proporsi identifikasi positif yang sebenarnya benar.|
| **Recall (Sensitivity)** | $$ \frac{TP}{TP + FN} $$                                  | Proporsi positif sebenarnya yang diidentifikasi dengan benar.|
| **Specificity**          | $$ \frac{TN}{TN + FP} $$                                  | Proporsi negatif sebenarnya yang diidentifikasi dengan benar.|
| **F1 Score**             | $$ \frac{2 \cdot (Precision \cdot Recall)}{Precision + Recall} $$ | Ukuran seimbang antara presisi dan recall.       |


Akurasi mengukur tingkat kebenaran keseluruhan dari model, sementara presisi menilai proporsi identifikasi positif yang sebenarnya benar. Recall mengindikasikan proporsi positif sebenarnya yang diidentifikasi dengan benar, dan spesifisitas mencerminkan proporsi negatif sebenarnya yang diidentifikasi secara akurat. Metrik-metrik ini memberikan gambaran komprehensif tentang performa sebuah pengklasifikasi dalam memahami seberapa baik model dapat membedakan antara kelas positif dan negatif.

Hasil dari metrik ini menunjukkan model Random Forest memiliki False Positive dan False Negative yang lebih kecil dibandingkan dengan model XGBoost.

![conf_matrix2](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/conf_matrix2.png)
Correlation matrix model Random Forest.

![rf](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/conf_matrix.png)
Correlation matrix model XGBoost.

## Conclusion
- Sensor yang paling berdampak pada prediksi adalah sensor_0 sampai dengan sensor_12.
- Model dengan akurasi yang paling baik berdasarkan kode dalam repository ini adalah RandomForest.

