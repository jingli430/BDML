#!/usr/bin/python
# coding=utf-8
import sys

oldKey = None
# 这里也可以用list，反正是每个key处理完后就清空，不一定要用dict
users_attrs = {}
posts_attrs = {}

for line in sys.stdin:
    data = line.strip().replace('"','').split("\t")
    if len(data) < 6:
        continue
    # 不管数据来自psot还是user，我第一步只关心key有没有变化
    thisKey = data[0]

    if oldKey and oldKey != thisKey:
        # 如果变化，就开始对oldKey实施join操作
        # join (LEFT TABLE = post, RIGHT TABLE = user)
        for user_id in posts_attrs:
            if user_id in users_attrs:
                # 同一个user_id有可能有多个post records
                reputation, gold, silver, bronze = users_attrs[user_id]
                for record in posts_attrs[user_id]:
                    id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = record
                    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id, title, tagnames,
                                                                                                  user_id, node_type,
                                                                                                  parent_id,
                                                                                                  abs_parent_id,
                                                                                                  added_at, score,
                                                                                                  reputation,
                                                                                                  gold, silver, bronze)
        # reset
        users_attrs = {}
        posts_attrs = {}

    # 开始处理每条record【不管是来自user还是post】
    oldKey = thisKey
    # per oldKey, user record只有一个
    if data[1] == "A":
        users_attrs[oldKey] = data[2:]
    # per oldKey, post records可能不只一个，value用list来装所有的records
    if data[1] == "B":
        if oldKey in posts_attrs:
            posts_attrs[oldKey].append(data[2:])
        else:
            posts_attrs[oldKey] = [data[2:]]

# 不要忘记最后一个Key
if oldKey:
    for user_id in posts_attrs:
        if user_id in users_attrs:
            # 同一个user_id有可能有多个post records
            reputation, gold, silver, bronze = users_attrs[user_id]
            for record in posts_attrs[user_id]:
                id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = record
                print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id, title, tagnames,
                                                                                                  user_id, node_type,
                                                                                                  parent_id,
                                                                                                  abs_parent_id,
                                                                                                  added_at, score,
                                                                                                  reputation,
                                                                                                  gold, silver, bronze)