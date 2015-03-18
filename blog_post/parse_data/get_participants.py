import csv
import operator
from collections import defaultdict
from pprint import pprint

participants = defaultdict(int)
has_solved_it = defaultdict(bool)
no_submissions = 0

with open('../submissions.csv') as stream:
    reader = csv.reader(stream)
    for row in reader:
        participants[row[1]] += 1
        no_submissions += 1

        if row[3] == '100':
            has_solved_it[row[1]] = True

print("Sunt {0} participanti cu {1} submisii, din care {2} au corect.".format(
        len(participants), no_submissions, len(has_solved_it)))

sorted_participants = sorted(participants.items(), key=operator.itemgetter(1), reverse=True)

for participant in sorted_participants:
    print("{0} - {1} - {2}".format(participant[0], participant[1],
                                   has_solved_it[participant[0]]))

# Compute average number of submissions for solving correctly

sum_of_submissions = 0
for participant in sorted_participants:
    if has_solved_it[participant[0]]:
        sum_of_submissions += participant[1]
print("Average number of submissions: {0}".format(sum_of_submissions / len(has_solved_it)))
