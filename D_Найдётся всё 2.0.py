from sys import stdin

lines = stdin.readlines()


def get_search(data):
    *headlines, search = data
    search = search.rstrip()

    for line in headlines:
        if search.lower() in line.lower():
            print(line.rstrip('\n'))


get_search(lines)
