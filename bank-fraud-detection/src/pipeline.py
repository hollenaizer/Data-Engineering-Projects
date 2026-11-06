from extract import extract_data
from transform import transform_data
from fraud_detection import detect_fraud
from load import save_fraud

print("Starting Fraud Detection Pipeline...")

df = extract_data()

df = transform_data(df)

fraud_df = detect_fraud(df)

save_fraud(fraud_df)

print(f"Fraud transactions found: {len(fraud_df)}")

print("Pipeline completed.")