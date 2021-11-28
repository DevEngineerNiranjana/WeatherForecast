from pymongo import MongoClient

MONGO_CLIENT = MongoClient('mongodb://127.0.0.1:27017')
# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
MAPBOX_ACCESS_KEY = "pk.eyJ1IjoibmlyYW5qYW5hYXRoYXBwaWxsaWwiLCJhIjoiY2t3aTJiMGw1MGwxMDJ4cGt2aGsyM3pldSJ9.F5EAtTlEt7DVACANu_TXpQ"

API_KEY = "3ad1b5b131bb42289ab140422212311"
FORECAST_DAYS = "5"
AIR_QUALITY_INDEX = "yes"  # yes/no to enable or disable air quality index
LOCATION_NAME = "Kochi"
ALERT = "no"
