# Laporan Proyek Machine Learning - William Kester Hermawan

## Domain Proyek

Motivasi di balik proyek ini adalah untuk memastikan keandalan sistem pompa air di kota-kota kecil dengan mengatasi potensi kegagalan. Sangat penting bagi masyarakat untuk memiliki akses terhadap pasokan air yang stabil, yang pada gilirannya menekankan pentingnya menjaga keandalan sistem pompa air. Sistem pompa air yang rusak dapat menyebabkan gejolak yang signifikan, sehingga mengakibatkan terganggunya pasokan air yang dapat berdampak besar pada kehidupan sehari-hari. Untuk mencegah kejadian seperti itu, fokus inisiatif ini adalah memanfaatkan data yang diperoleh dari sensor-sensor tersebut untuk mengantisipasi potensi malfungsi sistem.

Analisis data sensor dapat dilakukan untuk mengidentifikasi pola atau karakteristik khusus yang mungkin mengindikasikan kesalahan. Dengan pemahaman yang lebih baik mengenai kegagalan sistem, solusi dari proyek ini diharapkan dapat mendukung upaya pemeliharaan preventif dan meningkatkan keandalan sistem pompa air. Dengan kata lain, proyek ini bertujuan tidak hanya untuk merespon kesalahan yang sudah terjadi, tetapi juga  mencegahnya dengan merekam tanda atau pola yang dapat diidentifikasi melalui data sensor. Hal ini akan membantu  mengoptimalkan sistem pengelolaan dan pemeliharaan, meningkatkan efisiensi dan dengan demikian memberikan manfaat yang lebih besar bagi masyarakat yang menggunakan layanan  air tersebut.

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

### Variabel-variabel pada water pump sensor dataset adalah sebagai berikut:
- Time stamp data: berisikan waktu saat data sensor diambil.
- Sensor data (52 series): berisikan nilai raw dari sensor.
- Machine status: berisikan status berjalan atau tidaknya sistem pada saat itu.

### Exploratory Analysis
Setiap kolom terdiri dari dua ratus ribu lebih entri.
|   Column          | Non-Null Count | Dtype   |
|-------------------|----------------|---------|
| Unnamed: 0        | 220320         | int64   |
| timestamp         | 220320         | object  |
| sensor_00         | 210112         | float64 |
| sensor_01         | 219951         | float64 |
| sensor_02         | 220301         | float64 |
| sensor_03         | 220301         | float64 |
| sensor_04         | 220301         | float64 |
| sensor_05         | 220301         | float64 |
| sensor_06         | 215522         | float64 |
| sensor_07         | 214869         | float64 |
| sensor_08         | 215213         | float64 |
| sensor_09         | 215725         | float64 |
| sensor_10         | 220301         | float64 |
| sensor_11         | 220301         | float64 |
| sensor_12         | 220301         | float64 |
| sensor_13         | 220301         | float64 |
| sensor_14         | 220299         | float64 |
| **sensor_15**         | **0**              | float64 |
| sensor_16         | 220289         | float64 |
| sensor_17         | 220274         | float64 |
| sensor_18         | 220274         | float64 |
| sensor_19         | 220304         | float64 |
| sensor_20         | 220304         | float64 |
| sensor_21         | 220304         | float64 |
| sensor_22         | 220279         | float64 |
| sensor_23         | 220304         | float64 |
| sensor_24         | 220304         | float64 |
| sensor_25         | 220284         | float64 |
| sensor_26         | 220300         | float64 |
| sensor_27         | 220304         | float64 |
| sensor_28         | 220304         | float64 |
| sensor_29         | 220248         | float64 |
| sensor_30         | 220059         | float64 |
| sensor_31         | 220304         | float64 |
| sensor_32         | 220252         | float64 |
| sensor_33         | 220304         | float64 |
| sensor_34         | 220304         | float64 |
| sensor_35         | 220304         | float64 |
| sensor_36         | 220304         | float64 |
| sensor_37         | 220304         | float64 |
| sensor_38         | 220293         | float64 |
| sensor_39         | 220293         | float64 |
| sensor_40         | 220293         | float64 |
| sensor_41         | 220293         | float64 |
| sensor_42         | 220293         | float64 |
| sensor_43         | 220293         | float64 |
| sensor_44         | 220293         | float64 |
| sensor_45         | 220293         | float64 |
| sensor_46         | 220293         | float64 |
| sensor_47         | 220293         | float64 |
| sensor_48         | 220293         | float64 |
| sensor_49         | 220293         | float64 |
| **sensor_50**         | **143303**         | float64 |
| sensor_51         | 204937         | float64 |
| machine_status    | 220320         | object  |

