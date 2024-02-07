with open('secret.txt', encoding="UTF-8") as file_in:
    code_of_chars = [ord(char) for char in ''.join(file_in.readlines())]
    decrypt = ''
    for code in code_of_chars:
        if code > 128:
            code = code % 256
        decrypt += chr(code)
    print(decrypt)

# 0.0.0.0
# 255.255.255.255
#
# 32x - 01011010 01011010 01011010 01011010
# 64x - 01011010 01011010 01011010 01011010 01011010 01011010 01011010 01011010
