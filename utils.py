
def countryInput():
    print("\nPlease enter a country. e.g. United States\n")
    country = input()
    return country

def getCountryCode(data):
    close_matches = []
    first_run = True
    while len(close_matches) == 0:
        if first_run == False:
            print("\nNo close matches found. Try again")
        country_name = countryInput()
        close_matches = data.getClosestCountryMatch(country_name)
        first_run = False
    while len(close_matches) > 0:
        if country_name == close_matches[0]:
            country_code = data.getCountryCode(country_name)
            return country_code
        else:
            print("\nDid you mean " + close_matches[0] + "? y/n\n")
            answer = input()
            while answer != "y" and answer != "n":
                print("\nPlease enter y or n\n")
                answer = input()
            if answer == "y":
                country_code = data.getCountryCode(close_matches[0])
                return country_code
            elif answer == "n":
                country_name = countryInput()
                close_matches = data.getClosestCountryMatch(country_name)
    return ""

def cityInput():
    print("\nPlease enter a city. e.g. Minneapolis\n")
    city = input()
    return city

def getCity(data):
    close_matches = []
    first_run = True
    while len(close_matches) == 0:
        if first_run == False:
            print("\nNo close matches found. Try again")
        city_name = cityInput()
        close_matches = data.getClosestCityMatch(city_name)
        first_run = False
    while len(close_matches) > 0:
        if city_name == close_matches[0]:
            return city_name
        else:
            print("\nDid you mean " + close_matches[0] + "? y/n\n")
            answer = input()
            while answer != "y" and answer != "n":
                print("Please enter y or n\n")
                answer = input()
            if answer == "y":
                return close_matches[0]
            elif answer == "n":
                city_name = cityInput()
                close_matches = data.getClosestCityMatch(city_name)
    return ""

def printTemperature(response, city):
    response_json = response.json()
    print("\nEnter f for Farenheit or c for Celsius\n")
    unit = input()
    temperature_in_kelvin = response_json['main']['temp']
    temperature_in_farenheit = round((temperature_in_kelvin * 9/5 - 459.67), 2)
    temperature_in_celsius = round(temperature_in_kelvin - 273.15, 2)
    if unit == "f":
        print("\nCurrent temperature in " + city +
            " is " + str(temperature_in_farenheit) + "°F")
    elif unit == "c":
        print("\nCurrent temperature in " + city +
            " is " + str(temperature_in_celsius) + "°C")