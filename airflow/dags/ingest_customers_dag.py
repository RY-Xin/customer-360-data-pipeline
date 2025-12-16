from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import sqlite3

def ingest_customers():
    # Load CSV
    df = pd.read_csv('/opt/airflow/dags/data/customers.csv')
    
    print(f"Loaded {len(df)} customer records")
    
    # Save to SQLite database
    conn = sqlite3.connect('/opt/airflow/dags/data/customer.db')
    df.to_sql('customers', conn, if_exists='replace', index=False)
    conn.close()

with DAG(
    dag_id='ingest_customers',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['customer360']
) as dag:
    
    ingest_task = PythonOperator(
        task_id='ingest_customers_task',
        python_callable=ingest_customers
    )
