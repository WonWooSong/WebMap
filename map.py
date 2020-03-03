import folium
import pandas

data = pandas.read_csv("data/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3500:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.GeoJson(data=open('data/world.json', 'r', encoding='utf-8-sig').read()))

for lat,lon,elev in zip(lat,lon,elevation):
    fg.add_child(folium.Marker(location=[lat,lon], popup=folium.Popup(str(elev), parse_html=True), icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")