from sys import stdin


def validation_data(data):
    for line in data:
        name, prev_height, new_height = line.rstrip("\n").split()
        if (
            not isinstance(name, str)
            or not prev_height.isdigit()
            or not new_height.isdigit()
        ):
            raise TypeError

        prev_height = int(prev_height)
        new_height = int(new_height)
        if prev_height > new_height:
            raise ValueError


def changes_height(data):
    validation_data(data)

    total_changes=0
    for line in data:
        _, last_height, new_height = line.rstrip("\n").split()
        total_changes += (int(new_height) - int(last_height))

    print(round(total_changes / len(data)))


if __name__ == '__main__':
    lines = stdin.readlines()
    changes_height(lines)
