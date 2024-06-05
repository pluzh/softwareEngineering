import sys
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

geolocator = Nominatim(user_agent="http")

cities = []

input_cities = input("Введите список городов через запятую: ")
for city in input_cities.split(","):
    location = geolocator.geocode(city)
    if location is not None:
        cities.append((city, (location.latitude, location.longitude)))
    else:
        print(f"Не удалось найти координаты для {city}", file=sys.stderr)

if not cities:
    print("Ни один город не был найден.", file=sys.stderr)
else:
    southernmost_city = min(cities, key=lambda x: x[1][0])
    print(southernmost_city[0])