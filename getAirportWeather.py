import csv
import json
import os
import requests

# from myOpenWeatherKey import *


class getAirportWeather():
    """docstring for getAirportWeather"""
    def __init__(self, iata_code, api_key=""):
        self.iata_code = iata_code
        self.__key__ = api_key
        self.latitude = ""
        self.longitude = ""
        self.AIRPORT_CSV_PATH = "./data/airport-codes.csv"
        with open(self.AIRPORT_CSV_PATH, mode='r') as fff:
            csvReader = csv.DictReader(fff)
            found = False
            for row in csvReader:
                if row["iata_code"] == self.iata_code:
                    found = True
                    curr = row["coordinates"]
                    self.latitude = curr.split(",")[0]
                    self.longitude = curr.split()[1]
                    self.elevation = row["elevation_ft"]
                    self.airportName = row["name"]
            if not found:
                raise Exception("ERROR: IATA CODE NOT FOUND")

    """get the current weather of the airport"""
    def getCurrent(self):
        try:
            url = "http://api.openweathermap.org/data/2.5/weather?lat=" + self.latitude + "&lon=" + self.longitude + "&appid=" + self.__key__
            rrr = requests.get(url)
            if rrr.status_code != 200:
                raise Exception("ERROR: BAD REQUEST")
            return rrr.json()
        except:
            raise Exception("ERROR: INVALID RESPONSE")


# def runrun():
#     obj = getAirportWeather("BOS", myKey)
#     # print(obj.latitude, obj.longitude)
#     rjson = obj.getCurrent()
#     print(rjson)


# def failfail():
#     flflflfl = getAirportWeather("asduibovqq")


# if __name__ == '__main__':
#     runrun()
#     failfail()
