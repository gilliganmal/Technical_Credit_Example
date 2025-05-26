### weather/models.py

from dataclasses import dataclass

@dataclass
class WeatherData:
    temperature: float
    condition: str
    location: str