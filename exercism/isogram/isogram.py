from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)


def is_isogram(string: str):
    str_convert = string.lower()
    lst = list(filter(lambda char: char in ALPHABET, set(str_convert)))
    for item in lst:
        if (str_convert).count(item) > 1:
            return False
    return True


if __name__ == '__main__':
    is_isogram('alphAbet')
