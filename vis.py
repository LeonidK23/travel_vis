from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.animation

import warnings
import matplotlib.cbook

warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

# draw map of europe
fig = plt.figure(num=None, figsize=(15, 15))
m = Basemap(projection='merc', llcrnrlat=30, urcrnrlat=70, llcrnrlon=-13, urcrnrlon=42, resolution='l')
m.drawcoastlines()
m.fillcontinents(color='darkgrey',lake_color='dimgrey')
m.drawcountries()
m.drawmapboundary(fill_color='dimgrey')

belon = 13.404954; belat = 52.520008
lonlat = 51.53; lonlon = 0.08
line, = m.drawgreatcircle(belon, belat, lonlon, lonlat, color='yellow', linewidth=0.5)
x, y = line.get_data()

line.remove()

line, = plt.plot([], [])
def update(i):
    line.set_data(x[:i], y[:i])

ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(x) + 1, interval=200, repeat=False)

plt.tight_layout()
plt.show()
