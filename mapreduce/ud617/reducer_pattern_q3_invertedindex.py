#!/usr/bin/python
import sys
import csv

'''
reducer input: <key=word, value=nodeId>
reducer output: <key=word, value=(total_count, List_of_comma_separated_nodes_in_ascending_order)>
'''
oldWord = None
word_count = 0
set_nodes = set()

# since the key and value are enclosed by double quotes and delimited by \t, it is better to use the same way to read
reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if len(line) != 2:
        continue
    thisWord, node_id = line
    if oldWord and thisWord != oldWord:
        # sort should be based on int value, so need to do the conversion
        sorted_nodes_comma_separated_str = ",".join(str(x) for x in sorted(list(set_nodes)))
        # output
        print "{0}\t{1}".format(oldWord, (word_count, sorted_nodes_comma_separated_str))
        # reset for next word
        word_count = 0
        set_nodes = set()

    oldWord = thisWord
    word_count += 1
    set_nodes.add(int(node_id))

# don't forget last word
if oldWord:
    sorted_nodes_comma_separated_str = ",".join(str(x) for x in sorted(list(set_nodes)))
    print "{0}\t{1}".format(oldWord, (word_count, sorted_nodes_comma_separated_str))