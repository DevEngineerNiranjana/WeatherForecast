import configparser
import logging
import os


class ParseConfig:
    __config = configparser.ConfigParser()
    __results = dict()

    def __init__(self, file_name):
        self.__config.read(file_name)

    def get_server_details(self):
        server_details = self.__config['SERVER_DETAILS']
        if server_details['ServerIP']:
            self.__results["host"] = server_details['ServerIP']
        if server_details['ServerListeningPort']:
            self.__results["port"] = server_details['ServerListeningPort']
        print("Host: " + self.__results["host"])
        print("Port: " + self.__results["port"])
        return self.__results
