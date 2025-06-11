import os
import requests
import time
from airflow.models import Variable

API_KEY = Variable.get("OPENAQ_API_KEY", default_var=os.getenv('OPENAQ_API_KEY'))
if not API_KEY:
    raise ValueError("OPENAQ_API_KEY não encontrada. Configure-a nas variáveis do Airflow ou nas variáveis de ambiente.")

BASE_URL = 'https://api.openaq.org/v3'
HEADERS = {
    'X-API-Key': API_KEY,
    'Accept': "application/json"
}

# Tempo de espera entre requisições (em segundos)
REQUEST_DELAY = 1

def make_api_request(url):
        time.sleep(REQUEST_DELAY)
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()


def get_countries():
    url = f"{BASE_URL}/countries"
    return make_api_request(url)

def get_locations():
    url = f"{BASE_URL}/locations"
    return make_api_request(url)

def get_measurements(sensor_id):
    url = f"{BASE_URL}/sensors/{sensor_id}/measurements/daily"
    return make_api_request(url)

if __name__ == "__main__":
        data_countries = get_countries()
        data_measurements = get_measurements(3917)
        print(data_measurements)







