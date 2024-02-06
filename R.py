import math

read_file = input()

with open(read_file, "rb") as file_in:
    byte = file_in.read()
size = len(byte)

if size < 1024:
    result = f'{size}Б'
elif 1024 <= size < 1024 ** 2:
    result = f'{math.ceil(size/1024)}КБ'
elif 1024 ** 2 <= size < 1024 ** 3:
    result = f'{math.ceil(size/1024**2)}МБ'
elif size >= 1024 ** 3:
    result = f'{math.ceil(size/1024**3)}ГБ'

print(result)