from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.animation
import pandas as pd

import warnings
import matplotlib.cbook

warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

# data processing
with open("travels.csv") as f:
    flights = f.readlines()

flights = [l.strip().split(",") for l in flights]
cities = set()
for flight in flights:
    source, dist = flight
    cities.add(source)
    cities.add(dist)

city_coords = dict()
df = pd.read_csv("worldcities.csv")
related_data = df.loc[df['city_ascii'].isin(cities)]
for city in cities:
    city_coords[city] = (0, 0)
    city_data = related_data.loc[related_data['city_ascii'] == city]
    if not city_data.empty:
        city_coords[city] = (city_data.iloc[0]['lat'], city_data.iloc[0]['lng'])

for flight in flights:
    dep = flight[0]
    dest = flight[1]
    flight += [city_coords[dep], city_coords[dest]]

# draw map of europe
fig = plt.figure(num=None, figsize=(8, 8))
m = Basemap(projection='merc', llcrnrlat=30, urcrnrlat=70, llcrnrlon=-13, urcrnrlon=42, resolution='l')
m.drawcoastlines(linewidth=0.4)
m.fillcontinents(color='darkgrey',lake_color='dimgrey')
m.drawcountries()
m.drawmapboundary(fill_color='dimgrey')

for flight in flights:
    dep_lat, dep_lon = flight[2]
    dest_lat, dest_lon = flight[3]
    m.drawgreatcircle(dep_lon, dep_lat, dest_lon, dest_lat, color='yellow', linewidth=0.5)

# --------animation part---------
# line, = m.drawgreatcircle(belon, belat, lonlon, lonlat, color='yellow', linewidth=0.5)
# x, y = line.get_data()
#
# line.remove()
#
# line, = plt.plot([], [])
# def update(i):
#     line.set_data(x[:i], y[:i])
#
# ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(x) + 1, interval=200, repeat=False)
#
# --------------------------------
plt.tight_layout()
plt.savefig("static_2d.png", bbox_inches="tight")
# plt.show()
