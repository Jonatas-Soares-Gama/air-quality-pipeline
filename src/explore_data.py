import pandas as pd
import os
from dateutil.parser import parse
from src.openaq_ingestion import get_measurements



def filter_sensors_location(locations_data):
    sensor_list_by_countries = []
    for item in locations_data.get('results', []):
        country_name = item.get('country', {}).get('name')
        for sensor in item.get('sensors', []):
            sensor_list_by_countries.append({
                'country': country_name,
                'sensor_id': sensor.get('id'),
                'sensor_name': sensor.get('name')
            })
    return sensor_list_by_countries

def create_sensors_by_countries_csv(sensor_list_by_countries):
    df_sensors_by_countries = pd.DataFrame(sensor_list_by_countries)
    
    output_dir = os.getenv("MY_DATA_DIR", "/usr/local/airflow/data/raw")
    print(output_dir)
    
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'sensors_by_countries.csv')
    
    df_sensors_by_countries.to_csv(output_file, index=False, encoding='utf-8', sep=';')
    return df_sensors_by_countries


values_by_sensor = []
def filter_values_by_sensor(df_sensors_by_countries):
    for sensor_id in df_sensors_by_countries['sensor_id']: # for que passa por cada sensor_id da lista de sensores por país
        measurements = get_measurements(sensor_id) # pega as medidas do sensor
        for measurement in measurements.get('results', []): # for que passa por cada medida do sensor
            value = measurement.get('value')
            parameter_id = measurement.get('parameter').get('id') 
            parameter_name = measurement.get('parameter').get('name')
            units = measurement.get('parameter').get('units')
            date_time_utc = measurement.get('period', {}).get('datetimeFrom', {}).get('utc')
            date_obj = parse(date_time_utc)
            date = date_obj.strftime('%Y-%m-%d')
            values_by_sensor.append({
                'sensor_id': sensor_id,
                'parameter_id': parameter_id,
                'parameter_name': parameter_name,
                'value': value,
                'units': units,
                'date': date
            })

    return values_by_sensor

def create_values_by_sensor_csv(values_by_sensor):
    df_values_by_sensor = pd.DataFrame(values_by_sensor)

    output_dir = os.getenv("MY_DATA_DIR", "/usr/local/airflow/data/raw")

    
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'values_by_sensor.csv')
    
    df_values_by_sensor.to_csv(output_file, index=False, encoding='utf-8', sep=';')
    return df_values_by_sensor

def filter_instruments(instruments_data):
    instruments_list = []
    for instrument in instruments_data.get('results', []):
        instrument_id = instrument.get('id')
        instrument_name = instrument.get('name')
        instrument_official = instrument.get('isMonitor')
        instrument_manufacturer_id = instrument.get('manufacturer', {}).get('id')
        instrument_manufacturer_name = instrument.get('manufacturer', {}).get('name')
        instruments_list.append({
            'instrument_id': instrument_id,
            'instrument_name': instrument_name,
            'instrument_official': instrument_official,
            'instrument_manufacturer_id': instrument_manufacturer_id,
            'instrument_manyfacturer_name': instrument_manufacturer_name
        })
    return instruments_list

def create_instruments_path(instruments_list):
    df_instruments = pd.DataFrame(instruments_list)

    output_dir = os.getenv("MY_DATA_DIR", "/usr/local/airflow/data/raw")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, 'instruments.csv')

    df_instruments.to_csv(output_file, index=False, encoding='utf-8', sep=';')
    df_instruments.to_json(output_file.replace('.csv', '.json'), orient='records', lines=True)
    return df_instruments






