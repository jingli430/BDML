#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv
import Queue as Q
import heapq


# Queue.PriorityQueue本质上是对heapq的再封装
# 同样的用list来存储heap，同样的是minHeap
# 当然，你也可以直接用heapq

# 如果直接用heapq, 常用的methods有下面5个
# 其实看heapq源码看他们的methods是如何实现的是一个很好的学习机会
# 1. heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.
# 2. heappush(heap, item) :- This function is used to insert the element mentioned in its arguments into heap. The order is adjusted, so as heap structure is maintained.
# 3. heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained.
# 4. heapreplace(heap, item) : -(pop and push) Pop and return the current smallest value, and add the new item
# 5. heappushpop(heap, item) : -(push and pop) Fast version of a heappush followed by a heappop.

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

test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""


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
