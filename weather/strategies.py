### weather/strategies.py

from abc import ABC, abstractmethod
from .models import WeatherData

class ForecastStrategy(ABC):
    @abstractmethod
    def generate_forecast(self, data: WeatherData) -> str:
        pass

class SimpleForecastStrategy(ForecastStrategy):
    def generate_forecast(self, data: WeatherData) -> str:
        return f"{data.location}: {data.condition}, {data.temperature}°C"
