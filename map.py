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

map = folium.Map(location=[40.0, -120.0], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('data/world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 25000000
else 'orange' if 25000000 <= x['properties']['POP2005'] < 55000000 else 'red'}))

for lat,lon,elev,name in zip(lat,lon,elevation,name):
    fgv.add_child(folium.CircleMarker(location=[lat,lon], popup=folium.Popup(str(name), parse_html=True), radius = 10,
    fill_color=color_producer(elev), fill=True,  color = 'grey', fill_opacity=0.7))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")