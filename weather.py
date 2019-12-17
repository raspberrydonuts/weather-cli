import json
import requests
import sys
import utils

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
def main():
    # if len(sys.argv) < 2:
    #     print("Please input a location as an argument")
    #     print("Example: Minneapolis,US")
    #     exit()
    country_matches = utils.countryInput()
    country = ""
    country_code = ""
    if len(country_matches) == 0:
        country = country_matches[0]
        country_code = utils.getCountryCode(country)
    while len(country_matches) > 0:
        country = country_matches[0]
        print("Did you mean " + country + "? y/n")
        answer = input()
        while answer != "y" or answer != "n":
            print("Please enter y or n")
            answer = input()
        if answer == "y":
            country_code = utils.getCountryCode(country)
        elif answer == "n":
            country_matches = utils.countryInput()

    print("Please enter a city. e.g. Minneapolis")
    city = input()
    id = utils.getCityId(city, country_code)
    key = "64018178f1e2f943f959087caa369c63"
    # query = sys.argv[1]
    # url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (query, key)
    url = "https://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s" % (id, key)
    response = requests.get(url)
    if response.status_code == 200:
        # x * 9/5 - 459.67
        response_json = response.json()
        temperature_in_kelvin = response_json['main']['temp']
        temperature_in_farenheit = round((temperature_in_kelvin * 9/5 - 459.67), 2)
        print("Current temperature in " + city + ", " + county +
        " is " + str(temperature_in_farenheit) + "°F")
    else:
        print("Error: Response status code not 200")


if __name__ == "__main__":
    main()
