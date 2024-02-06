from sys import stdin

lines = stdin.readlines()


def comments_clean(data):
    for idx, line in enumerate(data):
        if '#' in line:
            data[idx] = line[:line.index('#')].rstrip()
    print('\n'.join(data).lstrip('\n'))


comments_clean(lines)  # commments

# Взять индекс решетки, срезать символы
# до решетки и очистить от пробелов с правой стороны.
