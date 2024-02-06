from sys import stdin

search_line = input()
files = [line.rstrip('\n') for line in stdin.readlines()]
found = 0

for file in files:
    with open(file, encoding="UTF-8") as file_in:
        lines = ''.join(file_in.readlines())
        while '&nbsp' in lines or '  ' in lines or '\n' in lines:
            lines = lines.replace('&nbsp', '').replace('  ', ' ').replace('\n', ' ')
        if search_line.strip().lower() in lines.lower():
            found += 1
            print(file)

if not found:
    print('404. Not Found')
