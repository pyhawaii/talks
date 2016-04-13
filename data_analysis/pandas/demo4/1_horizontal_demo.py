# <demo> stop
# generate a horizontal bar chart
# (based on an example from the matplotlib website...)
# http://matplotlib.org/1.2.1/examples/pylab_examples/barh_demo.html

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# <demo> stop
# we'll use pandas to read in some data, but we'll only keep two of the columns

df = pd.read_csv('../../log_file.csv', names=['name',
                                                  'email',
                                                  'fmip',
                                                  'toip',
                                                  'date',
                                                  'lat',
                                                  'long',
                                                  'payload'],
                                            usecols=['name'])

# <demo> stop
# to generate this graph, we are gonna make up a set of random numbers between 
# 42 and 48.5
# NOTE:
#     0) the function len(df) returns the number of rows in df
#     1) np.random.rand yields numbers between [0 and 1].
#

df['fan_rating'] = 42 + 6.5 * np.random.rand(len(df))

# <demo> stop
# as a first step, let's clean up the data by dropping duplicate rows using
# these rules/parameters:
#     0) check whether there is a duplicate in a given column
#     1) keep only the last value of any duplicates (default is to take the first)
#     2) replace the dataframe with our new deduplicated version

df.drop_duplicates(subset='name', inplace=True, take_last=True)

# NOTE: in this case, we will get a warning that the argument 'take_last'
# has been deprecated. This function has been modernized and now uses the
# argument 'keep' instead.

# <demo> stop
# let's convert the content of the name column from first & last to just first name
# we do this by generating a function to do the conversion on a single value

def fname_only(full_name):
    fname = full_name.split(' ')[0]
    return fname

# the map() function associated with dataframe columns maps the named function against
# every item in every row of the given column
# NOTE:
#     Remember, pandas has several ways to refer to columns:
#     0) when creating a new column, you must use bracket syntax: df['<colname>']
#     1) to refer to an existing column, you are free to use either
#        bracket syntax OR dot notation syntax: df.<colname>
#        I find the dot notation easier to type, so defer to it when possible

df['fname'] = df.name.map(fname_only)

# lastly, let's extract just the values out of the fname column.
# this is a list-like object and will be used as the names for our horizontal bars
# later.

people = df.fname.values

# <demo> stop
# now we can put together a sequence that will
# store the y position values. we'll use np.arange to create an array of
# sequential values based on the length of the people array
# this will be used as a set of temporary names for our horizontal bars...
# ultimately, we will replace it with real names...

# plus, we will save off the fan rating as a series for use
# in the plotting software as the x values

y_pos = np.arange(len(people))

performance = df['fan_rating']

# <demo> stop
# based on this preliminary work, we can generate a
# simple horizontal bar chart
# we give it y values and x values
# and we tell it to show() the plot

plt.barh(y_pos, performance)
plt.show()

# <demo> stop
# presume we don't like the alignment of the names against the horizontal bars.
# we can align the names to the center of the bars.

plt.barh(y_pos, performance, align='center')
plt.show()

# <demo> stop
# what if we don't like the dark color? we can revise the color to have a
# greater degree of transparency by setting the alpha characteristic

plt.barh(y_pos, performance, align='center', alpha=0.4)
plt.show()

# <demo> stop
# what if we don't like the default color? we can revise the color as desired
# matplotlib has a number of default colors: 'r' stands for red

plt.barh(y_pos, performance, align='center', alpha=0.4, color='r')
plt.show()

# <demo> stop
# what if our data comes with some percentage of error?
# this can be represented using an xerr parameter.
# here, we again use random to generate a random set of values that we can
# then use to generate error bars. in real life, you would have some
# margin for error for all the values.

error = np.random.rand(len(people))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4, color='r')
plt.show()

# <demo> stop
# this still leaves off info that most of us would want, in terms of the
# people names, title, axis labels, etc.

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4, color='r')

plt.yticks(y_pos, people)
plt.xlabel('rating')
plt.title("Estimated Justice League's Fan Ratings")
plt.savefig('hbar.png')

