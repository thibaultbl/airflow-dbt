from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

#Define default arguments
default_args = {
 'owner': 'airflow',
 'start_date': datetime (2023, 9, 29),
 'retries': 1,
}

# Instantiate your DAG
dag = DAG ('create_database', default_args=default_args, schedule_interval=None)

# Define tasks
def task1():
 'echo "task 1"'

def task2():
 'echo "task 2"'

task_1 = BashOperator(
 task_id='task_1',
 bash_command=task1,
 dag=dag,
)
task_2 = BashOperator(
 task_id='task_2',
 bash_command=task2,
 dag=dag,
)

# Set task dependencies
task_1 >> task_2