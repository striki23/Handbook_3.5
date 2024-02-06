with open('secret.txt', encoding="UTF-8") as file_in:
    lines = [ord(char) for char in ''.join(file_in.readlines())]
    result = ''
    for ord_char in lines:
        if ord_char > 128:
            ord_char = ord_char % 256
        result += chr(ord_char)
    print(result)
