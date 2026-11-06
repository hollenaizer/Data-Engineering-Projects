import pandas as pd

def transform_data(df):

    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    df.dropna(inplace=True)

    return df