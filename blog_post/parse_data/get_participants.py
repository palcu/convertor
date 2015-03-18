import csv
import operator
from collections import defaultdict
from pprint import pprint

participants = defaultdict(int)
time_spent = defaultdict(int)
last_submission = {}
has_solved_it = defaultdict(bool)
no_submissions = 0
submissions = []

with open('../submissions.csv') as stream:
    reader = csv.reader(stream)
    for row in reader:
        submissions.append(row)

submissions.sort(key=lambda x: x[4])

for submission in submissions:
    participants[submission[1]] += 1
    no_submissions += 1

    if submission[3] == '100':
        has_solved_it[submission[1]] = True

    if not last_submission.get(submission[1]):
        last_submission[submission[1]] = int(submission[4])
        time_spent[submission[1]] += 60*60 # one hour
    else:
        if int(submission[4]) - last_submission[submission[1]] > 60 * 60:
            time_spent[submission[1]] += 60*60
        else:
            time_spent[submission[1]] += int(submission[4]) - last_submission[submission[1]]
        last_submission[submission[1]] = int(submission[4])

print("Sunt {0} participanti cu {1} submisii, din care {2} au corect.".format(
        len(participants), no_submissions, len(has_solved_it)))

sorted_participants = sorted(participants.items(), key=operator.itemgetter(1), reverse=True)

print("Name,Submissions,Success,Hours Spent")
for participant in sorted_participants:
    time_spent[participant[0]] = time_spent[participant[0]] / 60 / 60
    print("{0},{1},{2},{3}".format(participant[0], participant[1],
                                   has_solved_it[participant[0]],
                                   time_spent[participant[0]]))

# Compute average number of submissions for solving correctly

sum_of_submissions = 0
for participant in sorted_participants:
    if has_solved_it[participant[0]]:
        sum_of_submissions += participant[1]
print("Average number of submissions: {0}".format(sum_of_submissions / len(has_solved_it)))

sum_of_hours = 0
sum_of_hours_for_success = 0
for participant in sorted_participants:
    sum_of_hours += time_spent[participant[0]]
    if has_solved_it[participant[0]]:
        sum_of_hours_for_success += time_spent[participant[0]]

print("Total number of hours: {0}".format(sum_of_hours))
print("Total number of hours if he succeeded: {0}".format(sum_of_hours_for_success))
print("Average number of hours: {0}".format(sum_of_hours/len(participants)))
print("Average number of hours if he succeeded: {0}".format(sum_of_hours_for_success/len(has_solved_it)))