Dapat dilihat pada tabel sebelumnya terdapat banyak kolom yang jumlah valuenya tidak sama dengan satu sama lain. Selain itu, kolom sensor_15 memiliki nilai 0 dari non null count yang artinya pada sensor_15 tidak terdapat nilai sama sekali. Kemudian pada sensor_50 juga terdapat banyak sekali missing values. Oleh karena itu, dapat dilakukan pengedropan kepada dua kolom tersebut. Alhasil, didapatkan data sebagai berikut.

|   Column         | Non-Null Count | Dtype   |
|------------------|----------------|---------|
| sensor_00        | 210112         | float64 |
| sensor_01        | 219951         | float64 |
| sensor_02        | 220301         | float64 |
| sensor_03        | 220301         | float64 |
| sensor_04        | 220301         | float64 |
| sensor_05        | 220301         | float64 |
| sensor_06        | 215522         | float64 |
| sensor_07        | 214869         | float64 |
| sensor_08        | 215213         | float64 |
| sensor_09        | 215725         | float64 |
| sensor_10        | 220301         | float64 |
| sensor_11        | 220301         | float64 |
| sensor_12        | 220301         | float64 |
| sensor_13        | 220301         | float64 |
| sensor_14        | 220299         | float64 |
| sensor_16        | 220289         | float64 |
| sensor_17        | 220274         | float64 |
| sensor_18        | 220274         | float64 |
| sensor_19        | 220304         | float64 |
| sensor_20        | 220304         | float64 |
| sensor_21        | 220304         | float64 |
| sensor_22        | 220279         | float64 |
| sensor_23        | 220304         | float64 |
| sensor_24        | 220304         | float64 |
| sensor_25        | 220284         | float64 |
| sensor_26        | 220300         | float64 |
| sensor_27        | 220304         | float64 |
| sensor_28        | 220304         | float64 |
| sensor_29        | 220248         | float64 |
| sensor_30        | 220059         | float64 |
| sensor_31        | 220304         | float64 |
| sensor_32        | 220252         | float64 |
| sensor_33        | 220304         | float64 |
| sensor_34        | 220304         | float64 |
| sensor_35        | 220304         | float64 |
| sensor_36        | 220304         | float64 |
| sensor_37        | 220304         | float64 |
| sensor_38        | 220293         | float64 |
| sensor_39        | 220293         | float64 |
| sensor_40        | 220293         | float64 |
| sensor_41        | 220293         | float64 |
| sensor_42        | 220293         | float64 |
| sensor_43        | 220293         | float64 |
| sensor_44        | 220293         | float64 |
| sensor_45        | 220293         | float64 |
| sensor_46        | 220293         | float64 |
| sensor_47        | 220293         | float64 |
| sensor_48        | 220293         | float64 |
| sensor_49        | 220293         | float64 |
| sensor_51        | 204937         | float64 |
| machine_status   | 220320         | object  |

Kemudian akan melakukan perhitungan jumlah missing values pada setiap kolom dan didapatkan hasil seperti tabel di bawah.

