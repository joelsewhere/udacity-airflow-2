from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'glue_parse_json_dag',
    default_args=default_args,
    description='Trigger AWS Glue job to parse JSON objects',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
    max_active_runs=1,
) as dag:

    glue_job = AwsGlueJobOperator(
        task_id='run_glue_parse_json',
        job_name='your-glue-job-name',  # Replace with your Glue job name
        script_location='s3://your-bucket/path/to/glue_script.py',  # optional, if you override default script
        job_desc='Glue job to parse JSON objects',
        num_of_dpus=2,
        aws_conn_id='aws_default',  # Replace if you use a different AWS connection
        region_name='us-east-1',  # Your AWS region
        arguments={
            '--input_path': 's3://your-input-bucket/input-json/',    # example argument
            '--output_path': 's3://your-output-bucket/parsed-json/',  # example argument
        },
    )

    glue_job