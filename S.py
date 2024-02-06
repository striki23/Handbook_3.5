LENGTH_A_Z = 26
size_shift = int(input())
A_code = 65
Z_code = 90
alphabet = list(range(A_code, Z_code + 1))
print(alphabet)

with open('public.txt', mode='r', encoding="UTF-8") as file_in:
    lines = ''.join(file_in.readlines())
    encoded_lines = ''
    for char in lines:
        code = ord(char.upper())

        if A_code <= code <= Z_code:
            code = alphabet[(alphabet.index(code) + size_shift) % LENGTH_A_Z]

            if not char.isupper():
                new_char = chr(code).lower()
            else:
                new_char = chr(code)
        else:
            new_char = char

        encoded_lines += new_char

with open('private.txt', mode='w', encoding="UTF-8") as file_out:
    file_out.writelines(encoded_lines)
