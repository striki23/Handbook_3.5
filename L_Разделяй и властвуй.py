r_file = input()
even_file = input()
odd_file = input()
eq_file = input()


def read_file(file):
    with open(file, encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        nums = []
        for line in lines:
            line = line.rstrip('\n').split()
            nums.append(list(map(int, line)))
        return nums


def is_even(num):
    even = odd = 0

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd


def write_file(file, data):
    with open(file, "w", encoding="UTF-8") as file_out:
        file_out.writelines(data)


numbers = read_file(r_file)
even_lst = []
odd_lst = []
eq_lst = []
for n_line in numbers:
    even_str = odd_str = eq_str = ''
    for n in n_line:
        even_n, odd_n = is_even(n)
        if even_n > odd_n:
            even_str += ' ' + str(n)
        elif even_n < odd_n:
            odd_str += ' ' + str(n)
        elif even_n == odd_n:
            eq_str += ' ' + str(n)
    even_str = even_str.strip() + '\n'
    odd_str = odd_str.strip() + '\n'
    eq_str = eq_str.strip() + '\n'
    even_lst.append(even_str)
    odd_lst.append(odd_str)
    eq_lst.append(eq_str)

write_file(even_file, even_lst)
write_file(odd_file, odd_lst)
write_file(eq_file, eq_lst)
