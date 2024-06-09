from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

#Define default arguments
default_args = {
 'owner': 'airflow',
 'start_date': datetime (2023, 9, 29),
 'retries': 1,
}

@dag(
    "dbt_run",
    start_date=datetime(2020, 6, 1),
    max_active_runs=3,
    schedule="@daily",
    default_args=default_args,
    template_searchpath="/opt/airflow/dags/sql",
    catchup=False,
)
def dbt_run():
    opr_call_sproc1 = BashOperator(
        task_id="run_dbt_op", bash_command="cd /opt/airflow/dags/dbt/test_project && dbt run"
    )

    opr_call_sproc2 = SQLExecuteQueryOperator(
        task_id="call_sproc2", conn_id="postgres", sql="select * from dbt_project.pet_model"
    )


    opr_call_sproc1 >> opr_call_sproc2


dbt_run()