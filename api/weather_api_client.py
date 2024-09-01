
import requests


class WeatherApiClient:
    def __init__(self, api_key, base_url="https://api.openweathermap.org/data/2.5"):
        self.api_key = api_key
        self.base_url = base_url

    def get_current_weather(self, lat, lon):
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key
        }
        response = requests.get(f"{self.base_url}/weather", params=params)
        response.raise_for_status()
        return response.json()
