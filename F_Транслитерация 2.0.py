with open("cyrillic.txt", mode="r", encoding="UTF-8") as file_in:
    lines = file_in.readlines()


def transliterate(data):
    tabl_trans = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'Й': 'I',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'Kh',
        'Ц': 'Tc',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ы': 'Y',
        'Э': 'E',
        'Ю': 'Iu',
        'Я': 'Ia',
        'Ъ': '',
        'Ь': ''
    }
    trans_data = ''
    for line in data:
        for char in line:
            if char.islower():
                trans_data += tabl_trans.get(char.upper(), char).lower()
            else:
                trans_data += tabl_trans.get(char, char)
    return trans_data


with open("transliteration.txt", mode="w", encoding="UTF-8") as file_out:
    file_out.writelines(transliterate(lines))
