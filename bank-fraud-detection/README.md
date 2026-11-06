Bank Fraud Detection ETL Pipeline
Overview
This project simulates a real-world banking fraud detection pipeline built using Python and Pandas.

The pipeline extracts transaction data from a CSV file, performs data validation and transformation, applies fraud detection rules, and stores suspicious transactions for further investigation.

The project demonstrates core Data Engineering concepts including ETL development, data quality checks, fraud analytics, and automated data processing.

Business Problem
Banks process thousands of transactions every day. Identifying potentially fraudulent transactions quickly is critical to reducing financial losses and protecting customers.

This project helps identify suspicious transactions based on predefined fraud detection rules.

Examples:

High-value transactions
Unusual customer activity
Transactions requiring further investigation
Project Architecture
Raw Transactions ↓ Extract ↓ Transform ↓ Fraud Detection Rules ↓ Fraud Alerts Output

Project Structure
bank-fraud-detection/

├── data/
│   ├── raw/
│   ├── processed/
│   └── fraud/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── fraud_detection.py
│   ├── load.py
│   └── pipeline.py
│
├── reports/
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore


Technologies Used
Python
Pandas
Git
GitHub
CSV Files
ETL Development
Fraud Detection Rule

Transactions greater than R50,000 are flagged as suspicious.

Example:

Amount	ResultR500	Normal
R10,000	Normal
R55,000	Suspicious
R120,000	Suspicious