import json
from sys import stdin

file_name = input()
data = stdin.readlines()

data_dict = {}
for line in data:
    key, value = line.strip('\n').split(' == ')
    data_dict[key] = value

with open(file_name, encoding="UTF-8") as file_in:
    records = json.load(file_in)
    records.update(data_dict)
with open(file_name, "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)
