\# Banking Data Pipeline – Financial Transaction Data Quality and Fraud Analysis



\## Project Overview



This project is a Python-based banking data engineering pipeline built to process and investigate large volumes of synthetic financial transaction data.



The objective is to demonstrate practical data engineering skills, including data inspection, data quality assessment, transaction validation, fraud-label analysis and the development of a reliable data processing workflow.



The project uses the PaySim synthetic financial transactions dataset, containing approximately 6.36 million transactions.



\## Project Objectives



\- Inspect large CSV datasets using Python.

\- Assess data completeness and validity.

\- Identify unexpected transaction types and invalid financial values.

\- Investigate sender account balance inconsistencies.

\- Analyse transaction distributions and fraud labels.

\- Develop a reliable and testable data pipeline.

\- Prepare transaction data for future SQL-based analysis.



\## Technology Stack



| Technology | Purpose |

|---|---|

| Python | Data processing and validation |

| CSV | Source data format |

| SQL | Planned database analysis |

| PostgreSQL | Planned database storage |

| Git and GitHub | Version control and project portfolio |



\## Dataset



\*\*Source:\*\* \[PaySim – Synthetic Financial Dataset for Fraud Detection](https://www.kaggle.com/datasets/ealaxi/paysim1)



The dataset contains simulated financial transactions with the following fields:



\- `step` – Simulation time unit.

\- `type` – Transaction type.

\- `amount` – Transaction amount.

\- `nameOrig` – Originating account identifier.

\- `oldbalanceOrg` – Sender's balance before the transaction.

\- `newbalanceOrig` – Sender's balance after the transaction.

\- `nameDest` – Destination account identifier.

\- `oldbalanceDest` – Recipient's balance before the transaction.

\- `newbalanceDest` – Recipient's balance after the transaction.

\- `isFraud` – Fraud classification label.

\- `isFlaggedFraud` – Indicates transactions flagged by the simulation.



The dataset is synthetic and does not contain actual bank customer transactions.



\## Initial Data Assessment



The initial inspection identified:



| Metric | Result |

|---|---:|

| Total transactions | 6,362,620 |

| Missing values detected | 0 |

| Invalid amounts | 0 |

| Negative amounts | 0 |

| Unexpected transaction types | 0 |

| Fraud-labelled transactions | 8,213 |

| Non-fraud-labelled transactions | 6,354,407 |



\### Transaction Types



The dataset contains five transaction types:



\- PAYMENT

\- TRANSFER

\- CASH\_OUT

\- DEBIT

\- CASH\_IN



\### Sender Balance Investigation



An initial balance validation rule was applied to investigate sender balances.



The investigation identified 3,779,503 mismatches against the preliminary calculation rule.



Further analysis showed that these mismatches were not reliable indicators of fraud. The validation logic therefore requires further investigation before being used to reject records.



This is an important part of the project: understanding the source data and its business rules before implementing production validation.



\## Project Structure



```text

banking-data-pipeline/

│

├── data/

│   ├── raw/

│   ├── processed/

│   └── quarantine/

│

├── reports/

├── sql/

├── src/

│   ├── inspect\_data.py

│   ├── data\_quality.py

│   ├── balance\_diagnostics.py

│   └── balance\_rule\_invest

