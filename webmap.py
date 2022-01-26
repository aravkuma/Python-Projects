
import folium
import pandas

#Importing the volcanoes.txt file
data = pandas.read_csv("Volcanoes.txt")
#Extracting the latitude & longitude from the txt file
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#Defining a function for the dynamic assignment of colors for the icon
def colors(elevation):
    if elevation < 1000:
        return 'blue'
    if 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start= 6, tiles="Stamen Terrain")

#Adding a Feature group so that it can also be used later
fgv = folium.FeatureGroup(name="Volcano Map")

#Iterating the LAT, LONG, ELEV in for loop and change the marker to circle from default
for lt, lo, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, lo], radius=7, popup= str(el)+" m", icon=folium.Icon(color=colors(el)), fill_color=colors(el), color = 'grey', fill_opacity=1))

#Feature group for population
fgp = folium.FeatureGroup(name="World Population")

#Adding a population layer map from the world.json file &
#Differentiating the population of the world with styles
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function= 
lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 10000000 else 'yellow' 
if 20000000 <= x['properties']['POP2005'] < 40000000 
else 'grey' if 40000000 <= x['properties']['POP2005'] < 80000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map.html")