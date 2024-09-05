def is_isogram(phrase):
    scrubbed = phrase.replace('-', '').replace(' ', '').lower()
    return len(scrubbed) == len(set(scrubbed))


if __name__ == '__main__':
    is_isogram('alphAbet')
