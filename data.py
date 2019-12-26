import json
import difflib

# class for handling city and country data
class Data:
    city_names = []
    cities = []
    country_names = []
    countries = []

    def __init__(self):
        self.loadCities()
        self.loadCountries()

    def loadCities(self):
        with open('city.list.json', encoding="utf8") as json_file:
            data = json.load(json_file)
            for city in data:
                self.cities.append(city)
                self.city_names.append(city['name'])

    def loadCountries(self):
        with open('country.list.json') as json_file:
            data = json.load(json_file)
            for country in data:
                self.countries.append(country)
                self.country_names.append(country['name'])
    
    def getCities(self):
        return self.cities
    
    def getCountries(self):
        return self.countries

    def getClosestCountryMatch(self, country_name):
        close_matches = difflib.get_close_matches(country_name, self.country_names)
        return close_matches
    
    def getClosestCityMatch(self, city_name):
        close_matches = difflib.get_close_matches(city_name, self.city_names)
        return close_matches

    def getCountryCode(self, country_name):
        for country in self.countries:
            if country_name == country['name']:
                return country['code']
        return ""
    
    def getCityId(self, city_name, country_code):
        for city in self.cities:
            if (city['name'] == city_name) and (city['country'] == country_code):
                return city['id']
        return 1