from airflow.decorators import dag, task
from datetime import datetime
from src.openaq_ingestion import get_instruments
from src.explore_data import filter_instruments, create_instruments_path



@dag(
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["extract"],
)
def instruments_pipeline():
    
    @task
    def get_instruments_dag():
        return get_instruments()
    
    @task
    def filter_instruments_dag(instruments_data):
        return filter_instruments(instruments_data)
    
    @task
    def create_instruments_path_dag(instruments_list):
        return create_instruments_path(instruments_list)
    
    instruments_data = get_instruments_dag()
    instruments_list = filter_instruments_dag(instruments_data)
    create_instruments_path_dag(instruments_list)

instruments_pipeline = instruments_pipeline()