
'''

Uses info from the as-505-ascent-phase-data.txt to make 11 plots of each variable against time. Also prints a graph
of the latitude and longitude track over a map of the Earth, color-coded by the altitude.

'''

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

df_apollo = pd.read_csv('as-505-ascent-phase-data.txt', comment='$', sep=',', header=[0,1], skipinitialspace=True)
apollo1 = df_apollo.astype(float) # Converting everything to a float type (not int because I don't want it to round)
apollo2 = apollo1.to_dict('list') # Converting the pd dataframe to a dictionary

y_axes = list(apollo2.keys()) # Names of all the columns
y_axes_key = 0

# Create graphs of every column vs time on a 4x3 grid
# Iterating over all columns
fig, axs = plt.subplots(4, 3)
for i in range(4):
    for j in range(3):
        axs[i, j].plot(apollo2[('TIME', 'SEC')], apollo2[y_axes[y_axes_key]])
        axs[i, j].set_xlabel(y_axes[0][0] + ' (' + y_axes[0][1] + ')')
        axs[i, j].set_ylabel(y_axes[y_axes_key][0] + ' (' + y_axes[y_axes_key][1] + ')')
        axs[i, j].set_title(y_axes[0][0] + ' vs ' + y_axes[y_axes_key][0])
        axs[i, j].grid()
        y_axes_key += 1
fig.delaxes(axs[0,0]) # Deleting the TIME v TIME plot
fig.set_figheight(32)
fig.set_figwidth(30)
plt.show()

fig = plt.figure(figsize=(12,9))
im = plt.imread('NE1_50M_SR_W_CROPPED_1080.png') # Map of the Earth
ax = fig.add_subplot(1, 1, 1)
ax.imshow(im, extent=[-120, -30, 15, 60])
ax.set_aspect('equal')
plt.scatter(apollo2[('LONG', 'DEG E')], apollo2[('GC LAT', 'DEG N')], c=apollo2[('ALTITUDE', 'M')])
plt.colorbar(label='Altitude (M)')
plt.xlabel('Longitude (DEG E)')
plt.ylabel('Latitude (DEG N)')
plt.grid()
plt.title('Apollo 10 Rocket\'s Groundtrack')
