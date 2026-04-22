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

```text
model/churn_model.pkl
```

---

## Project Structure

```text
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
```

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Demo Accounts

```text
admin / Admin@123
7590-VHVEG / Cust@7590
```

---

## Testing Guide

See:

```text
TEST_GUIDE.md
```

---

## Future Improvements

- Credit Risk Prediction
- Customer Segmentation
- Database Integration
- OTP Recovery
- Activity Logs
- Cloud Deployment

---

## Author

Nguyen Van Truong

GitHub: NVTruong473
