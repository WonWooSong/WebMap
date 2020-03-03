import folium
import pandas

data = pandas.read_csv("data/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])
name = list(data["NAME"])

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

for lat,lon,elev,name in zip(lat,lon,elevation,name):
    fg.add_child(folium.CircleMarker(location=[lat,lon], popup=folium.Popup(str(name), parse_html=True), radius = 10,
    fill_color=color_producer(elev), fill=True,  color = 'grey', fill_opacity=0.7))
map.add_child(fg)

map.save("Map1.html")