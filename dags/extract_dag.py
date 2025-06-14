from airflow.decorators import dag, task
from datetime import datetime
from src.openaq_ingestion import get_locations
from src.explore_data import filter_sensors_location, create_sensors_by_countries_csv, filter_values_by_sensor, create_values_by_sensor_csv



@dag(
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["extract"],
)
def openaq_pipeline():
    
    @task
    def get_locations_dag():
        return get_locations()
    
    @task
    def filter_sensors_location_dag(locations_data): 
        return filter_sensors_location(locations_data)
    
    @task
    def create_sensors_by_countries_csv_dag(sensor_list_by_countries):
        return create_sensors_by_countries_csv(sensor_list_by_countries)
    
    @task
    def filter_values_by_sensor_dag(df_sensors_by_countries):
        return filter_values_by_sensor(df_sensors_by_countries)
    
    @task
    def create_values_by_sensor_csv_dag(values_by_sensor):
        return create_values_by_sensor_csv(values_by_sensor)

    locations_data = get_locations_dag()
    sensor_list_by_countries = filter_sensors_location_dag(locations_data)
    df_sensors_by_countries = create_sensors_by_countries_csv_dag(sensor_list_by_countries)
    values_by_sensor = filter_values_by_sensor_dag(df_sensors_by_countries)
    create_values_by_sensor_csv_dag(values_by_sensor)   

# Instantiate the DAG
openaq_pipeline = openaq_pipeline()
    
