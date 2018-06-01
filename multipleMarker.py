import pandas
import folium

data = pandas.read_csv("Volcanoes-USA.txt");

minimum_elevation = min(data['ELEV'])
maximum_elevation = max(data['ELEV'])
average_lat = data['LAT'].mean()
average_lon = data['LON'].mean()
step = ((minimum_elevation-maximum_elevation)/3)*-1

map = folium.Map(location = [average_lat,average_lon], zoom_start = 4)

def color(elev):
	if elev in range(int(minimum_elevation),int(minimum_elevation+step)):
		col = 'green'
	elif elev in range(int(minimum_elevation+step),int(minimum_elevation+step+step)):
		col = 'orange'
	else:
		col = 'red'
	return col



for lat,lon,location,elevation in zip(data['LAT'],data['LON'],data['NAME'],data['ELEV']):
	popup = folium.Popup(location, parse_html=True)
	icon = folium.Icon(color = color(elevation))
	folium.Marker([lat,lon], popup = popup,icon = icon).add_to(map)

map.save("test.html")

