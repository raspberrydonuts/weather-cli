import json
import difflib

def getClosestCountryMatch(country_name):
    countries = []
    with open('country.list.json') as json_file:
        data = json.load(json_file)
        for country in data:
            name = country['name']
            countries.append(name)
    # search country.list.json for country, or closest to
    print(country_name)
    close_matches = difflib.get_close_matches(country_name, countries)
    print(close_matches)
    # return country code
    return close_matches

def getCountryCode(country_name):
    with open('country.list.json') as json_file:
        data = json.load(json_file)
        for country in data:
            if country_name == country['name']:
                return country['code']
    return ""

def getCityId(city, country_code):
    # search city.list.json for a matching city with country code
    # return id
    return 1

def countryInput():
    print("Please enter a country. e.g. United States")
    country = input()
    return getClosestCountryMatch(country)