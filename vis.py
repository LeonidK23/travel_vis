from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

fig = plt.figure(num=None, figsize=(20, 20))
m = Basemap(projection='merc', llcrnrlat=31, urcrnrlat=69, llcrnrlon=-15, urcrnrlon=36, resolution='i')
m.drawcoastlines()
plt.show()
