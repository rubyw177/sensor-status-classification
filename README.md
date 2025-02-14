# Machine Learning Project Report - William Kester Hermawan

## Project Domain

The motivation behind this project is to ensure the reliability of water pump systems in small cities by addressing potential failures. It is essential for communities to have stable water supplies, which underscores the importance of maintaining the reliability of water pump systems. A malfunctioning pump system can cause significant disruptions, leading to water supply interruptions that can have a substantial impact on daily life. To prevent such occurrences, this initiative focuses on leveraging sensor data to anticipate potential system malfunctions.

Analyzing sensor data can help identify patterns or specific characteristics that may indicate failures. With a better understanding of system failures, this project aims to support preventive maintenance efforts and improve the reliability of water pump systems. In other words, this project is not just about responding to failures that have already occurred but also preventing them by identifying patterns or warning signs from sensor data. This will help optimize system management and maintenance, increase efficiency, and ultimately provide greater benefits to communities that rely on these water services.

## Business Understanding

### Problem Statements

Based on the background, the following problem statements are addressed:
- **Which sensors have the most significant impact on system failures?**
  The project will investigate which sensors have the most influence on system failures in water pumps. This analysis will provide deeper insights into the variables most sensitive to abnormal system conditions.
- **Which model has the highest accuracy in predicting system failures?**
  This evaluation is crucial for selecting the most suitable and reliable algorithm to provide accurate predictions of system conditions. The results of this analysis are expected to offer valuable insights into efficient water pump system management and maintenance.

### Goals

To answer the questions above, the following goals are set:
- Conduct correlation analysis between sensors and system status to understand the relationship between each sensor and system conditions. This analysis will help identify the sensors that are strongly linked to system failures, providing valuable information for determining the most impactful features in model development. The results of this analysis will offer deeper insights into the contribution of each sensor to system operations.
- Compare the performance of **Random Forest** and **XGBoost** in predictive modeling. By evaluating metrics such as accuracy, precision, recall, and F1-score, this project will assess the effectiveness and reliability of both models in predicting system failures. This analysis will not only determine which model yields the best results but also offer insights into the unique characteristics of each algorithm, enabling the selection of the most suitable model for the project.

### Solution Statements

- Implementing two classification models:
  - **Random Forest Classifier**, an ensemble model of decision trees trained in parallel. Each tree makes its own classification, and the final prediction is determined through a majority vote.
  - **XGBoost**, a gradient boosting model that sequentially creates a series of small decision trees (weak learners). In each iteration, XGBoost assigns more importance to previously misclassified data, improving performance gradually.
- Using evaluation metrics such as **Confusion Matrix, Accuracy, Precision, Recall, and F1-score** on the test dataset. The confusion matrix is particularly useful for multi-class classification problems as it allows a more detailed analysis of model performance across different classes.

## Data Understanding

The dataset used consists of raw values from **52 sensors** monitoring a water pump system in a small city. The dataset can be accessed from **[Pump Sensor Data](https://www.kaggle.com/datasets/nphantawee/pump-sensor-data/data)**.

### Variables in the Water Pump Sensor Dataset:
- **Timestamp**: The time when the sensor data was recorded.
- **Sensor Data (52 series)**: Raw values from each sensor.
- **Machine Status**: The operational status of the system at the recorded time (running or not running).

### Exploratory Data Analysis

| Column           | Non-Null Count | Dtype   |
|-----------------|---------------|--------|
| sensor_00       | 210112        | float64 |
| sensor_01       | 219951        | float64 |
| sensor_02       | 220301        | float64 |
| sensor_03       | 220301        | float64 |
| sensor_04       | 220301        | float64 |
| sensor_05       | 220301        | float64 |
| sensor_06       | 215522        | float64 |
| sensor_07       | 214869        | float64 |
| sensor_08       | 215213        | float64 |
| sensor_09       | 215725        | float64 |
| machine_status  | 220320        | object  |

A **correlation matrix** analysis indicates that sensors **sensor_0 to sensor_12** have the most significant effect on system failures, while **sensor_44 to sensor_51** are particularly important for predicting broken system status.

Further, **class distribution analysis** reveals an imbalance, with the majority of samples labeled as `NORMAL`. **Oversampling** is applied to ensure equal distribution among all classes before training the models.

## Modeling

Two classification models are trained with the following hyperparameters:

**Random Forest Classifier:**
```python
n_estimators = 150
max_depth = 20
```

**XGBoost:**
```python
n_estimators = 150
max_depth = 20
```

## Evaluation

| Metric        | Formula  |
|--------------|-----------------------------------------------------------|
| **Accuracy** | (TP + TN) / (TP + FP + FN + TN) |
| **Precision** | TP / (TP + FP) |
| **Recall** | TP / (TP + FN) |
| **F1 Score** | 2 * (Precision * Recall) / (Precision + Recall) |

Results indicate that **Random Forest** outperforms XGBoost in terms of accuracy and misclassification rates. Specifically, **Random Forest produces fewer false alarms** (lower FP and FN rates) than XGBoost, making it a more reliable model for predictive maintenance in water pump systems.

## Conclusion

- **The most impactful sensors for prediction are sensor_0 to sensor_12.**
- **The best-performing model in this study is Random Forest.**
- **Random Forest is recommended for deployment due to its superior accuracy and reduced false alarms.**

This study demonstrates the effectiveness of predictive maintenance in water pump systems, providing a proactive approach to system reliability and efficiency.
