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
    close_matches = difflib.get_close_matches(country_name, countries)
    # return country code
    return close_matches

def getCountryCode(country_name):
    with open('country.list.json') as json_file:
        data = json.load(json_file)
        for country in data:
            if country_name == country['name']:
                return country['code']
    return ""

def getCityId(city_name, country_code):
    # search city.list.json for a matching city with country code
    with open('city.list.json', encoding="utf8") as json_file:
        data = json.load(json_file)
        for city in data:
            if (city['name'] == city_name) and (city['country'] == country_code):
                return city['id']
    # return id
    return 1

def countryInput(country):
    return getClosestCountryMatch(country)