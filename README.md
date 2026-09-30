# customer-churn-prediction
Machine Learning-based Customer Churn Prediction using Python, Scikit-learn, and FastAPI. Includes data preprocessing, model tuning, and a REST API for predicting customer churn.

## Project Overview

This project uses Machine Learning to predict whether a telecom customer is likely to leave the company (churn) or stay.

The project includes data preprocessing, model training, hyperparameter tuning, and a FastAPI application to serve predictions.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* FastAPI
* Uvicorn
* Joblib
* Jupyter Notebook

## Machine Learning

The project explores and evaluates classification models, including:

* Logistic Regression
* Decision Tree
* Random Forest

A tuned Decision Tree model was selected based on its recall performance during model comparison.

## Features

* Data preprocessing using Scikit-learn pipelines
* Handling numerical and categorical features
* Model training and evaluation
* Hyperparameter tuning with GridSearchCV
* Saving the trained pipeline using Joblib
* Predicting customer churn through a REST API
* Testing the API using Swagger UI

## Project Structure

```text
customer-churn-prediction/
├── main.py
├── churn_pipeline.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone tarunkumaraika/customer-churn-prediction.git
```

### 2. Navigate to the project folder

```bash
cd customer-churn-prediction
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the FastAPI application

```bash
fastapi dev main.py
```

### 5. Open Swagger UI

Visit:

http://127.0.0.1:8000/docs

Use the `POST /predict` endpoint to submit customer details and receive a prediction.

## Prediction Output

The API returns a prediction and a description:

* `1` — Customer is likely to churn
* `2` — Customer is likely to stay

## Future Improvements

* Deploy the API to a cloud hosting platform
* Add churn probability scores
* Build a user-friendly web interface

## Author

Tarun Kumar Aika