| Kolom       | Missing Value |
|-----------------|-------|
| sensor_00       | 10208 |
| sensor_01       | 369   |
| sensor_02       | 19    |
| sensor_03       | 19    |
| sensor_04       | 19    |
| sensor_05       | 19    |
| sensor_06       | 4798  |
| sensor_07       | 5451  |
| sensor_08       | 5107  |
| sensor_09       | 4595  |
| sensor_10       | 19    |
| sensor_11       | 19    |
| sensor_12       | 19    |
| sensor_13       | 19    |
| sensor_14       | 21    |
| sensor_16       | 31    |
| sensor_17       | 46    |
| sensor_18       | 46    |
| sensor_19       | 16    |
| sensor_20       | 16    |
| sensor_21       | 16    |
| sensor_22       | 41    |
| sensor_23       | 16    |
| sensor_24       | 16    |
| sensor_25       | 36    |
| sensor_26       | 20    |
| sensor_27       | 16    |
| sensor_28       | 16    |
| sensor_29       | 72    |
| sensor_30       | 261   |
| sensor_31       | 16    |
| sensor_32       | 68    |
| sensor_33       | 16    |
| sensor_34       | 16    |
| sensor_35       | 16    |
| sensor_36       | 16    |
| sensor_37       | 16    |
| sensor_38       | 27    |
| sensor_39       | 27    |
| sensor_40       | 27    |
| sensor_41       | 27    |
| sensor_42       | 27    |
| sensor_43       | 27    |
| sensor_44       | 27    |
| sensor_45       | 27    |
| sensor_46       | 27    |
| sensor_47       | 27    |
| sensor_48       | 27    |
| sensor_49       | 27    |
| sensor_51       | 15383 |
| machine_status  | 0     |

Selanjutnya dilakukan analisis korelasi untuk melihat sensor mana yang memiliki "efek" yang signifikan dan mana yang tidak signifikan
![correlation matrix](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/corr_matrix_zoomed.png)
Dapat dilihat dari correlation matrix tersebut, terlihat sensor yang memberi efek signifikan terhadap ketiga status adalah sensor_0 sampai dengan sensor_12 dan untuk status broken terlihat sensor yang paling berdampak adalah sensor_44 sampai sensor 51.

Kemudian akan dilihat distribusi data label untuk menentukan apakah perlu dilakukan oversampling atau undersampling pada data training sebelum melakukan proses pelatihan model.
![grafik label](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/labels.png)
Pada grafik tersebut dapat terlihat data untuk label NORMAL sangatlah banyak sehingga perlu dilakukan teknik resampling agar distribusi label menjadi rata atau jumlah data pada setiap class menjadi sama.

Berikut adalah tampilan pada dataset
| Unnamed: 0 | timestamp            | sensor_00 | sensor_01 | sensor_02 | sensor_03 | sensor_04 | sensor_05 | sensor_06 | sensor_07 | ...    | sensor_44 | sensor_45 | sensor_46 | sensor_47 | sensor_48 | sensor_49 | sensor_50 | sensor_51 | machine_status |
|------------|----------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------------|
| 0          | 2018-04-01 00:00:00 | 2.465394  | 47.09201  | 53.2118   | 46.31076  | 634.3750  | 76.45975  | 13.41146  | 16.13136  | ...    | 39.6412   | 65.68287  | 50.92593  | 38.19444  | 157.9861  | 67.70834  | 243.0556  | 201.3889  | NORMAL          |
| 1          | 2018-04-01 00:01:00 | 2.465394  | 47.09201  | 53.2118   | 46.31076  | 634.3750  | 76.45975  | 13.41146  | 16.13136  | ...    | 39.6412   | 65.68287  | 50.92593  | 38.19444  | 157.9861  | 67.70834  | 243.0556  | 201.3889  | NORMAL          |
| 2          | 2018-04-01 00:02:00 | 2.444734  | 47.35243  | 53.2118   | 46.39757  | 638.8889  | 73.54598  | 13.32465  | 16.03733  | ...    | 39.35185  | 65.39352  | 51.21528  | 38.19444  | 155.9606  | 67.12963  | 241.3194  | 203.7037  | NORMAL          |


## Data Preparation
Pada bagian data preparation dilakukan beberapa metode preprocessing sebelum memasukan data training pada model seperti:
- **Forward Fill**
    - Melakukan pengisian missing values dengan forward fill. Forward fill merupakan suatu metode pengisian nilai yang hilang dengan menggunakan nilai yang ada pada baris sebelumnya.Penggunaan forward fill biasanya relevan pada data yang memiliki urutan waktu (time series data) seperti pada dataset sensor ini. Dengan cara ini, data yang hilang dapat diisi dengan estimasi yang mungkin mendekati kondisi sebenarnya pada waktu yang bersamaan.
- **Encoding**
    - Melakukan one hot encoding untuk keperluan training. One-hot encoding adalah suatu teknik dalam pengolahan data yang digunakan untuk mengubah variabel kategori menjadi representasi numerik biner. Hal ini diperlukan karena banyak model machine learning, terutama yang berbasis pada algoritma seperti Random Forest dan XGBoost, memerlukan input data dalam bentuk numerik.

