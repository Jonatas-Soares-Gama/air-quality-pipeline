import pandas as pd
from openaq_ingestion import get_countries, get_locations, get_measurements


countries = get_countries()
locations = get_locations()

sensor_list_by_countries = []
def filter_sensors_location():
    for item in locations.get('results', []):
        country_name = item.get('country', {}).get('name')
        for sensor in item.get('sensors', []):
            sensor_list_by_countries.append({
                'country': country_name,
                'sensor_id': sensor.get('id'),
                'sensor_name': sensor.get('name')
            })
    return sensor_list_by_countries

sensor_list_by_countries = filter_sensors_location()
df_sensors_by_countries = pd.DataFrame(sensor_list_by_countries)

values_by_sensor = []
def filter_values_by_sensor():
    for sensor_id in df_sensors_by_countries['sensor_id']:
        measurements = get_measurements(sensor_id)
        for measurement in measurements.get('results', []):
            value = measurement.get('value')
            parameter_id = measurement.get('parameter').get('id')
            values_by_sensor.append({
                'sensor_id': sensor_id,
                'parameter_id': parameter_id,
                'value': value
            })

    return values_by_sensor
    
values_by_sensor = filter_values_by_sensor()
df_values_by_sensor = pd.DataFrame(values_by_sensor)

df_sensors_by_countries.to_csv('./data/raw/sensors_by_countries.csv', index=False, encoding='utf-8', sep=';')
df_values_by_sensor.to_csv('./data/raw/values_by_sensor.csv', index=False, encoding='utf-8', sep=';')



