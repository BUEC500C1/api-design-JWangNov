import json
from getAirportWeather import *


"""get current weather of Tivat Airport"""
try:
    tiv = getAirportWeather("TIV", "{API_KEY}")
    info = tiv.getCurrent()
    print("Airport Name:     ", tiv.airportName)
    print("Latitude:         ", info['coord']['lat'])
    print("Longitude:        ", info['coord']['lon'])
    print("Elevation (ft):   ", tiv.elevation)
    print("Weather:          ", info['weather'][0]['main'])
    print("                  ", info['weather'][0]['description'])
    print("Temperature (K):  ", info['main']['temp'])
    print("Real Feel (K):    ", info['main']['feels_like'])
    print("Pressure (Pa):    ", info['main']['pressure'])
    print("Humidity:         ", info['main']['humidity'], "%")
    print("Wind Speed:       ", info['wind']['speed'])
    print("Wind Direction:   ", info['wind']['deg'])

except Exception as e:
    raise e


"""
After I replaced {API_KEY} with my API key,
the output is shown:

Airport Name:      Tivat Airport
Latitude:          42.4
Longitude:         18.72
Elevation (ft):    20
Weather:           Rain
                   shower rain
Temperature (K):   286.6
Real Feel (K):     283.55
Pressure (Pa):     1000
Humidity:          82 %
Wind Speed:        4.6
Wind Direction:    160
"""
