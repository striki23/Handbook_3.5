from sys import stdin
import json

user_scores = stdin.readlines()
user_scores = [line.rstrip('\n') for line in user_scores]

with open('scoring.json', encoding="UTF-8") as file_in:
    records = json.load(file_in)

total = 0
idx = 0
for test in records:
    for t in test['tests']:
        if t['pattern'] == user_scores[idx]:
            total += test['points'] / len(test['tests'])
        idx += 1

print(round(total))
