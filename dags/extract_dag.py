import sys
sys.path.append("/opt/airflow/src")
from datetime import datetime
from airflow.decorators import dag, task

from explore_data import filter_sensors_location, filter_values_by_sensor
from openaq_ingestion import get_measurements, get_locations

@dag(
    dag_id="extract_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["extract"]
)

def extract_data():
    @task()
    def extract_raw_data():
        return get_locations()
    @task()
    def extract_sensors_location():
        return filter_sensors_location()
    @task()
    def transform_data():
        df_sensors_by_countries = pd.DataFrame(filter_sensors_location())
        df_sensors_by_countries.to_csv("/opt/airflow/data/sensors_by_countries.csv", index=False)
    
    extract_raw_data()
    extract_sensors_location()
    transform_data()
    
extract_data()

