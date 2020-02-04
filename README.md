# api-design-JWangNov

## Airport Information
Airport information is obtained and generated through the following link:

[Airport Information](https://github.com/datasets/airport-codes)

## Usage
### OpenWeather API Key
Get your OpenWeather API Key [here](https://openweathermap.org/price).

### Get Airport Weather
```
import getAirportWeather

obj = getAirportWeather("BOS", {YOUR_API_KEY})
curWthr = obj.getCurrent()
```

`curWthr` is the current weather of "BOS" airport. (in json format)

### Example
See an example [here](https://github.com/BUEC500C1/api-design-JWangNov/blob/master/example.py).
