import pandas as pd
from openaq_ingestion import get_countries, get_locations


countries = get_countries()
locations = get_locations()

sensor_list_by_countries = []
def filter_sensors_location():
    for item in locations['results']:
        for sensor in item['sensors']:
            sensor_list_by_countries.append({
                'country': item['country']['name'],
                'sensor_id': sensor.get('id'),
                'sensor_name': sensor.get('name')
            })
    
    return sensor_list_by_countries

sensor_list_by_countries = filter_sensors_location()

df_sensors_by_countries = pd.DataFrame(sensor_list_by_countries)
df_sensors_by_countries.to_csv('./data/raw/sensors_by_countries.csv', index=False, encoding='utf-8', sep=';')






