
import csv
from pathlib import Path
from collections import Counter

PROJECT_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_DIR / "data" / "raw" / "paysim_transactions.csv"


def investigate_balances():

    mismatch_by_type = Counter()
    checked_by_type = Counter()

    mismatch_by_fraud = Counter()
    checked_by_fraud = Counter()

    examples = []

    with open(INPUT_FILE, "r", encoding="utf-8", newline="") as file:

        reader = csv.DictReader(file)

        for record in reader:

            transaction_type = record["type"]
            fraud_label = record["isFraud"]

            amount = float(record["amount"])
            old_balance = float(record["oldbalanceOrg"])
            new_balance = float(record["newbalanceOrig"])

            if transaction_type == "CASH_IN":
                expected_balance = old_balance + amount
            else:
                expected_balance = old_balance - amount

            checked_by_type[transaction_type] += 1
            checked_by_fraud[fraud_label] += 1

            difference = new_balance - expected_balance

            if abs(difference) > 0.01:

                mismatch_by_type[transaction_type] += 1
                mismatch_by_fraud[fraud_label] += 1

                if len(examples) < 10:
                    examples.append({
                        "type": transaction_type,
                        "fraud": fraud_label,
                        "amount": amount,
                        "old_balance": old_balance,
                        "expected_balance": expected_balance,
                        "actual_balance": new_balance,
                        "difference": difference
                    })

    print("\nBALANCE MISMATCHES BY TRANSACTION TYPE")
    print("======================================")

    for transaction_type, checked in checked_by_type.items():

        mismatches = mismatch_by_type[transaction_type]

        percentage = (mismatches / checked) * 100

        print(
            f"{transaction_type}: "
            f"{mismatches:,} / {checked:,} "
            f"({percentage:.2f}%)"
        )

    print("\nBALANCE MISMATCHES BY FRAUD LABEL")
    print("=================================")

    for fraud_label, checked in checked_by_fraud.items():

        mismatches = mismatch_by_fraud[fraud_label]

        percentage = (mismatches / checked) * 100

        print(
            f"Fraud {fraud_label}: "
            f"{mismatches:,} / {checked:,} "
            f"({percentage:.2f}%)"
        )

    print("\nFIRST 10 MISMATCH EXAMPLES")
    print("==========================")

    for example in examples:
        print(example)


if __name__ == "__main__":
    investigate_balances()
