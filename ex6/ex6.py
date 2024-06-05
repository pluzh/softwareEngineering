import requests
import random
import webbrowser


def get_coordinates(city_name):
    api_key = "3c765e4d-7e03-4a9c-95e4-0606a0a95c04"
    endpoint = "https://geocode-maps.yandex.ru/1.x/"

    params = {
        "apikey": api_key,
        "geocode": city_name,
        "format": "json"
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    coordinates = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = map(float, coordinates.split())

    return lat, lon

cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]

def get_city_image(lat, lon):
    api_key = "c064e049-8398-4afb-9a76-9887ef3af4ec"
    endpoint = f"https://static-maps.yandex.ru/1.x/?apikey={api_key}"

    map_type = random.choice(["map", "sat"])

    params = {
        "ll": f"{lon},{lat}",
        "size": "250,250",
        "l": "map",
        "z": "12"
    }

    response = requests.get(endpoint, params=params)

    image_url = response.url
    return image_url

def display_image(image_url):
    webbrowser.open_new_tab(image_url)

def main():
    while True:
        random.shuffle(cities)
        for city in cities:
            lat, lon = get_coordinates(city)
            image_url = get_city_image(lat, lon+0.1)
            display_image(image_url)
            
            input("Угадайте название города: ")
            print(f"Правильный ответ: {city}\n")
            
            input("Нажмите Enter, чтобы продолжить...")
    
if __name__ == "__main__":
    main()