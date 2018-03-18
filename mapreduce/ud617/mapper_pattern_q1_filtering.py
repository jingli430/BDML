#!/usr/bin/python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        '''
        The objective is to count the number of forum nodes where 'body' either
        contains none of the three punctuation marks: period ('.'), exclamation point ('!'),
        question mark ('?'), or else 'body' contains exactly one such punctuation mark as the
        last character
        '''
        body = line[4]
        first_condition = body and '!' not in body and '?' not in body and '.' not in body
        second_condition = body and body[-1] in '?!.' and ('!' not in body[:-1] and '?' not in body[:-1] and '.' not in body[:-1])
        if first_condition or second_condition:
            writer.writerow(line)


test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Also one sentence!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
"""

mapper()

# This function allows you to test the mapper with the provided test string
# But you should comment out if you use another dataset as input
# def main():
#     import StringIO
#     sys.stdin = StringIO.StringIO(test_text)
#     mapper()
#     sys.stdin = sys.__stdin__
#
#
# if __name__ == "__main__":
#     main()