import requests

points = [
    (37.619815, 55.760274), # Красная площадь
    (37.607739, 55.776806),  # Парк Зарядье
    (37.554191, 55.715551) # Лужники
]

path_points = ",".join([f'{point[0]},{point[1]}' for point in points])
base_url = 'https://static-maps.yandex.ru/1.x?'
params = {
    'pl': path_points,
    'pt': f'{points[1][0]},{points[1][1]},vkbkm',
    'l': 'map',
    'apikey': 'c064e049-8398-4afb-9a76-9887ef3af4ec'
}

try:
    response = requests.get(url=base_url, params=params)
except ConnectionError:
    print(ConnectionError, "Проверьте подключение к сети.")
else:
    with open('ex2/ex2.png', 'wb') as file:
        file.write(response.content)