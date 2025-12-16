from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime
import pandas as pd
import sqlite3


def transform_customers():
    conn = sqlite3.connect('/opt/airflow/dags/data/customer.db')
    df = pd.read_sql_query("SELECT * FROM customers", conn)

    df = df.rename(columns={"id": "customer_id"})
    df["is_adult"] = df["age"] >= 18

    df.to_sql("customer_clean", conn, if_exists="replace", index=False)
    conn.close()


with DAG(
    dag_id="transform_customers",
    start_date=datetime(2024, 12, 1),
    schedule=None,
    catchup=False,
) as dag:

    wait_for_ingest = ExternalTaskSensor(
        task_id="wait_for_ingest_customers",
        external_dag_id="ingest_customers",
        external_task_id=None,
        allowed_states=["success"],
        failed_states=["failed"], 
        mode="poke",
        timeout=300,
        poke_interval=30,
    )

    transform_task = PythonOperator(
        task_id="transform_customers_task",
        python_callable=transform_customers,
    )

    wait_for_ingest >> transform_task
