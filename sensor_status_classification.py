# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
import seaborn as sns

# %% [markdown]
# Load dataset from csv file

# %%
filename = "C:/Users/willi/Documents/William/Programming Tests/Python test/Dicoding ML Terapan/sensor_classification/dataset/sensor.csv"
df = pd.read_csv(filename)
df.head()

# %%
df.info()

# %%
df.describe()

# %% [markdown]
# Dapat dilihat pada beberapa sensor terdapat nilai minimal 0 dan NaN yang menandakan adanya missing values, selain itu kita juga perlu mendrop kolom yang tidak relevan untuk train model seperti timestamp dan kolom pertama karena kita hanya mengklasifikasikan bukan untuk analisis time series.

# %% [markdown]
# Pada code cell selanjutnya akan dilakukan pengedropan kolom yang tidak relevan

# %%
df.drop(columns=["Unnamed: 0", "timestamp"], inplace=True)
df.head()

# %% [markdown]
# Drop sensor_50 dan sensor_15 karena banyak missing valuesnya

# %%
df.drop(columns=["sensor_15", "sensor_50"], inplace=True)
df.head()

# %%
df.info()

# %% [markdown]
# Check banyaknya missing values di setiap column

# %%
df.isnull().sum()

# %%
missing_percentage = (df.isnull().sum() / len(df)) * 100
missing_percentage

# %% [markdown]
# Fill missing values dengan forward fill

# %%
df.fillna(inplace=True, method="ffill")
df.info()

# %% [markdown]
# Melakukan analisis fitur

# %%
label_df = df["machine_status"]
count = label_df.value_counts()
count_percent = 100 * label_df.value_counts(normalize=True)

feature_count_df = pd.DataFrame({
    "Jumlah": count,
    "Persentase": count_percent
}) 
print(feature_count_df)

# %%
label = count.sort_values(ascending=False)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
color_map = ['gray' for _ in range(len(df['machine_status'].value_counts()))]
color_map[0] = "#6abb41"

ax.bar(label.index, label, color=color_map, width=0.45)
ax.set_title("Data Feature Count", fontsize=15, fontweight='bold', position=(0.5, 1.0))

for i in label.index:
    ax.annotate(f"{label[i]}",
                xy=(i, label[i] + 4500),
                va='center', ha='center', color='#383838')
    
ax.set_xticklabels(label.index, fontsize=12, rotation=0)
plt.show()

# %% [markdown]
# Encode categorical data dengan pandas

# %%
encoded_df = pd.get_dummies(df, columns=["machine_status"])
encoded_df.head()

# %% [markdown]
# Check correlation between sensors and statuses

# %%
corr_matrix = encoded_df.corr().round(3)
corr_matrix.head()

# %%
plt.figure(figsize=(100, 100), dpi=100)
sns.heatmap(data=corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix", size=50)
plt.savefig('correlation_heatmap.png', dpi=72, bbox_inches='tight')

# %% [markdown]
# Berdasarkan korelasi di atas data sensor yang memiliki pengaruh kecil untuk ketiganya adalah sensor 13 - 37 dan 44 - 51. Oleh karena itu, kita akan drop kolom-kolom tersebut.

# %%
columns_to_drop = []
for i in range(13, 37+1):
    if i != 15: 
        columns_to_drop.append(f"sensor_{i}")

for i in range(44, 51+1):
    if i != 50: 
        columns_to_drop.append(f"sensor_{i}")

print(columns_to_drop)


# %%
encoded_df.drop(columns=columns_to_drop, inplace=True)
encoded_df.info()

# %% [markdown]
# Kemudian kita akan menggunakan PCA untuk mereduksi dimensi karena jumlah kolom sensor sangat banyak

# %%
from sklearn.decomposition import PCA

column_count = len(encoded_df.columns) - 3
pca = PCA(n_components=column_count)

# %%
pca_column = []
for i in encoded_df.columns:
    if i.startswith("sensor"):
        pca_column.append(i)

pca_column

# %%
pca.fit(encoded_df[pca_column])
princ_comp = pca.transform(encoded_df[pca_column])
pca.explained_variance_ratio_.round(3)

# %% [markdown]
# terdapat 93% informasi dan 3% informasi pada PC ke 1 dan 2, sehingga kali ini akan menggunakan 2 PC

# %%
pca = PCA(n_components=2)
pca.fit(encoded_df[pca_column])
princ_comp = pca.transform(encoded_df[pca_column])
princ_comp_df = pd.DataFrame(princ_comp, columns=["sensor_pca_1", "sensor_pca_2"])

# %%
# menambah hasil pca ke dataframe
pca_encoded_df = pd.concat([encoded_df, princ_comp_df], axis=1)
pca_encoded_df.head()

# %% [markdown]
# Split data to features and label

# %%
X = pca_encoded_df.loc[:, "sensor_pca_1":"sensor_pca_2"]
y = pca_encoded_df.loc[:, "machine_status_BROKEN":"machine_status_RECOVERING"]

# %%
X.info()

# %%
y.info()

# %% [markdown]
# Melakukan proses standarisasi untuk fitur

# %%
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)
X_standardized

# %%
from sklearn.model_selection import train_test_split

# Split data to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 3)

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

# %% [markdown]
# Karena distribusi data sangatlah tidak rata untuk setiap label, akan digunakan teknik oversampling untuk meningkatkan minoritas

