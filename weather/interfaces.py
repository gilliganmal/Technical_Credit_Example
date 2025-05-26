### weather/interfaces.py

from abc import ABC, abstractmethod
from typing import List
from .models import WeatherData

class WeatherService(ABC):
    @abstractmethod
    def get_weather(self, location: str) -> WeatherData:
        pass