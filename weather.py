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
    print("Please enter a country. e.g. United States")
    country = input()
    country_matches = utils.countryInput(country)
    country_code = ""
    while len(country_matches) == 0:
        print("Could not find any countries close to what you're looking for. Please try again")
        country = input()
        country_matches = utils.countryInput(country)
    if country == country_matches[0]:
        country_code = utils.getCountryCode(country)
    else:
        while len(country_matches) > 0:
            country = country_matches[0]
            print("Did you mean " + country + "? y/n")
            answer = input()
            while answer != "y" and answer != "n":
                print("Please enter y or n")
                answer = input()
            if answer == "y":
                country_code = utils.getCountryCode(country)
                break
            elif answer == "n":
                print("Please enter a country. e.g. United States")
                country = input()
                country_matches = utils.countryInput(country)
            if len(country_matches) == 0:
                print("Could not find any countries close to what you're looking for. Please try again")
                country = input()
                country_matches = utils.countryInput(country)

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
        print("Enter f for farenheit or c for celsius")
        unit = input()
        temperature_in_kelvin = response_json['main']['temp']
        temperature_in_farenheit = round((temperature_in_kelvin * 9/5 - 459.67), 2)
        temperature_in_celsius = round(temperature_in_kelvin - 273.15, 2)
        if unit == "f":
            print("Current temperature in " + city +
                " is " + str(temperature_in_farenheit) + "°F")
        elif unit == "c":
            print("Current temperature in " + city +
                " is " + str(temperature_in_celsius) + "°C")
    else:
        print(response)
        print("Error: Response status code not 200")


if __name__ == "__main__":
    main()
