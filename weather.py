import json
import requests
import sys

# current weather or 5-days/3 hours forecast can be searched by
# By city name
# By city ID
# By geographic coordinates
# By ZIP code

# usage ->
def main():
    key = "64018178f1e2f943f959087caa369c63"
    # Minneapolis,us
    query = sys.argv[1]
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (query, key)
    request = requests.get(url)
    print(request)


if __name__ == "__main__":
    main()
