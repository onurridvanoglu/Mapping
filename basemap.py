import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map([38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location = [lt, ln], radius=6, popup = str(el) + " m", weight = 12, color = color_producer(el)))

map.add_child(fg)

map.save("Map1.html")
