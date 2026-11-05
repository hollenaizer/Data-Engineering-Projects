from extract import load_transactions
from quality_checks import validate_transactions


def main():

    print("Starting Banking ETL Pipeline...\n")

    transactions = load_transactions()

    clean_df, rejected_df = validate_transactions(
        transactions
    )

    clean_df.to_csv(
        "data/processed_transactions.csv",
        index=False
    )

    rejected_df.to_csv(
        "data/rejected_transactions.csv",
        index=False
    )

    print(
        f"Clean Transactions: {len(clean_df)}"
    )

    print(
        f"Rejected Transactions: {len(rejected_df)}"
    )

    print("\nPipeline Complete")


if __name__ == "__main__":
    main()