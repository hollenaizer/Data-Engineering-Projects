def save_fraud(df):

    df.to_csv(
        "data/fraud/fraud_transactions.csv",
        index=False
    )