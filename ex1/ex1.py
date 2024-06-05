import requests

apikey = "c064e049-8398-4afb-9a76-9887ef3af4ec"

stadiums_location = ["37.554191,55.715551", "37.440262,55.818015","37.559809,55.791540"]

base_url = f'https://static-maps.yandex.ru/v1?ll=37.617603%2C55.743700&z=11&l=map&lang=ru_RU&width=600&height=400&mode=json'

params = {
    "pt": f"{stadiums_location[0]},vkbkm~{stadiums_location[1]},vkbkm~{stadiums_location[2]},vkbkm",
    "apikey": f"{apikey}"
}

try:
    response = requests.get(url=base_url, params=params)
except ConnectionError:
    print(ConnectionError, "Проверьте подключение к сети.")
else:
    with open('ex1/ex1.png', 'wb') as file:
        file.write(response.content)
