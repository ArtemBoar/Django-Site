import requests

class WeatherAPI:
    API_KEY = '9a6bea2d365d94ebb5e189249a0b6e53'
    API_LINK = 'http://api.openweathermap.org/data/2.5/weather'

    @classmethod
    def get_weather_info(cls):
        params = {'q': 'Kyiv', 'appid': cls.API_KEY, 'units': 'metric'}
        response = requests.get(url=cls.API_LINK, params=params)
        return cls.format_response(response)

    @staticmethod
    def format_response(response):
        response_data = response.json()
        return response_data.get('main', {}).get('temp')

if __name__ == '__main__':
    print(WeatherAPI.get_weather_info())