Beginilah hasilnya setelah dilakukan forward fill dan juga one hot encoding pada label
|   Column                     | Non-Null Count | Dtype   |
|----------------------------- | -------------- | ------- |
| sensor_00                   | 220320         | float64 |
| sensor_01                   | 220320         | float64 |
| sensor_02                   | 220320         | float64 |
| sensor_03                   | 220320         | float64 |
| sensor_04                   | 220320         | float64 |
| sensor_05                   | 220320         | float64 |
| sensor_06                   | 220320         | float64 |
| sensor_07                   | 220320         | float64 |
| sensor_08                   | 220320         | float64 |
| sensor_09                   | 220320         | float64 |
| sensor_10                   | 220320         | float64 |
| sensor_11                   | 220320         | float64 |
| sensor_12                   | 220320         | float64 |
| sensor_38                   | 220320         | float64 |
| sensor_39                   | 220320         | float64 |
| sensor_40                   | 220320         | float64 |
| sensor_41                   | 220320         | float64 |
| sensor_42                   | 220320         | float64 |
| sensor_43                   | 220320         | float64 |
| machine_status_BROKEN       | 220320         | uint8   |
| machine_status_NORMAL       | 220320         | uint8   |
| machine_status_RECOVERING   | 220320         | uint8   |

- **Pereduksian dimensi dengan PCA**
    - Melakukan PCA atau pereduksian dimensi pada fitur (sensor_0 - sensor terakhir pada data). Pada tahapan ini dilakukan pereduksian dimensi dengan jumlah komponen sebanyak dua. Pereduksian dimensi dilakukan karena data fitur sangat banyak yaitu bisa mencapai 14 fitur setelah dilakukan pengedropan kolom yang tidak begitu relevan. Pada data ini, hanya digunakan 2 PC saja karena informasi-informasi yang paling relevan terdapat pada komponen pertama dan kedua saja

Berikut adalah data hasil PCA
|   Column       | Non-Null Count | Dtype   |
|--------------  | -------------- | ------- |
| sensor_pca_1   | 220320         | float64 |
| sensor_pca_2   | 220320         | float64 |

- **Pembagian data training dan test**
    - Setelah melakukan PCA, dilakukan pembagian dataset train dan test dengan perbandingan 80:20 menggunakan fungsi train_test_split dari sklearn. Pemilihan 80:20 dilakukan karena merupakan rasio standar dalam pembagian dataset. Didapatkan pembagian sebagai berikut.
```
Total # of sample in whole dataset: 220320
Total # of sample in train dataset: 176256
Total # of sample in test dataset: 44064
```
- **Standarisasi**
    - Kemudian dilakukan juga Standarisasi dengan StandardScaler, alasan dilakukan standarisasi bukan normalisasi karena setiap fitur pada dataset mengandung besaran dan skala yang berbeda-beda.
- **Oversampling**
    - Setelah itu dilakukan oversampling untuk menambah jumlah data pada label yang merupakan minoritas agar sama dengan minoritas jumlahnya (BROKEN status dan RECOVERING status), hal ini dilakukan agar akurasi prediksi dari model dapat meningkat karena tidak hanya terlatih pada satu label saja. Untuk melakukan oversampling digunakan fungsi resample() dari library sklearn. Dapat dilihat pada tabel distribusi di bawah, label yang paling banyak adalah machine dengan status NORMAL. Untuk menyetarakan distribusinya, dilakukan proses oversampling pada status RECOVERING dan BROKEN. Undersampling tidak dilakukan agar tidak mengurangi jumlah data yang ada, ndersampling baik digunakan apabila baris pada dataset berjumlah sekitar satu juta.

Beginilah distribusi dari label pada dataset
|   Status    | Jumlah | Persentase   |
|-------------|--------|--------------|
| NORMAL      | 205836 | 93.4256%       |
| RECOVERING  | 14477  | 6.5700%        |
| BROKEN      | 7      | 0.0031%        |


