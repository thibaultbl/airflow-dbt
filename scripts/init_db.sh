docker exec airflow-dbt-postgres-1 psql -U airflow -c "CREATE DATABASE dbt_database"
docker exec airflow-dbt-postgres-1 psql -U airflow -c "GRANT ALL PRIVILEGES ON DATABASE dbt_database TO airflow;"