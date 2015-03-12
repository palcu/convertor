from faker import Factory
import json
import random

faker = Factory.create()

NO_KEYS = 1000
NO_ENTRIES = 10
NO_ENTRIES_NUMBER = NO_KEYS / 3

keys = [faker.sentence() for _ in range(NO_KEYS)]
keys_with_ints = {random.randint(0, NO_KEYS-1)
                  for x in range(NO_ENTRIES_NUMBER)}

l = []
for _ in range(NO_ENTRIES):
    d = {}
    for i, key in enumerate(keys):
        if i in keys_with_ints:
            d[key] = random.randint(0, 1000000)
        else:
            d[key] = faker.sentence()
    l.append(d)


def add_random_whitespace(s):
    s2 = ""
    state = 0
    for c in s:
        s2 += c
        if c == '"':
            state += 1
        if c == ',':
            state = 0
        if ord('0') <= ord(c) and ord(c) <= ord('9'):
            state = 1
        if state % 4 == 0 or state % 4 == 2:
            if random.choice([True, False]):
                s2 += random.randint(0, 10) * " "
            if random.choice([True] + [False]*20):
                s2 += "\n"
    return s2

print add_random_whitespace(json.dumps(l, sort_keys=True, indent=1))
