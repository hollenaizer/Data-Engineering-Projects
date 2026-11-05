import pandas as pd


def load_customers():
    return pd.read_csv("data/raw/customers.csv")


def load_accounts():
    return pd.read_csv("data/raw/accounts.csv")


def load_branches():
    return pd.read_csv("data/raw/branches.csv")


def load_loans():
    return pd.read_csv("data/raw/loans.csv")


def load_transactions():
    return pd.read_csv("data/raw/transactions.csv")


def load_all_data():

    customers = load_customers()
    accounts = load_accounts()
    branches = load_branches()
    loans = load_loans()
    transactions = load_transactions()

    print("\n=== DATA LOADED SUCCESSFULLY ===\n")

    print(f"Customers: {len(customers)}")
    print(f"Accounts: {len(accounts)}")
    print(f"Branches: {len(branches)}")
    print(f"Loans: {len(loans)}")
    print(f"Transactions: {len(transactions)}")

    return (
        customers,
        accounts,
        branches,
        loans,
        transactions
    )


if __name__ == "__main__":
    load_all_data()