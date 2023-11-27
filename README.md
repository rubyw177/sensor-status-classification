# Laporan Proyek Machine Learning - Nama Anda

## Domain Proyek

Proyek ini memanfaatkan dataset yang diperoleh dari Kaggle dengan judul "pump_sensor_data". Dataset ini menyajikan nilai raw dari 52 sensor yang terpasang pada sistem pompa air, dan tujuan utama proyek adalah melakukan prediksi terhadap kemungkinan kegagalan sistem tersebut. Informasi dari sensor-sensor ini diharapkan dapat memberikan wawasan yang berguna dalam pemeliharaan dan manajemen sistem pompa air di suatu kota kecil. Dengan menganalisis data sensor ini, proyek ini bertujuan untuk mengidentifikasi pola atau karakteristik khusus yang dapat menjadi indikator potensial terjadinya kegagalan sistem. Dengan demikian, solusi yang dihasilkan dapat membantu dalam perawatan preventif dan peningkatan keandalan sistem pompa air tersebut.

## Business Understanding

### Problem Statements

Berdasarkan latar belakang, berikut adalah rumusan masalah yang diangkat.
- **Sensor manakah yang paling berpengaruh dalam kegagalan sistem?**
    Proyek akan menyelidiki sensor mana yang memiliki pengaruh paling signifikan terhadap terjadinya kegagalan sistem pada pompa air. Analisis ini dapat memberikan pemahaman mendalam tentang variabel yang paling sensitif terhadap kondisi sistem yang tidak normal.
- **Model manakah yang memiliki akurasi paling tinggi untuk memprediksi kegagalan sistem?**
    Evaluasi ini menjadi kunci untuk memilih algoritma yang paling sesuai dan andal dalam memberikan prediksi yang akurat terkait kondisi sistem pada proyek ini. Dengan demikian, hasil dari analisis ini diharapkan dapat memberikan wawasan berharga untuk pengelolaan dan perawatan sistem pompa air secara efisien.

### Goals

Untuk menjawab pertanyaan di atas, diperlukan goals sebagai berikut.
- Melakukan analisis korelasi pada sensor terhadap status sistem menjadi langkah kunci dalam pemahaman hubungan antara setiap sensor dengan kondisi sistem. Analisis korelasi akan membantu mengidentifikasi sensor-sensor yang memiliki keterkaitan kuat dengan kegagalan sistem, memberikan informasi berharga untuk penentuan fitur-fitur yang paling berpengaruh dalam pembuatan model. Hasil analisis ini dapat memberikan pandangan yang lebih mendalam tentang kontribusi masing-masing sensor terhadap kondisi operasional sistem.
- Membandingkan model Random Forest dan XGBoost akan melibatkan evaluasi performa keduanya dalam konteks pemodelan prediktif. Dengan memperbandingkan metrik-metrik seperti akurasi, presisi, recall, dan F1-score, proyek ini akan mengevaluasi keefektifan dan keandalan kedua model tersebut dalam memprediksi kegagalan sistem. Analisis ini tidak hanya akan memberikan wawasan tentang model mana yang memberikan hasil terbaik, tetapi juga dapat memberikan pandangan terhadap karakteristik khusus dari masing-masing algoritma, memungkinkan pemilihan model yang paling sesuai dengan kebutuhan proyek.

    ### Solution statements
    - Menggunakan dua model klasifikasi yaitu dengan menggunakan: 
        - Random Forest Classifier yang merupakan model ensemble dari decision trees yang ditrain secara paralel dan setiap tree akan menentukan kelasnya sendiri kemudian hasil prediksi didapat melalui voting dengan hasil class terbanyak.
        - XGBoost yang merupakan model gradient boosting yang secara sekuensial atau berurutan membuat sejumlah kecil decision trees, yang disebut weak learners. Pada setiap iterasi, XGBoost memberikan lebih banyak "perhatian" kepada data yang diidentifikasi sebagai kesalahan sebelumnya, sehingga meningkatkan performa secara bertahap.
    - Menggunakan metrik seperti Confusion matrix, akurasi, presisi, recall, dan F1-score (Classification Report) pada test dataset. confusion matrix biasanya digunakan untuk metrik dari data yang memiliki multiclass label karena memungkinkan analisis yang lebih rinci tentang performa model pada setiap kelas.

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
- Melakukan pengisian missing values dengan forward fill. Forward fill merupakan suatu metode pengisian nilai yang hilang dengan menggunakan nilai yang ada pada baris sebelumnya.Penggunaan forward fill biasanya relevan pada data yang memiliki urutan waktu (time series data) seperti pada dataset sensor ini. Dengan cara ini, data yang hilang dapat diisi dengan estimasi yang mungkin mendekati kondisi sebenarnya pada waktu yang bersamaan.
- Melakukan one hot encoding untuk keperluan training. One-hot encoding adalah suatu teknik dalam pengolahan data yang digunakan untuk mengubah variabel kategori menjadi representasi numerik biner. Hal ini diperlukan karena banyak model machine learning, terutama yang berbasis pada algoritma seperti Random Forest dan XGBoost, memerlukan input data dalam bentuk numerik.
- Melihat distribusi data pada label untuk menentukan apakah akan dilakukan oversampling atau undersampling pada data training sebelum melakukan proses pelatihan model.
![grafik label](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/labels.png)
Pada grafik tersebut dapat terlihat data untuk label NORMAL sangatlah banyak dan perlu dilakukan preprocessing agar distribusi antar label setara.

