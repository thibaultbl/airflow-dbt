from airflow.decorators import dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


@dag(
    "query_pet_table",
    start_date=datetime(2020, 6, 1),
    max_active_runs=3,
    schedule="@daily",
    default_args=default_args,
    template_searchpath="/opt/airflow/dags/sql",
    catchup=False,
)
def query_pet_table():
    opr_call_sproc1 = SQLExecuteQueryOperator(
        task_id="call_sproc1", conn_id="postgres", sql="SELECT * FROM pet;"
    )


    opr_call_sproc1


query_pet_table()