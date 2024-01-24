from sys import stdin

lines = stdin.readlines()


def comments_clean(data):
    is_comments = False
    clean_text = []
    for line in data:
        new_line = ''
        for letter in line:
            if letter == '#':  # коммент
                is_comments = True
            elif not is_comments or letter == '\n':
                new_line += letter
            if letter == '\n':
                is_comments = False
        new_line = (''.join(new_line)).rstrip()
        if new_line:
            clean_text.append(new_line)
    print('\n'.join(clean_text).lstrip('\n'))


comments_clean(lines)  # commments

# Взять индекс решетки, срезать символы
# до решетки и очистить от пробелов с правой стороны.
