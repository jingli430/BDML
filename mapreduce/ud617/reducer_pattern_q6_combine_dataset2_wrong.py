#!/usr/bin/python
import sys

users_attrs = {}
posts_attrs = {}

for line in sys.stdin:
    data = line.strip().replace('"','').split("\t")
    if len(data) < 6:
        continue
    if data[1] == "A":
        users_attrs[data[0]] = data[2:]
    elif data[1] == "B":
        posts_attrs[data[0]] = data[2:]

# join (LEFT TABLE = post, RIGHT TABLE = user)
for user_id in posts_attrs:
    if user_id in users_attrs:
        id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = posts_attrs[user_id]
        reputation, gold, silver, bronze = users_attrs[user_id]
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id, title, tagnames,
                                                                                          user_id, node_type,
                                                                                          parent_id, abs_parent_id,
                                                                                          added_at, score, reputation,
                                                                                          gold, silver, bronze)
