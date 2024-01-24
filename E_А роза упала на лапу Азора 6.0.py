from sys import stdin

lines = stdin.readlines()


def get_palindrome(data, palindrome=[]):
    for line in data:
        for word in line.split():
            if word.lower() == word.lower()[::-1]:
                palindrome.append(word)
    print(*sorted(set(palindrome)), sep='\n')


get_palindrome(lines)
