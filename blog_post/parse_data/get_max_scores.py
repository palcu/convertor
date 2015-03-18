import csv
import operator
from collections import defaultdict
from pprint import pprint

participants = defaultdict(int)

with open('../submissions.csv') as stream:
    reader = csv.reader(stream)
    for row in reader:
        participants[row[1]] = max(participants[row[1]], int(row[3]))

scores = defaultdict(int)
for participant in participants:
    scores[participants[participant]] += 1

print("score,participants")
for i in range(0, 110, 10):
    print("{0},{1}".format(i, scores.get(i, 0)))
