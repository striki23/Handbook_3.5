import json

with open(input(), encoding="UTF-8") as file_in:
    lines = file_in.readlines()
    numbers = []
    for line in lines:
        line = line.rstrip('\n').split()
        numbers.extend(map(int, line))

results = {
    'count': len(numbers),
    'positive_count': len(list(filter(lambda x: x > 0, numbers))),
    'min': min(numbers),
    'max': max(numbers),
    'sum': sum(numbers),
    'average': round(sum(numbers) / len(numbers), 2),
}

with open(input(), "w", encoding="UTF-8") as file_out:
    json.dump(results, file_out, ensure_ascii=False, indent=2)
