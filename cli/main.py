### cli/main.py

from weather.controller import WeatherController
from weather.strategies import SimpleForecastStrategy
from weather.adapter import OpenWeatherAdapter

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py <city>")
        sys.exit(1)

    location = sys.argv[1]
    service = OpenWeatherAdapter(api_key="your_api_key_here")
    strategy = SimpleForecastStrategy()
    controller = WeatherController(service, strategy)
    print(controller.display_weather(location))
