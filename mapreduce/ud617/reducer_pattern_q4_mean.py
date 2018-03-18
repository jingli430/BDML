#!/usr/bin/python
import sys
from datetime import datetime

oldKey = None
weekday_count = 0
weekday_cost = 0

for line in sys.stdin:

    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    thisKey, cost = data
    if oldKey and thisKey != oldKey:
        mean = weekday_cost / float(weekday_count)
        print "{0}\t{1}".format(oldKey, mean)
        # reset
        weekday_count = 0
        weekday_cost = 0

    oldKey = thisKey
    weekday_count += 1
    weekday_cost += float(cost)

if oldKey:
    mean = weekday_cost / float(weekday_count)
    print "{0}\t{1}".format(oldKey, mean)
