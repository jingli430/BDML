#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv
import heapq

# reducer这边的top10应该是汇总来自多个mappers的top10
# 这道题由于求得是global top10，所以最后一定需要汇总到一个reducer。
# 本质上和mapper那边算法一样。都是求top10


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    # 这个PQ的Entries are typically tuples of the form:  (priority number, data).
    # And priority_number should be int
    # Get the first 10 lines
    top_ten = [reader.next() for _ in range(10)]
    # reshape it as tuple (len(line[4]), line)
    top_ten = [(len(line[4]), line) for line in top_ten]
    # init minHeap
    heapq.heapify(top_ten)
    # process the rest
    for line in reader:
        print(len(line[4]), line)
        if (len(line[4]), line) > top_ten[0]:
            # push and pop
            heapq.heappushpop(top_ten, (len(line[4]), line))
    while top_ten:
        writer.writerow(heapq.heappop(top_ten)[1])


# This function allows you to test the mapper with the provided test string
# But you should comment out if you use another dataset as input
# def main():
#     import StringIO
#     sys.stdin = StringIO.StringIO(test_text)
#     mapper()
#     sys.stdin = sys.__stdin__
#
#
# if __name__ == '__main__':
#     main()

