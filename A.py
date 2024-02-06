from sys import stdin

lines = stdin.readlines()
total = 0
for line in lines:
    for num in line.rstrip("\n").split():
        total += int(num)

print(total)
