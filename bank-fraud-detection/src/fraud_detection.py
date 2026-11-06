def detect_fraud(df):

    fraud_df = df[
        df["amount"] > 50000
    ]

    return fraud_df