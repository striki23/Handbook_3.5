from sys import stdin

user_input = stdin.readlines()
user_input = [line.rstrip() for line in user_input]
*r_files, outfile = user_input


def read_file(files: list[str, str], data={}) -> dict[str, list]:
    for file in files:
        with open(file, encoding="UTF-8") as file_in:
            lines = file_in.readlines()
            for line in lines:
                line = line.rstrip('\n').split()
                data[file] = data.get(file, []) + line
    return data


def file_differ(file_data: dict[str, list]) -> list[str, str]:
    differ = set()
    for data in file_data.values():
        differ = differ.symmetric_difference(set(data))
    return sorted(list(differ))


def write_file(file: str, data: list[str, str]) -> None:
    lines = [word + '\n' for word in data]
    with open(file, "w", encoding="UTF-8") as file_out:
        file_out.writelines(lines)


res = read_file(r_files)
difference = file_differ(res)
write_file(outfile, difference)
