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

def load_data(data):
    data_base = TinyDB('./data/raw/data_base.json')
    data_base.insert(data)

def get_countries():
    url = f"{BASE_URL}/countries"
    response = requests.get(url, headers=HEADERS)
    return response.json()

if __name__ == "__main__":
    data_countries = get_countries()
    load_data(data_countries)





