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
print(average)

# version 2...

signals = []
previous_sig = 0

for item in l:
    if item == 1 and previous_sig == 0:
        # starting a new signal
        signals.append([item])

    elif item == 1 and previous_sig == 1:
        # continuing the signal...
        signals[-1].append(item)

    previous_sig = item

num = len(signals)

average = sum(len(sublist) for sublist in signals) / num

print(average)


# version 3...
from itertools import groupby

on = []

for value, grp in groupby(l):
    if value:
        on.append(list(grp))

    # print(k, g, len(g))

num = len(on)
print(sum(len(sublist) for sublist in on) / num)

# version 4...
from itertools import groupby
from statistics import mean

def mean_duration(l):
   """
   Takes in a list l whose values will be cast to boolean
   
   Finds the average length of runs of True
   
   >>> mean_duration([0,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0])
   2.6666666666666665
   >>> mean_duration([0,0,0,1,2,5,0,0,1,0,0,0,1,7,1,1,0])
   2.6666666666666665
   """
   return mean(len(list(g)) for v, g in groupby(map(bool,l)) if v)
