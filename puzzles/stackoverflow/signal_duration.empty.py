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