Dengan teknik PCA, standarisasi, dan oversampling, didapatkan dataframe akhir seperti ini.
|   sensor_pca_1   |   sensor_pca_2   |   machine_status_BROKEN   |   machine_status_NORMAL   |   machine_status_RECOVERING   |
|-------------------|-------------------|---------------------------|---------------------------|-------------------------------|
|    -51.571332     |    -1.687069      |              0            |             1             |                0              |
|    -32.981869     |   -21.536421      |              0            |             1             |                0              |
|    -37.910068     |    -3.861386      |              0            |             1             |                0              |
|    -38.191263     |    -0.295439      |              0            |             1             |                0              |
|    -39.493727     |    -9.400861      |              0            |             1             |                0              |

Distribusi data pada setiap label juga telah sama
```
Total # of sample in broken class: 164621
Total # of sample in recover class: 164621
Total # of sample in normal class: 164621
```

## Modeling
Pada tahapan modeling, digunakan dua jenis model yaitu Random Forest Classifier dengan parameter sebagai berikut,
```
n_estimators=150
max_depth=20
```
"n_estimators" merupakan banyaknya tree atau pohon yang dapat dibuat oleh model sedangkan "max_depth" merupakan kedalaman atau banyaknya cabang dari pohon atau tree.

Parameter yang sama digunakan juga untuk model XGBoost
```
n_estimators=150
max_depth=20
```
Di tahap ini, akan dibandingkan performa dari model hasil bagging dan model hasil boosting (khususnya gradient boosting). Alasan dipilihnya kedua model tersebut karena model-model tersebut merupakan penggabungan dari model-model seperti decision tree sehingga performa dan kecepatan yang tinggi dalam melakukan prediksi. Selain itu juga, kedua model tersebut tidak dapat mengatasi masalah imbalanced class seperti yang dialami pada dataset yang dipakai sekarang ini. 

Pada saat training, model XGBoost memiliki waktu training yang jauh lebih cepat (10,7 s) daripada waktu training dari model Random Forest (1 menit lebih). Dari kedua algoritma ini hasil prediksi (dengan jumlah tree dan max depth yang sama), algoritma Random Forest memiliki tingkat kesalahan prediksi yang lebih kecil daripada XGBoost walaupun waktu trainingnya jauh lebih lama.

## Evaluation
Untuk tahap evaluasi digunakan metrik confusion matrix yang cocok digunakan pada kasus klasifikasi. Confusion matrix sendiri merupakan matriks yang terdiri dari jumlah false positive, false negative, true positive, dan true negative. 

- True Positive (TP): Jumlah instansi yang diprediksi dengan **benar** sebagai positif.
- False Positive (FP): Jumlah instansi yang diprediksi dengan **salah** yang harusnya negatif tetapi hasil prediksi positif.
- False Negative (FN): Jumlah instansi yang diprediksi dengan **salah** yang harusnya positif tetapi hasil prediksi negatif.
- True Negative (TN): Jumlah instansi yang diprediksi dengan **benar** sebagai negatif.

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

Hasil dari metrik ini menunjukkan model Random Forest memiliki False Positive dan False Negative yang lebih kecil dibandingkan dengan model XGBoost. Dengan kata lain model Random Forest **lebih cenderung tidak memberikan sinyal palsu/false alarm** daripada model XGBoost. Oleh karena nilai dari FP dan FN yang kecil serta TN dan TF yang besar pada model Random Forest, metrik pada classification report seperti akurasi, presisi, recall, specificity, dan F1 score juga akan lebih baik dibandingkan dengan metrik classification report pada model XGBoost. Untuk kasus predictive maintainance pada water pump plant ini, diperlukan model yang memiliki FN dan FP yang serendah mungkin agar terhindar dari false alarm (false alarm dapat membuang resource dan waktu) serta TN dan TF yang tinggi agar dengan tepat dapat menghindari problem yang akan terjadi sehingga plant akan andal.

![conf_matrix2](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/conf_matrix2.png)
Correlation matrix model Random Forest.

![rf](https://github.com/rubyw177/sensor-status-classification/blob/9cfb1dc4a003ba1eba047f8420e530f97eedf8de/images/conf_matrix.png)
Correlation matrix model XGBoost.

## Conclusion
- Sensor yang paling berdampak pada prediksi adalah sensor_0 sampai dengan sensor_12.
- Model dengan akurasi yang paling baik berdasarkan hasil pada repository ini adalah Random Forest.

