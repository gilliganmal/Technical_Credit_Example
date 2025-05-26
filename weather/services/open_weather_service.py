import requests

class OpenWeatherApiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def fetch_weather_data(self, location: str) -> dict:
        response = requests.get(
            "http://api.openweathermap.org/data/2.5/weather",
            params={
                "q": location,
                "appid": self.api_key,
                "units": "metric"
            }
        )
        return response.json()