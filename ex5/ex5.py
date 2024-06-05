import requests

def find_nearest_pharmacy(address):
    geo_api_key = '3c765e4d-7e03-4a9c-95e4-0606a0a95c04'
    search_api_key = '98f1d3df-60fe-4110-92dd-5f822333c025'

    try:
        geocode_response = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={geo_api_key}&format=json&geocode={address}')
        geocode_data = geocode_response.json()
        
        coordinates = geocode_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        longitude, latitude = map(float, coordinates.split())

        pharmacy_response = requests.get(f'https://search-maps.yandex.ru/v1/?apikey={search_api_key}&text=аптека&ll={longitude},{latitude}&type=biz&lang=ru_RU&results=1')
        pharmacy_data = pharmacy_response.json()

        nearest_pharmacy = pharmacy_data['features'][0]
        name = nearest_pharmacy['properties']['name']
        address = nearest_pharmacy['properties']['CompanyMetaData']['address']

        return name, address
    except Exception as e:
        return "Ошибка при поиске аптеки:", str(e)

if __name__ == "__main__":
    address = input("Введите адрес: ")
    result = find_nearest_pharmacy(address)
    print("Ближайшая аптека:")
    print("Название:", result[0])
    print("Адрес:", result[1])