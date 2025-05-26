### weather/controller.py

from .interfaces import WeatherService
from .strategies import ForecastStrategy

class WeatherController:
    def __init__(self, service: WeatherService, strategy: ForecastStrategy):
        self.service = service
        self.strategy = strategy

    def display_weather(self, location: str):
        data = self.service.get_weather(location)
        forecast = self.strategy.generate_forecast(data)
        return forecast