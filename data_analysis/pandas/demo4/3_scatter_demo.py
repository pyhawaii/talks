# <demo> stop
# generate a scatter plot
# (based heavily on an example from the matplotlib website...)
# http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# <demo> stop
# Let's read in a csv via pandas but keep only two of the columns

df = pd.read_csv('../../log_file_1000.csv', names=['name',
                                                   'email',
                                                   'fmip',
                                                   'toip',
                                                   'date',
                                                   'lat',
                                                   'long',
                                                   'payload'],
                                            nrows=35,
                                            usecols=['lat', 'long'])

# <demo> stop
# next, let's create two arrays from the lat and long columns

latitudes = df.lat
longitudes = df.long

# <demo> stop
# here we calculate the length of one of the arrays

count = len(latitudes)

# <demo> stop
# we'll use numpy to create a random collections of numbers for use in defining colors
# of the circles in our scatterplot

colors = np.random.rand(count)

# this step creates a random set of areas based on a radiuses from 0 to 20
# we can imagine that this is indicative of a the frequency of communications OR
# something similarly awesome and nerdy like that.
# np.pi gives us pi to 15 decimal places
# np.random.rand gives us random numbers from 0 to 1

areas = np.pi * (20 * np.random.rand(count))**2

# <demo> stop
# generate the scatter plot

plt.scatter(latitudes, longitudes, s=areas, c=colors) #, alpha=0.4)

# we chose to create stand alone variables (latitude, longitude) but these are not
# required... we can just as happily read in directly from df.lat or df.long:
# plt.scatter(df.lat, df.long, s=area, c=colors, alpha=0.4)

# <demo> stop
plt.savefig('scatter.png')
plt.show()
