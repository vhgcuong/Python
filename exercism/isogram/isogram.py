from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)


def is_isogram(string: str):
    dic = {}

    for item in string.lower():
        if item in dic.keys():
            dic[item] += 1
        else:
            dic[item] = 1

    for (key, value) in dic.items():
        if key in [' ', '-', '_']:
            continue
        if str(key).lower() not in ALPHABET:
            return False
        if value != 1:
            return False
    return True


if __name__ == '__main__':
    is_isogram('alphAbet')
