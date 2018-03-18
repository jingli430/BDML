#!/usr/bin/python
import sys
import csv

'''
mapper input: line
mapper output: <key=word, value=nodeId>
reducer input: <key=word, value=nodeId>
reducer output: <key=word, value=(total_count, List_of_comma_separated_nodes_in_ascending_order)>
'''


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        '''
        Write a MapReduce program that creates an index of all words that can be find in the body of a forum post and 
        node id they can be found in. Do not parse the HTML. Just split the test on all whitespace as well as the
        following characters:.,!?:;"()<>[]#$=-/
        Make sure to create a case-insensitive index (e.g. "FANTASTIC" and "fantastic" should both count towards the same word).
        '''
        body = line[4].strip().replace('.', ' ') \
            .replace(',', ' ').replace('!', ' ') \
            .replace('?', ' ').replace(':', ' ') \
            .replace(';', ' ').replace('"', ' ') \
            .replace('(', ' ').replace(')', ' ') \
            .replace('(', ' ').replace(')', ' ') \
            .replace('<', ' ').replace('>', ' ') \
            .replace('[', ' ').replace(']', ' ') \
            .replace('#', ' ').replace('$', ' ') \
            .replace('=', ' ').replace('-', ' ') \
            .replace('/', ' ').replace('\n', ' ')
        # split words using space as delimiter after removing the heading and trailing space again
        # DO NOT use split(' '), it will take EXACTLY one space as delimeter. It will treat double spaces wrong
        # Ex. aaa = 'Hey  Two sentences'
        # aaa.split(' ') will be equal to ['Hey', '', 'Two', 'sentences'] (wrong!)
        # aaa.split() will be equal to ['Hey', 'Two', 'sentences'] (correct!)
        words = body.lower().strip().split()
        for word in words:
            if word == "fantastically":
                # print("{0}\t{1}".format(word, line[0]))
                writer.writerow((word, line[0]))


test_text = """\"1\"\t\"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"2\"\t\"\"\t\"\"\t\"\"\t\"Also one sentence!\"\t\"\"
\"3\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
\"4\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
\"5\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
\"6\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
"""


# This function allows you to test the mapper with the provided test string
# But you should comment out if you use another dataset as input
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__


if __name__ == "__main__":
    main()
