import json
import requests
import logging
from common.constants import *


class FetchWeather:

    def __init__(self) -> None:
        logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', level=logging.DEBUG)
        logging.info('Logger initiated.')

    def fetch_data(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("GET request completed successfully.")
            return True, response.json()
        else:
            logging.error("GET request failed. Status Code :: " + response.status_code)
            return False, response.json()

    # fetch current weather data
    def fetch_current_data_by_name_of_location(self, loc_name):
        url = "http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=" + loc_name + "&aqi=" + AIR_QUALITY_INDEX
        return self.fetch_data(url)

    # fetch forecast weather data
    def fetch_forecast_data_by_lat_long(self, lat, long):
        url = "http://api.weatherapi.com/v1/forecast.json?key=" + API_KEY + "&q=" + lat + ',' + long + "&days=" + FORECAST_DAYS + "&aqi=" + AIR_QUALITY_INDEX + "&alerts=" + ALERT
        return self.fetch_data(url)


data_fetcher = FetchWeather()

# status, data = data_fetcher.fetch_current_data_by_name_of_location(LOCATION_NAME)
# if status:
#     # parse data json
#     print(data)

# status, data = data_fetcher.fetch_forecast_data_by_name_of_location(LOCATION_NAME)
# if status:
#     # parse data json
#     print(status)
#     print(data)
