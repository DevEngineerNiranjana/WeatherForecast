import logging
import uuid

import requests

from common.constants import *
from common.weatherForecast import FetchWeather


class DataPoints:

    def __init__(self) -> None:
        logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', level=logging.DEBUG)
        self.__db_obj = MONGO_CLIENT["weather"]["data_points"]
        self.__forecast_db = MONGO_CLIENT["weather"]["forecast_data"]

    def get_data_point(self, location):
        try:
            data = self.__db_obj.find_one({"location": location})
            if data:
                return True, data
            return False, {}
        except Exception as err:
            logging.error("GET request failed. Exception :: " + str(err))
            return False, {}

    def update_data_point(self, location, input_json):
        try:
            condition = {"location": location}
            query = {"$set": {
                "longitude": input_json["longitude"],
                "latitude": input_json["latitude"],
                "min_temp": input_json["min_temperature"],
                "max_temp": input_json["max_temperature"]}
            }
            self.__db_obj.update_one(condition, query)
            logging.info("Successfully Updated datapoint")
            return True
        except Exception as err:
            logging.error("PUT request failed. Exception :: " + str(err))
            return False

    def delete_data_point(self, location):
        try:
            query = {"location": location}
            self.__db_obj.remove(query)
            logging.info("Successfully deleted Datapoint")
            return True
        except Exception as err:
            logging.error("DELETE request failed. Exception :: " + str(err))
            return False

    def get_all_data_point(self):
        try:
            data = []
            for d in self.__db_obj.find({}):
                data.append(d)
            if data:
                logging.info("Successfully fetched data points")
                return True, data
            return False, {}
        except Exception as err:
            logging.error("GET request failed. Exception :: " + str(err))
            return False, {}

    def add_data_point(self, input_data):
        try:
            unique_id = str(uuid.uuid4())
            query = {
                "_id": unique_id,
                "location": input_data["location"],
                "longitude": input_data["longitude"],
                "latitude": input_data["latitude"],
                "min_temp": input_data["minimum_temperature"],
                "max_temp": input_data["maximum_temperature"],
            }
            forecast_obj = FetchWeather()
            lat = input_data["latitude"]
            long = input_data["longitude"]
            forecast_response = forecast_obj.fetch_forecast_data_by_lat_long(lat, long)
            forecast_data = {}
            for i in forecast_response:
                forecast_data = i
            if forecast_data:
                query["forecast"] = {}
                query["forecast"]["location"] = forecast_data["location"]
                query["forecast"]["forecast_day"] = forecast_data["forecast"]["forecastday"]
                # forecast_data["_id"] = unique_id
                # self.__forecast_db.insert_one(forecast_data)
                logging.info("Forecast data inserted for location" + input_data["location"])
            self.__db_obj.insert_one(query)
            logging.info("data point inserted for location" + input_data["location"])
            return True
        except Exception as err:
            logging.error("POST request failed. Exception :: " + str(err))
            return False

    def rerun_forecast(self, lat, long):
        try:
            forecast_obj = FetchWeather()
            forecast_response = forecast_obj.fetch_forecast_data_by_lat_long(lat, long)
            forecast_data = {}
            for i in forecast_response:
                forecast_data = i
            if forecast_data:
                condition = {"latitude": lat, "longitude": long}
                query = {"forecast": {}}
                query["forecast"]["location"] = forecast_data["location"]
                query["forecast"]["forecast_day"] = forecast_data["forecast"]["forecastday"]
                self.__db_obj.update_one(condition, {"$set": query})
                logging.info("Successfully Updated datapoint")
                return True
            return False
        except Exception as err:
            logging.error("PUT request failed. Exception :: " + str(err))
            return False
