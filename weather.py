import json
import requests
import sys
import utils
from data import Data
from ascii import Ascii

# current weather or 5-days/3 hours forecast can be searched by
# By city name
# By city ID
# By geographic coordinates
# By ZIP code

#country.list.json credit to Félix Bellanger (keeguon on Github)

# usage -> python weather.py
# output: What city?
# input: city
# output: whtat country?


#TODO: case insensitive for country and city lookup
#TODO: get weather based off current location
#TODO: What if multiple cities of same name in one country?

def main():
    data = Data()
    country_code = utils.getCountryCode(data)
    city = utils.getCity(data)
    id = data.getCityId(city, country_code)
    key = "64018178f1e2f943f959087caa369c63"
    url = "https://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s" % (id, key)
    response = requests.get(url)
    if response.status_code == 200:
        utils.parseWeather(response)
        utils.printTemperature(response, city)
    else:
        print(response)
        print("Error: Response status code not 200, contact jaredlim320@gmail.com")


if __name__ == "__main__":
    main()
