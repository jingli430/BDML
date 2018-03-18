#!/usr/bin/python
import sys

oldKey = None
weekday_cost = 0

for line in sys.stdin:

    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    thisKey, cost = data
    if oldKey and thisKey != oldKey:
        print "{0}\t{1}".format(oldKey, weekday_cost)
        # reset
        weekday_cost = 0

    oldKey = thisKey
    weekday_cost += float(cost)

if oldKey:
    print "{0}\t{1}".format(oldKey, weekday_cost)
