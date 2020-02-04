# api-design-JWangNov

## Airport Information
Airport information is obtained and generated through the following link:

[Airport Information](https://github.com/datasets/airport-codes)

## Usage
### OpenWeather API Key
Get your OpenWeather API Key [here](https://openweathermap.org/price).

Run the following line and follow the instruction.

```
$ ./keyPrepare.sh
```

### Get Airport Weather
```
import getAirportWeather

obj = getAirportWeather("BOS", myKey)
curWthr = obj.getCurrent()
```

`curWthr` is the current weather of "BOS" airport. (in json format)
