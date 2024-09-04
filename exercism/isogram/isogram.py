from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)


def is_isogram(string: str):
    lst = list(filter(lambda char: char in ALPHABET, set(string.lower())))
    for item in lst:
        if (string.lower()).count(item) > 1:
            return False
    return True


if __name__ == '__main__':
    is_isogram('alphAbet')
