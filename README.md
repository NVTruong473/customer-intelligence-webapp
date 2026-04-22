# AI Customer Intelligence Web App

A production-style Machine Learning web application built with Python and Streamlit.

This project predicts customer churn risk and provides an interactive customer dashboard with account management features.

---

## Main Features

- Customer Churn Prediction
- Risk Probability Score
- Business Recommendations
- Secure Login System
- Register New Account
- Change Password
- Forgot Password
- Reset Demo Accounts
- Responsive Mobile Friendly UI
- Admin / User Account Logic

---

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Google Colab
- GitHub

---

## Machine Learning Model

Dataset used:

Telco Customer Churn Dataset

Models tested:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- KNN

Best model selected automatically and saved as:

    model/churn_model.pkl

---

## Project Structure

    customer-intelligence-webapp/
    │── app.py
    │── auth.py
    │── ui.py
    │── predict.py
    │── utils.py
    │── styles.py
    │── config.py
    │── requirements.txt
    │── README.md
    │── TEST_GUIDE.md
    │
    ├── assets/
    │   └── logo.png
    │
    ├── data/
    │   ├── raw_telco.csv
    │   ├── processed_telco.csv
    │   └── users.csv
    │
    ├── model/
    │   ├── churn_model.pkl
    │   └── feature_columns.pkl

---

## Run Locally

Install packages:

    pip install -r requirements.txt

Run app:

    streamlit run app.py

---

## Demo Accounts

    admin / Admin@123
    7590-VHVEG / Cust@7590

---

## Testing Guide

See full test cases in:

    TEST_GUIDE.md

---

## Screenshots

Add screenshots after deployment:

- Login Page
- Dashboard
- Prediction Result
- Mobile View

---

## Why This Project Matters

This project demonstrates:

- End-to-End ML Workflow
- Data Cleaning
- Model Training
- Model Deployment
- User Authentication Logic
- Real Product Thinking
- Clean Multi-file Architecture

---

## Future Improvements

- Credit Risk Prediction
- Customer Segmentation
- Database Integration
- OTP Recovery
- User Activity Logs
- Cloud Deployment

---

## Author

Nguyen Van Truong

GitHub: NVTruong473
