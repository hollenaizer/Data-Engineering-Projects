import pandas as pd


def validate_transactions(df):

    rejected_rows = []

    for _, row in df.iterrows():

        if pd.isna(row["amount"]):
            row["rejection_reason"] = "Missing Amount"
            rejected_rows.append(row)

        elif float(row["amount"]) < 0:
            row["rejection_reason"] = "Negative Amount"
            rejected_rows.append(row)

        else:
            try:
                pd.to_datetime(row["transaction_date"])
            except:
                row["rejection_reason"] = "Invalid Date"
                rejected_rows.append(row)

    rejected_df = pd.DataFrame(rejected_rows)

    if not rejected_df.empty:
        clean_df = df[
            ~df["transaction_id"].isin(
                rejected_df["transaction_id"]
            )
        ]
    else:
        clean_df = df.copy()

    return clean_df, rejected_df