unformatted_file = input()
formatted_file = input()

with open(unformatted_file, encoding="UTF-8") as file_in:
    lines = file_in.readlines()

new_text = []
for line in lines:
    line = line.strip().replace('\t', '').replace('  ', ' ')
    while '  ' in line:
        line = line.replace('  ', ' ')
    if line:
        new_text.append(line + '\n')

with open(formatted_file, "w", encoding="UTF-8") as file_out:
    file_out.writelines(new_text)
