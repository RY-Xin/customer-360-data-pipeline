# Customer 360 Data Pipeline

An end-to-end **Customer 360 Analytics** data pipeline project.

## Goal

Build a data pipeline that integrates:
- Customer profile data
- Transactions
- User events

and transforms them into analytics-ready tables for:
- Revenue & retention dashboards
- Customer segmentation
- Churn analysis (future extension)

## Tech Stack (MVP)

- Python
- Airflow (for orchestration)
- dbt (for transformations)
- SQLite / PostgreSQL (as the warehouse for now)
- Tableau / Power BI / Looker Studio (for dashboards)

## Project Structure

```text
customer-360-data-pipeline/
├── data/                 # Raw sample CSV files (customers, transactions, events)
├── airflow/
│   └── dags/             # Airflow DAGs
├── dbt/
│   └── models/           # dbt models (staging + marts)
├── sql/                  # Star schema & helper SQL scripts
└── dashboard/            # Dashboard definitions / screenshots
