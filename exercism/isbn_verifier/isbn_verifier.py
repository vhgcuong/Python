def is_valid(isbn: str):
    # format isbn
    text = isbn.replace('-', '').strip(' ')

    # valid
    if len(text) != 10:
        return False

    if text[-1] != 'X' and not text[-1].isdigit():
        return False

    if any(c.isalpha() for c in text[:-1]):
        return False
    
    # check
    convert_text = list(text)
    if text.endswith('X'):
        convert_text[-1] = '10'
    convert_text = list(map(int, convert_text))

    
    lst = list(zip(convert_text, [i for i in range(10, 0, -1)]))
    total = 0
    for (key, value) in lst:
        total += key * value

    return total % 11 == 0

if __name__ == '__main__':
    is_valid("3-598-21515-X")
