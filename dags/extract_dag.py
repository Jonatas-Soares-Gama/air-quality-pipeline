from airflow.decorators import dag, task
from datetime import datetime
from openaq_ingestion import get_locations, get_measurements
from explore_data import filter_sensors_location, filter_values_by_sensor


@dag(
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["extract"],
)
def extract_dag():
    @task
    
