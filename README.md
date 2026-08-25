# 🔐 Phishing Website Detection System

An intelligent **Phishing URL Detection System** that uses Machine Learning and a hybrid **CNN-BiLSTM Deep Learning model** to identify whether a website URL is **legitimate or phishing**.

The system analyzes URL patterns, automatically learns structural and sequential characteristics, and provides **real-time predictions** through an interactive user interface.

## 📌 Project Overview

Phishing attacks use deceptive websites and URLs to steal sensitive information such as login credentials, financial details, and personal data.

Traditional phishing detection systems often depend on manually engineered URL features and machine learning algorithms. This project improves upon this approach by implementing a hybrid **CNN-BiLSTM architecture** that can automatically learn important patterns directly from URL sequences.

The system also compares the proposed deep learning model with traditional machine learning models such as **Random Forest**, providing a baseline for performance evaluation.

## 🎯 Objectives

* Detect phishing and legitimate URLs accurately.
* Implement a hybrid **CNN-BiLSTM** deep learning model.
* Automatically learn important patterns from URL sequences.
* Provide real-time URL prediction.
* Compare traditional Machine Learning with Deep Learning.
* Reduce dependency on manual feature engineering.
* Provide an interactive and user-friendly prediction interface.
* Support future integration with web applications and cybersecurity tools.

## 🧠 System Architecture

The project follows the following workflow:

```text
URL Dataset
     ↓
Data Collection
     ↓
Data Preprocessing
     ↓
Exploratory Data Analysis
     ↓
Feature Extraction / Tokenization
     ↓
 ┌───────────────────────┐
 │ Machine Learning      │
 │ Random Forest         │
 └──────────┬────────────┘
            ↓
      Performance
       Comparison
            ↑
 ┌──────────┴────────────┐
 │ Deep Learning         │
 │ CNN + BiLSTM          │
 └──────────┬────────────┘
            ↓
       Model Evaluation
            ↓
     Model Saving
            ↓
   Real-Time Prediction
            ↓
     User Interface
```

## 🚀 Proposed CNN-BiLSTM Model

The proposed system combines two deep learning architectures:

### CNN

The **Convolutional Neural Network (CNN)** extracts important local patterns and structural characteristics from URL sequences, including suspicious keywords and abnormal URL structures.

### BiLSTM

The **Bidirectional Long Short-Term Memory (BiLSTM)** network captures sequential dependencies within URL strings by processing the sequence in both forward and backward directions.

### CNN + BiLSTM

By combining CNN and BiLSTM, the system can learn both:

* Local URL patterns
* Structural characteristics
* Sequential dependencies
* Contextual relationships

This allows the model to identify complex phishing patterns more effectively.

## 🔄 Project Workflow

### 1. Data Collection

A dataset containing both **phishing and legitimate URLs** is collected and prepared for model training and testing.

### 2. Data Preprocessing

For traditional machine learning, URL characteristics such as:

* URL length
* Number of special characters
* Number of digits
* HTTPS presence
* Number of subdomains
* Suspicious keywords

are extracted and converted into numerical features.

For deep learning, URLs are processed using:

* Tokenization
* Sequence padding

### 3. Exploratory Data Analysis

EDA is performed to understand the dataset and identify patterns between phishing and legitimate URLs.

Visualizations such as:

* Bar charts
* Histograms
* Distribution plots

can be used to analyze URL characteristics and dataset distribution.

### 4. Machine Learning Model

Traditional machine learning models are used as the baseline system.

The project considers models such as:

* Random Forest
* Decision Tree
* Logistic Regression

Performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score

### 5. CNN-BiLSTM Model

The processed URL sequences are passed to the CNN-BiLSTM architecture.

The CNN extracts local patterns, while the BiLSTM captures sequential relationships from both directions.

### 6. Model Evaluation

The Machine Learning and Deep Learning models are compared using evaluation metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### 7. Model Saving

The trained models and tokenizer are saved so they can be reused for future predictions without retraining.

### 8. Real-Time Prediction

Users can enter a website URL into the prediction interface.

The system processes the URL and provides a prediction indicating whether it is:

```text
✅ Legitimate
```

or

```text
⚠️ Phishing
```

The interface can also display probability scores and visual indicators.

## 🛠️ Technologies Used

| Category                   | Technologies                |
| -------------------------- | --------------------------- |
| Programming Language       | Python                      |
| Machine Learning           | Scikit-learn                |
| Deep Learning              | TensorFlow, Keras           |
| Data Processing            | NumPy, Pandas               |
| Data Visualization         | Matplotlib                  |
| Deep Learning Architecture | CNN, BiLSTM                 |
| Web Framework              | Flask                       |
| Frontend                   | HTML, CSS, JavaScript       |
| Development Environment    | Jupyter Notebook / Anaconda |

These technologies are specified in the project requirements.

## 📂 Project Modules

The system consists of the following major modules:

1. **Data Collection Module**
2. **Data Preprocessing Module**
3. **Exploratory Data Analysis Module**
4. **Machine Learning Model Training Module**
5. **CNN-BiLSTM Deep Learning Module**
6. **Model Evaluation and Comparison Module**
7. **Model Saving and Deployment Module**
8. **Prediction and User Interface Module**

The project document describes these modules as the main components of the system.

## 📊 Model Evaluation

The system evaluates the trained models using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The performance of traditional machine learning models is compared with the proposed CNN-BiLSTM model to evaluate the effectiveness of the deep learning approach.

## 💻 System Requirements

### Hardware

* Intel Core i5 or above
* Minimum 8 GB RAM
* 256 GB SSD or higher
* Integrated GPU or NVIDIA GPU (optional)
* Stable Internet connection

### Software

* Windows / Linux / macOS
* Python
* Jupyter Notebook or Anaconda
* TensorFlow
* Keras
* Scikit-learn
* NumPy
* Pandas
* Matplotlib
* Flask

## 🔮 Future Scope

The system can be further extended to:

* Develop a browser extension for automatic URL checking.
* Integrate phishing detection into email filtering systems.
* Deploy the model in cybersecurity dashboards.
* Retrain the model with newly identified phishing URLs.
* Integrate the system with web security applications.
* Scale the system for large-volume URL monitoring.

These extensions are identified in the project's proposed scope.

## ⚠️ Disclaimer

This project is intended for **educational and research purposes**. It demonstrates the application of Machine Learning and Deep Learning techniques for phishing URL detection and should not be considered a complete replacement for professional cybersecurity solutions.

## 👨‍💻 Project Author

**Bharath**

B.Tech – Artificial Intelligence and Data Science

---

⭐ If you find this project useful, consider giving the repository a star!
