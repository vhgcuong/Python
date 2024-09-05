# import re


def is_isogram(phrase):
    scrubbed = phrase.replace('-', '').replace(' ', '').lower()
    # scrubbed = [ltr.lower() for ltr in phrase if ltr.isalpha()]
    # scrubbed = "".join(re.findall("[a-zA-Z]", phrase)).lower()

    return len(scrubbed) == len(set(scrubbed))


if __name__ == '__main__':
    is_isogram('alphAbet')
