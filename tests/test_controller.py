import pytest
from weather import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_list_products(client):
    response = client.get('/api/v1/products/')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
### tests/test_controller.py

import unittest
from weather.controller import WeatherController
from weather.models import WeatherData
from weather.strategies import SimpleForecastStrategy

class MockWeatherService:
    def get_weather(self, location):
        return WeatherData(temperature=22.5, condition="sunny", location=location)

class TestWeatherController(unittest.TestCase):
    def test_display_weather(self):
        service = MockWeatherService()
        strategy = SimpleForecastStrategy()
        controller = WeatherController(service, strategy)
        forecast = controller.display_weather("Sydney")
        self.assertIn("Sydney", forecast)

if __name__ == '__main__':
    unittest.main()