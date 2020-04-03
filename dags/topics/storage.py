import os

import minio

from .config import settings


def push_result(**context):
    file_name = context['task_instance'].xcom_pull(task_ids='dump_topics')

    client = minio.Minio(
        's3.amazonaws.com',
        access_key=settings.s3.access_key,
        secret_key=settings.s3.secret_key,
    )

    client.fput_object('airflow-topics', file_name, file_name)
