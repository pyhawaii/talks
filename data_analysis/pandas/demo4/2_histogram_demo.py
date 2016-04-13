# <demo> stop
# creating a histogram with some additional features
# (based heavily on an example from the matplotlib website...)
# http://matplotlib.org/1.2.1/examples/api/histogram_demo.html

# In addition to the basic histogram, this demo shows a few optional
# features:
#     * setting the number of data bins
#     * the ''normed'' flag, which normalizes bin heights so that the
#       integral of the histogram is 1. the resulting histogram is a
#       probability density
#     * setting the face color of the bars
#     * setting the opacity (alpha value)

# As always, we start by importing the appropriate libraries
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# <demo> stop
# we define some of the characteristics of our distribution:
mu = 100       # mean of the distribution
sigma = 15     # standard deviation of the distribution

# np.random.randn creates a random array of values taken from a
# standard normal distribution
# we can transform the distribution by multiplying the values by sigma and
# by adding the mean mu

x = mu + sigma * np.random.randn(10000)
print(x)

# we set a specific number of bins that we will group our values into...

num_bins = 50

# <demo> stop
# next we create the data for the histogram
# n = values (height) for each bar of the histogram
# bins = the indicators that demarck the bins
# patches = are the rectangle objects that represent each bar

n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
print(n)
print(bins)
# print(patches)
# for item in patches:
#     print(item)

plt.show()

# <demo> stop
# from here, we can add a 'best fit' line...
# the normal probability density function (pdf) helps to answer the question:
# "how common are samples at a given value?'

n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)

y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')

plt.show()

# <demo> stop
# And let's add some labels...

n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=0.7)
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'k--')

plt.xlabel('Smarts')
plt.ylabel('Probability')

plt.show()

# <demo> stop
# the opening '$\' and the closing '$' tags in the following commands enable you to
# include italics in the title

n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')

plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

plt.show()

# <demo> stop
# let's tweak the spacing to prevent clipping of our ylabels
# so that our plot looks professional and organized.

n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

plt.subplots_adjust(left=0.15)

plt.savefig('hist.png')
