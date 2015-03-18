import csv
import operator
import os
from collections import defaultdict


tests = defaultdict(int)


def count_submission(stream):
    reader = csv.reader(stream)
    for row in reader:
        if row[4] != '10':
            tests[int(row[0])] += 1



for root, dirs, files in os.walk('../submissions'):
    for filename in files:
        with open('../submissions/{0}'.format(filename)) as stream:
            count_submission(stream)

print("test_id,fail")
sorted_tests = sorted(tests.items(), key=operator.itemgetter(0))
for test in sorted_tests:
    print("{0},{1}".format(*test))
