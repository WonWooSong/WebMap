import folium
import pandas

data = pandas.read_csv("data/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lat,lon in zip(lat,lon,elevation):
    fg.add_child(folium.Marker(location=[lat,lon], popup="This is Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")