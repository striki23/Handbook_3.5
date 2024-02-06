from sys import stdin


def get_palindrome(data):
    palindrome = []
    for line in data:
        for word in line.split():
            if word.lower() == word.lower()[::-1]:
                palindrome.append(word)
    print(*sorted(set(palindrome)), sep='\n')


if __name__ == '__main__':
    lines = stdin.readlines()
    get_palindrome(lines)
