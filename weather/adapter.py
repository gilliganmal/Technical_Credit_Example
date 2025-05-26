from .interfaces import WeatherService
from .models import WeatherData
from .services.open_weather_service import OpenWeatherApiClient

class OpenWeatherAdapter(WeatherService):
    def __init__(self, api_key: str):
        self.api_client = OpenWeatherApiClient(api_key)

    def get_weather(self, location: str) -> WeatherData:
        data = self.api_client.fetch_weather_data(location)
        return WeatherData(
            temperature=data['main']['temp'],
            condition=data['weather'][0]['description'],
            location=location
        )