Berikut adalah tampilan pada dataset
| Unnamed: 0 | timestamp            | sensor_00 | sensor_01 | sensor_02 | sensor_03 | sensor_04 | sensor_05 | sensor_06 | sensor_07 | ...    | sensor_44 | sensor_45 | sensor_46 | sensor_47 | sensor_48 | sensor_49 | sensor_50 | sensor_51 | machine_status |
|------------|----------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------------|
| 0          | 2018-04-01 00:00:00 | 2.465394  | 47.09201  | 53.2118   | 46.31076  | 634.3750  | 76.45975  | 13.41146  | 16.13136  | ...    | 39.6412   | 65.68287  | 50.92593  | 38.19444  | 157.9861  | 67.70834  | 243.0556  | 201.3889  | NORMAL          |
| 1          | 2018-04-01 00:01:00 | 2.465394  | 47.09201  | 53.2118   | 46.31076  | 634.3750  | 76.45975  | 13.41146  | 16.13136  | ...    | 39.6412   | 65.68287  | 50.92593  | 38.19444  | 157.9861  | 67.70834  | 243.0556  | 201.3889  | NORMAL          |
| 2          | 2018-04-01 00:02:00 | 2.444734  | 47.35243  | 53.2118   | 46.39757  | 638.8889  | 73.54598  | 13.32465  | 16.03733  | ...    | 39.35185  | 65.39352  | 51.21528  | 38.19444  | 155.9606  | 67.12963  | 241.3194  | 203.7037  | NORMAL          |


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
Beginilah distribusi dari label pada dataset
|   Status    | Jumlah | Persentase   |
|-------------|--------|--------------|
| NORMAL      | 205836 | 93.4256%       |
| RECOVERING  | 14477  | 6.5700%        |
| BROKEN      | 7      | 0.0031%        |

Dapat dilihat distribusi dataset paling banyak adalah machine dengan status NORMAL. Untuk menyetarakan distribusinya, kita perlu melakukan proses oversampling pada status RECOVERING dan BROKEN. Kita tidak melakukan undersampling agar tidak mengurangi jumlah data yang ada, menurut saya undersampling baik digunakan apabila baris pada dataset berjumlah sekitar satu juta.

Dengan teknik PCA, standarisasi, dan oversampling, didapatkan dataframe akhir seperti ini.
|   sensor_pca_1   |   sensor_pca_2   |   machine_status_BROKEN   |   machine_status_NORMAL   |   machine_status_RECOVERING   |
|-------------------|-------------------|---------------------------|---------------------------|-------------------------------|
|    -51.571332     |    -1.687069      |              0            |             1             |                0              |
|    -32.981869     |   -21.536421      |              0            |             1             |                0              |
|    -37.910068     |    -3.861386      |              0            |             1             |                0              |
|    -38.191263     |    -0.295439      |              0            |             1             |                0              |
|    -39.493727     |    -9.400861      |              0            |             1             |                0              |



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

Metrik-metrik pada Classification Report:
| Metric                   | Formula                                                   | Description                                      |
|--------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **Accuracy**             | $$(\frac{TP + TN}{TP + FP + FN + TN}).$$                      | Tingkat kebenaran keseluruhan dari model.         |
| **Precision**            | $$(\frac{TP}{TP + FP}).$$                                  | Proporsi identifikasi positif yang sebenarnya benar.|
| **Recall (Sensitivity)** | $$(\frac{TP}{TP + FN}).$$                                    | Proporsi positif sebenarnya yang diidentifikasi dengan benar.|
| **Specificity**          | $$(\frac{TN}{TN + FP}).$$                                  | Proporsi negatif sebenarnya yang diidentifikasi dengan benar.|
| **F1 Score**             | $$(\frac{2 \cdot (Precision \cdot Recall)}{Precision + Recall}).$$ | Ukuran seimbang antara presisi dan recall.       |


Akurasi mengukur tingkat kebenaran keseluruhan dari model, sementara presisi menilai proporsi identifikasi positif yang sebenarnya benar. Recall mengindikasikan proporsi positif sebenarnya yang diidentifikasi dengan benar, dan spesifisitas mencerminkan proporsi negatif sebenarnya yang diidentifikasi secara akurat. Metrik-metrik ini memberikan gambaran komprehensif tentang performa sebuah pengklasifikasi dalam memahami seberapa baik model dapat membedakan antara kelas positif dan negatif.

Hasil dari metrik ini menunjukkan model Random Forest memiliki False Positive dan False Negative yang lebih kecil dibandingkan dengan model XGBoost.

![conf_matrix2](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/conf_matrix2.png)
Correlation matrix model Random Forest.

![rf](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/conf_matrix.png)
Correlation matrix model XGBoost.

## Conclusion
- Sensor yang paling berdampak pada prediksi adalah sensor_0 sampai dengan sensor_12.
- Model dengan akurasi yang paling baik berdasarkan kode dalam repository ini adalah RandomForest.