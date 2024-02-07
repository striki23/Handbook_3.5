reading_file = input()
n = int(input())

with open(reading_file, mode="r", encoding="UTF-8") as file_in:
    lines = file_in.readlines()

    length = len(lines)
    idx = length - n
    while idx < length:
        print(lines[idx].strip('\n'))
        idx += 1
