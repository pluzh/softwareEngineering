import requests
import io
from PIL import Image
from staticmap import StaticMap, CircleMarker

def get_satellite_image(latitude, longitude, zoom=15, size=(640, 640)):
    m = StaticMap(size[0], size[1], url_template='https://tile.openstreetmap.org/{z}/{x}/{y}.png')

    marker = CircleMarker((longitude, latitude), '#FF0000', 10)
    m.add_marker(marker)

    image = m.render(zoom=zoom)

    image.save('ex3/ex3.png')

latitude = 55.7522
longitude = 37.6156

get_satellite_image(latitude, longitude)

print(f"Спутниковый снимок сохранен в файл ex3/ex3.png")