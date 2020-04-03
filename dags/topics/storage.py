import os

import minio

from .config import s3 as settings


def push_result(**context):
    file_name = context['task_instance'].xcom_pull(task_ids='dump_topics')

    client = minio.Minio(
        's3.amazonaws.com',
        access_key=settings.access_key,
        secret_key=settings.secret_key,
    )

    client.fput_object(settings.bucket, file_name, file_name)
