
import csv
from pathlib import Path
from collections import Counter

# Locate the project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Original banking transaction file
INPUT_FILE = PROJECT_DIR / "data" / "raw" / "paysim_transactions.csv"

# Expected transaction types in PaySim
EXPECTED_TYPES = {
    "PAYMENT",
    "TRANSFER",
    "CASH_OUT",
    "DEBIT",
    "CASH_IN"
}


def assess_data_quality():

    print("BANKING DATA QUALITY ASSESSMENT")
    print("================================")

    if not INPUT_FILE.exists():
        print("ERROR: Dataset not found.")
        return

    total_records = 0

    missing_values = Counter()
    transaction_types = Counter()
    fraud_counts = Counter()

    invalid_amounts = 0
    negative_amounts = 0
    unexpected_types = 0

    balance_checks = 0
    balance_mismatches = 0

    with open(INPUT_FILE, "r", encoding="utf-8", newline="") as file:

        reader = csv.DictReader(file)

        for record in reader:

            total_records += 1

            # 1. Check for missing values
            for column in reader.fieldnames:
                value = record.get(column)

                if value is None or not value.strip():
                    missing_values[column] += 1

            # 2. Check transaction types
            transaction_type = (record.get("type") or "").strip()

            transaction_types[transaction_type] += 1

            if transaction_type not in EXPECTED_TYPES:
                unexpected_types += 1

            # 3. Check transaction amounts
            try:
                amount = float(record["amount"])

                if amount < 0:
                    negative_amounts += 1

            except (ValueError, TypeError):
                invalid_amounts += 1
                continue

            # 4. Count fraud labels
            fraud_counts[(record.get("isFraud") or "").strip()] += 1

            # 5. Check sender balance consistency
            try:
                old_balance = float(record["oldbalanceOrg"])
                new_balance = float(record["newbalanceOrig"])

                if transaction_type == "CASH_IN":
                    expected_balance = old_balance + amount
                elif transaction_type in EXPECTED_TYPES:
                    expected_balance = old_balance - amount
                else:
                    continue

                balance_checks += 1

                if abs(new_balance - expected_balance) > 0.01:
                    balance_mismatches += 1

            except (ValueError, TypeError):
                continue

    # Print the assessment report
    print(f"\nTOTAL TRANSACTIONS: {total_records:,}")

    print("\nMISSING VALUES:")
    if missing_values:
        for column, count in missing_values.items():
            print(f"{column}: {count:,}")
    else:
        print("No missing values found.")

    print(f"\nINVALID AMOUNTS: {invalid_amounts:,}")
    print(f"NEGATIVE AMOUNTS: {negative_amounts:,}")

    print(f"\nUNEXPECTED TRANSACTION TYPES: {unexpected_types:,}")

    print("\nTRANSACTION TYPE BREAKDOWN:")
    for transaction_type, count in transaction_types.items():
        print(f"{transaction_type}: {count:,}")

    print("\nFRAUD LABEL BREAKDOWN:")
    for fraud_label, count in fraud_counts.items():
        print(f"Label {fraud_label}: {count:,}")

    print("\nSENDER BALANCE ASSESSMENT:")
    print(f"Balance checks performed: {balance_checks:,}")
    print(f"Balance mismatches: {balance_mismatches:,}")

    print("\nDATA QUALITY ASSESSMENT COMPLETED.")


if __name__ == "__main__":
    assess_data_quality()
