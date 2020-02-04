import pytest
from getAirportWeather import *
# from myOpenWeatherKey import *

def test0():
    obj0 = getAirportWeather("BOS")
    assert obj0.latitude == "42.36429977"
    assert obj0.longitude == "-71.00520325"

# def test1():
#     obj1 = getAirportWeather("BOS", myKey)
#     out1 = """{'coord': {'lon': -71.01, 'lat': 42.36}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 276.34, 'feels_like': 270.87, 'temp_min': 274.15, 'temp_max': 278.71, 'pressure': 1009, 'humidity': 69}, 'wind': {'speed': 4.6, 'deg': 90}, 'clouds': {'all': 100}, 'dt': 1580828431, 'sys': {'type': 1, 'id': 4967, 'country': 'US', 'sunrise': 1580817301, 'sunset': 1580853648}, 'timezone': -18000, 'id': 4955993, 'name': 'Winthrop', 'cod': 200}"""
#     assert obj1.getCurrent() == out1

def test2():
    with pytest.raises(Exception):
        assert(getAirportWeather("123"))
        assert(getAirportWeather("BOS", "notakey..."))  
