import csv
from pathlib import Path
from collections import Counter

PROJECT_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_DIR / "data" / "raw" / "paysim_transactions.csv"


def investigate_balance_rules():

    results_by_type = Counter()
    results_overall = Counter()

    tolerance = 0.01

    with open(INPUT_FILE, "r", encoding="utf-8", newline="") as file:

        reader = csv.DictReader(file)

        for record in reader:

            transaction_type = record["type"]

            amount = float(record["amount"])
            old_balance = float(record["oldbalanceOrg"])
            new_balance = float(record["newbalanceOrig"])

            # Calculate the expected balance
            if transaction_type == "CASH_IN":
                expected_balance = old_balance + amount
            else:
                expected_balance = old_balance - amount

            # Classify the transaction
            if abs(new_balance - expected_balance) <= tolerance:

                category = "Matches calculation"

            elif amount > old_balance and new_balance == 0:

                category = "Amount exceeds balance; new balance is zero"

            elif amount > old_balance:

                category = "Amount exceeds balance; new balance is not zero"

            else:

                category = "Mismatch despite sufficient balance"

            results_by_type[(transaction_type, category)] += 1
            results_overall[category] += 1

    print("\nBALANCE RULE INVESTIGATION")
    print("==========================")

    print("\nOVERALL RESULTS")
    print("---------------")

    for category, count in results_overall.items():

        percentage = (count / sum(results_overall.values())) * 100

        print(f"{category}: {count:,} ({percentage:.2f}%)")

    print("\nRESULTS BY TRANSACTION TYPE")
    print("--------------------------")

    transaction_types = [
        "PAYMENT",
        "TRANSFER",
        "CASH_OUT",
        "DEBIT",
        "CASH_IN"
    ]

    for transaction_type in transaction_types:

        print(f"\n{transaction_type}:")

        for category in results_overall:

            count = results_by_type[(transaction_type, category)]

            print(f"  {category}: {count:,}")

    print("\nINVESTIGATION COMPLETED.")


if __name__ == "__main__":
    investigate_balance_rules()