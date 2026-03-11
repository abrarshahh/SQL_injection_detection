# SQL Injection Detection using Machine Learning

A comprehensive machine learning-based solution to detect and prevent SQL injection attacks. This project utilizes multiple models, including Random Forest, Gradient Boosting, and Neural Networks, reaching up to **97% accuracy** in identifying malicious SQL queries.

## Overview

SQL injection remains one of the most common web vulnerabilities. This project provides:
- **High-Accuracy Detection**: Trained on over 100,000 queries.
- **Multiple Models**: Compare performance between Random Forest, Gradient Boosting, and CNN/LSTM.
- **Web Interface**: A built-in Django web application for real-time testing.

## Tech Stack

- **Language**: Python 3.x
- **Web Framework**: Django
- **Machine Learning**: Scikit-learn, TensorFlow/Keras
- **Data Processing**: Pandas, NumPy
- **NLP**: TfidfVectorizer

## Performance

| Model              | Accuracy |
|--------------------|----------|
| Random Forest      | ~97.5%   |
| Gradient Boosting  | ~97.2%   |
| Neural Network     | ~96-99%  |

## Project Structure

- `webapp/`: Django web application for real-time query detection.
- `Dataset/`: Training and testing datasets (`sqli-extended.csv`).
- `sql_injection_attack.ipynb`: Jupyter notebook for model training, EDA, and evaluation.
- `randomforest.pkl`: Pre-trained Random Forest model.
- `gradientboost.pkl`: Pre-trained Gradient Boosting model.
- `SQl_injection_detection.h5`: Pre-trained Neural Network model.
- `Testing_queries.txt`: Sample queries for testing the models.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/SQL_injection_detection.git
   cd SQL_injection_detection
   ```

2. **Install dependencies**:
   ```bash
   pip install django pandas scikit-learn tensorflow wordcloud seaborn matplotlib
   ```

3. **Run the Web Application**:
   ```bash
   cd webapp
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` to test queries.

## Usage

1. Open the web interface.
2. Enter a SQL query in the input field.
3. Click "Submit" to see if the query is classified as a "SQL Injection Attack" or "Not SQL Injection Attack".

## Dataset Source

The models were trained using a dataset from Kaggle: [SQL Injection Dataset](https://www.kaggle.com/datasets/alextrinity/sqlinjectionextend).
