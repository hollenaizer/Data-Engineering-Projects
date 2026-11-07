
import csv
from pathlib import Path

# Locate the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Locate the original banking dataset
INPUT_FILE = PROJECT_DIR / "data" / "raw" / "paysim_transactions.csv"


def inspect_dataset():
    print("BANKING DATA PIPELINE")
    print("=====================")

    # Check whether the dataset exists
    if not INPUT_FILE.exists():
        print("ERROR: Dataset file not found.")
        return

    print("Dataset found!")
    print(f"File: {INPUT_FILE.name}")

    total_records = 0
    sample_records = []

    # Read the CSV file without loading everything into memory
    with open(INPUT_FILE, "r", encoding="utf-8", newline="") as file:

        reader = csv.DictReader(file)

        print("\nCOLUMN NAMES:")
        print(reader.fieldnames)

        for record in reader:
            total_records += 1

            # Keep only the first five records for inspection
            if len(sample_records) < 5:
                sample_records.append(record)

    print(f"\nTOTAL TRANSACTIONS: {total_records:,}")

    print("\nFIRST FIVE TRANSACTIONS:")
    for record in sample_records:
        print(record)


if __name__ == "__main__":
    inspect_dataset()
