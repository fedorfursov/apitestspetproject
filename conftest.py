import os

import pytest
from api.weather_api_client import WeatherApiClient

@pytest.fixture(scope="session")
def api_key():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("API ключ не найден в переменных окружения.")
    return api_key

@pytest.fixture(scope="session")
def weather_client(api_key):
    return WeatherApiClient(api_key=api_key)