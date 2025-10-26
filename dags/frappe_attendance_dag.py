from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 10, 23),
}

with DAG(
    dag_id='frappe_attendance_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    call_frappe_api = SimpleHttpOperator(
        task_id='call_frappe_api',
        http_conn_id='frappe_api',  # نفس Connection اللي أضفتيه في Astronomer
        endpoint='api/method/custom.attendance.export',
        method='GET',
        log_response=True
    )
