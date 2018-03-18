#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    # user_ptr_id@user
    if len(line) == 5:
        my_list = [line[0], 'A'] + line[1:]
        writer.writerow(my_list)
    # author_id@node
    if len(line) == 19:
        # only interested in some columns from node side
        my_list = [line[3], 'B'] + line[:3] + line[5:10]
        writer.writerow(my_list)
