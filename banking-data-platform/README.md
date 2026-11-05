Banking Data Platform

Project Overview



This project simulates a real-world banking data engineering solution for a South African bank.



The platform ingests customer, account, loan, branch, and transaction data, performs data quality validation, and prepares clean datasets for reporting and analytics.



The project demonstrates core Data Engineering concepts including:



Data Extraction

Data Transformation

Data Quality Checks

ETL Pipelines

Data Validation

Error Handling

Git Version Control

Data Warehousing Principles

Business Scenario



Ubuntu Bank SA receives data from multiple banking systems daily.



The Data Engineering team is responsible for:



Collecting data from source systems

Validating data quality

Rejecting invalid records

Preparing clean datasets

Supporting business reporting



Examples of business questions:



Which branch processes the highest transaction volume?

Which province generates the most activity?

What is the bank's total loan exposure?

Which transaction channels are most frequently used?

Project Structure

Plain Text

banking-data-platform/

 

│

├── data/

│ ├── raw/

│ ├── staging/

│ ├── warehouse/

│ └── rejected/

│

├── src/

│ ├── extract.py

│ ├── transform.py

│ ├── load.py

│ ├── quality\_checks.py

│ └── run\_pipeline.py

│

├── sql/

│ ├── create\_tables.sql

│ └── business\_queries.sql

│

├── tests/

├── docs/

├── logs/

│

├── requirements.txt

└── README.md

Technologies Used

Python

Pandas

Git

GitHub

SQL

PostgreSQL (Planned)

Power BI (Planned)

Data Sources

Customers



Contains customer demographic information.



Accounts



Contains customer bank account information.



Transactions



Contains customer transaction activity.



Loans



Contains loan account information.



Branches



Contains branch location information.



Data Quality Rules



The pipeline validates:



Missing Amounts



Example:



Plain Text

Amount = NULL

Negative Amounts



Example:



Plain Text

Amount = -400

Invalid Dates



Example:



Plain Text

invalid-date



Invalid records are moved to the rejected dataset for review.



Future Enhancements

PostgreSQL Data Warehouse

Star Schema Design

Incremental Loading

Automated Testing

Logging Framework

Apache Airflow Orchestration

Power BI Dashboard

Azure Data Factory Integration

Author



Casswell Maswanganye



Aspiring Data Engineer building hands-on projects focused on ETL development, data quality, SQL, cloud technologies, and modern data platforms.