# %%
# combine train data and take every class' features before oversampling
train_data = pd.concat([X_train, y_train], axis=1)

broken = train_data[train_data.machine_status_BROKEN==1]
recover = train_data[train_data.machine_status_RECOVERING==1]
normal = train_data[train_data.machine_status_NORMAL==1]

print(f'Total # of sample in broken class: {len(broken)}')
print(f'Total # of sample in recover class: {len(recover)}')
print(f'Total # of sample in normal class: {len(normal)}')

# %%
from sklearn.utils import resample

# Random oversampling
oversampled_broken_class = resample(
    broken,
    replace=True,
    n_samples=len(normal),
    random_state=3
)

oversampled_recover_class = resample(
    recover,
    replace=True,
    n_samples=len(normal),
    random_state=7
)

oversampled_combined_df = pd.concat([normal, oversampled_recover_class, oversampled_broken_class])
oversampled_combined_df.head()

# %%
normal_after = oversampled_combined_df[oversampled_combined_df.machine_status_NORMAL==1]
recover_after = oversampled_combined_df[oversampled_combined_df.machine_status_RECOVERING==1]
broken_after = oversampled_combined_df[oversampled_combined_df.machine_status_BROKEN==1]

print(f'Total # of sample in broken class: {len(broken_after)}')
print(f'Total # of sample in recover class: {len(recover_after)}')
print(f'Total # of sample in normal class: {len(normal_after)}')

# %%
X_train_resampled = oversampled_combined_df.loc[:, "sensor_pca_1":"sensor_pca_2"]
y_train_resampled = oversampled_combined_df.loc[:, "machine_status_BROKEN":"machine_status_RECOVERING"]

# %%
X_train.head()

# %%
y_train.head()

# %% [markdown]
# Setelah selesai memproses data untuk ditrain saatnya membuat model random forest, SVM, dan XGBoost dan membandingkan dengan metrik mse

# %%
from sklearn.metrics import mean_squared_error

# Siapkan dataframe untuk analisis model
models = pd.DataFrame(index=['train_mse', 'test_mse'], 
                      columns=['RandomForest', 'XGBoost'])

# %%
from sklearn.ensemble import RandomForestClassifier

rf_clf = RandomForestClassifier(n_estimators=150, max_depth=20, random_state=0)
rf_clf.fit(X_train_resampled, y_train_resampled)

models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred = rf_clf.predict(X_train_resampled), y_true=y_train_resampled)

# %%
# # Convert one hot encoded labels to label encoded
# y_train_label = np.argmax(y_train_resampled.values, axis=1)
# y_train_label

# %%
# from sklearn import svm

# svm_clf = svm.SVC(kernel="rbf", C=1.0, random_state=0)
# svm_clf.fit(X_train_resampled, y_train_label)

# models.loc['train_mse','SVM'] = mean_squared_error(y_pred = svm_clf.predict(X_train_resampled), y_true=y_train_label)

# %%
from xgboost import XGBClassifier

xgb_clf = XGBClassifier(n_estimators=150, max_depth=20, random_state=0)
xgb_clf.fit(X_train_resampled, y_train_resampled)

models.loc['train_mse','XGBoost'] = mean_squared_error(y_pred = xgb_clf.predict(X_train_resampled), y_true=y_train_resampled)

# %%
y_test_svm = np.argmax(y_test.values, axis=1)
models.loc['test_mse','RandomForest'] = mean_squared_error(y_pred = rf_clf.predict(X_test), y_true=y_test)
# models.loc['test_mse','SVM'] = mean_squared_error(y_pred = svm_clf.predict(X_test), y_true=y_test_svm)
models.loc['test_mse','XGBoost'] = mean_squared_error(y_pred = xgb_clf.predict(X_test), y_true=y_test)

# %%
models

# %% [markdown]
# Melihat hasil prediksi dengan metrik confusion matrix

# %%
from sklearn.metrics import confusion_matrix, classification_report

y_pred = rf_clf.predict(X_test)

y_pred_cm = np.argmax(y_pred, axis=1)
y_test_cm = np.argmax(y_test.values, axis=1)

y_pred_cm
y_test_cm
cm = confusion_matrix(y_test_cm, y_pred_cm)

print("Confusion Matrix RF:\n", cm)
print("\nRF Classification Report:\n", classification_report(y_test_cm, y_pred_cm))

# %%
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix RF')
plt.show()

# %%
# y_pred = svm_clf.predict(X_test)
# cm = confusion_matrix(y_test_svm, y_pred)

# print("Confusion Matrix SVM:\n", cm)
# print("\nSVM Classification Report:\n", classification_report(y_test_svm, y_pred))

# %%
# plt.figure(figsize=(8, 6))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.title('Confusion Matrix SVM')
# plt.show()

# %%
y_pred = xgb_clf.predict(X_test)
y_pred_cm = np.argmax(y_pred, axis=1)
y_test_cm = np.argmax(y_test.values, axis=1)

y_pred_cm
y_test_cm
cm = confusion_matrix(y_test_cm, y_pred_cm)

print("Confusion Matrix XGB:\n", cm)
print("\nXGB Classification Report:\n", classification_report(y_test_cm, y_pred_cm))

# %%
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix XGB')
plt.show()


