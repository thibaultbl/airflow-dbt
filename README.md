# How to launch

## First time 

```
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker compose up airflow-init
```


```
docker compose up
bash ./scripts/init_db.sh
```



## Second time

```
docker compose up
```

# Sources

https://rasiksuhail.medium.com/orchestrating-dbt-with-airflow-a-step-by-step-guide-to-automating-data-pipelines-part-i-7a6db8ebc974