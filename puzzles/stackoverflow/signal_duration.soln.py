# This puzzle derives from a question I saw on Stackoverflow. The original
# question is here:

# https://stackoverflow.com/questions/46268589/compute-the-length-of-consecutive-true-values-in-a-list

# You are given a set of binary values that indicate whether a signal is
# present or not. Each value corresponds to a unit of time
# (in this case minutes).

# QUESTION:  determine the average length of the 'on' signals given their
# occurrences within the overall list of values.
# For this scenario, use the following list:

# [0,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0]

# We can see that the signal (1) occurs 3 separate times and 'stays on' for
# variable lengths of time (i.e. in the first case for 3 minutes). Our
# objective is to calculate the average length of time for each occurrence.


# [0,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0]
#    ^   ^     ^
#    |   |     |
#  Off   |     |
#       On     |
#      Off again

# -----------------------------------------------------------
l = [0,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0]

# Your code here...

# version 1...
def size(xs):
    sz = 0
    for x in xs:
        # if x equals 0 AND sz is more than 0
        # yield sz
        # and set sz = 0
        if x == 0 and sz > 0:
            yield sz
            sz = 0
        # but if x equals 1
        # increment sz by 1
        if x == 1:
            sz += 1
    if sz > 0:
        yield sz

results = list(size(l))
average = sum(results)/len(results)


# version 2...
from itertools import groupby

on = []

for k, g in groupby(l):
    g = list(g)
    if g[0]:
        on.append(len(g))
    print(k, g, len(g))

average = sum(on)/len(on)
