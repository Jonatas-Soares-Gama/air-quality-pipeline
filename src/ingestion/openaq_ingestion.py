import os
from dotenv import load_dotenv
import requests
from tinydb import TinyDB
import pandas as pd

load_dotenv('.venv/.env')

API_KEY = os.getenv('OPENAQ_API_KEY')

BASE_URL = 'https://api.openaq.org/v3'
HEADERS = {
    'X-API-Key': API_KEY,
    'Accept': "application/json"
}

def load_countries(data):
    data_base = TinyDB('./data/raw/data_countries.json')
    data_base.insert(data)

def load_measurements(data):
    data_base = TinyDB('./data/raw/data_measurements.json')
    data_base.insert(data)

def get_countries():
    url = f"{BASE_URL}/countries"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_locations():
    url = f"{BASE_URL}/locations"
    response = requests.get(url, headers=HEADERS)
    return response.json()


def get_measurements(sensor_id: int):
    url = f"{BASE_URL}/sensors/{sensor_id}/measurements"
    response = requests.get(url, headers=HEADERS)
    return response.json()


if __name__ == "__main__":
    data_countries = get_countries()
    data_measurements = get_measurements(3917)
    load_countries(data_countries)
    load_measurements(data_measurements)






