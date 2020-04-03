from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from topics.config import settings
from topics.tweets import extract_tweets
from topics.lda import dump_topics
from topics.storage import push_result


default_args = {
    "owner": "maresac",
    "depends_on_past": False,
    "start_date": datetime(2020, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "provide_context":True
}

dag = DAG(
    "airflow-topics",
    default_args=default_args,
    schedule_interval='@daily')

task1 = PythonOperator(
    task_id="extract_tweets",
    python_callable=extract_tweets,
    op_kwargs={
        "sample_size": settings.sample_size
    },
    dag=dag
)

task2 = PythonOperator(
    task_id="dump_topics",
    python_callable=dump_topics,
    op_kwargs={
        "filename": "topics.json"
    },
    dag=dag
)

task3 = PythonOperator(
    task_id="push_result",
    python_callable=push_result,
    dag=dag
)

task1 >> task2 >> task3
