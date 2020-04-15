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
fig = plt.figure(num=None, figsize=(6, 6))
m = Basemap(projection='merc', llcrnrlat=30, urcrnrlat=70, llcrnrlon=-13, urcrnrlon=42, resolution='i')
m.drawcoastlines(linewidth=0.4)
m.fillcontinents(color='darkgrey',lake_color='dimgrey')
m.drawcountries()
m.drawmapboundary(fill_color='dimgrey')

all_x = []
all_y = []
len_line = 0

for flight in flights:
    dep_lat, dep_lon = flight[2]
    dest_lat, dest_lon = flight[3]
    # get coordinates of lines
    line, = m.drawgreatcircle(dep_lon, dep_lat, dest_lon, dest_lat, color='yellow', linewidth=0.5)
    x, y = line.get_data()
    len_line = len(x)
    all_x = all_x + list(x)
    all_y = all_y + list(y)

    line.remove()

def update(i):
    line.set_data(all_x[:i], all_y[:i])

line, = plt.plot([],[], color='yellow', linewidth=0.5)
ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(all_x) + 1, interval=100, repeat=False)
plt.tight_layout()
# ani.save("travels.gif", writer="imagemagick", fps=10)
# plt.savefig("static_2d.png", bbox_inches="tight")
plt.show()
