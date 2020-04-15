from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.animation

import warnings
import matplotlib.cbook

from data_processing import *

warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

flights = read_data("travels.csv")
cities = get_cities(flights)
city_coords = get_city_coords(cities)
flights_coords = add_coords(flights, city_coords)

# draw map of europe
fig = plt.figure(num=None, figsize=(15, 15))
m = Basemap(projection='merc', llcrnrlat=30, urcrnrlat=70, llcrnrlon=-13, urcrnrlon=42, resolution='l')
m.drawcoastlines(linewidth=0.4)
m.fillcontinents(color='darkgrey',lake_color='dimgrey')
m.drawcountries()
m.drawmapboundary(fill_color='dimgrey')

for flight in flights_coords:
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
# plt.tight_layout()
# --------------------------------
plt.show()
