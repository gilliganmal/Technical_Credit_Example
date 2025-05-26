### tests/test_strategies.py

import unittest
from weather.models import WeatherData
from weather.strategies import SimpleForecastStrategy

class TestSimpleForecastStrategy(unittest.TestCase):
    def test_generate_forecast(self):
        strategy = SimpleForecastStrategy()
        data = WeatherData(temperature=18, condition="cloudy", location="Melbourne")
        result = strategy.generate_forecast(data)
        self.assertEqual(result, "Melbourne: cloudy, 18°C")

if __name__ == '__main__':
    unittest.main()