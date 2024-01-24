from sys import stdin

lines = stdin.readlines()


def validation_data(data):
    for line in data:
        name, last_height, new_height = line.rstrip("\n").split()
        if not isinstance(name, str) or (
                not last_height.isdigit()) or (
                not new_height.isdigit()):
            raise TypeError
        if last_height > new_height:
            raise ValueError


def changes_height(data, total_changes=0):
    validation_data(data)
    for line in data:
        _, last_height, new_height = line.rstrip("\n").split()
        total_changes += (int(new_height) - int(last_height))
    print(round(total_changes / len(data)))


changes_height(lines)
