import pytest
import strings


data_test_prefix = [
    ("happy", "unhappy"), ("clear", "unclear"), ("fair", "unfair"), ("certain", "uncertain"),
    ("likely", "unlikely"), ("seen", "unseen"), ("usual", "unusual"), ("necessary", "unnecessary"),
    ("finished", "unfinished"), ("aware", "unaware")
]


@pytest.mark.parametrize("word, expected", data_test_prefix)
def test_add_prefix_un(word, expected):
    actual_result = strings.add_prefix_un(word)
    err_msg = (f'Called add_prefix_un({word}). '
               f'The function returned {actual_result} as the value of the {word}, '
               f'but the test expected {expected} as {word} value.')
    assert actual_result == expected, err_msg


data_test_word_groups = [
    (['en', 'close', 'joy', 'lighten'], 'en :: enclose :: enjoy :: enlighten'),
    (['pre', 'serve', 'dispose', 'position'], 'pre :: preserve :: predispose :: preposition'),
    (['auto', 'didactic', 'graph', 'mate'], 'auto :: autodidactic :: autograph :: automate'),
    (['inter', 'twine', 'connected', 'dependent'], 'inter :: intertwine :: interconnected :: interdependent')
]


@pytest.mark.parametrize("word, expected", data_test_word_groups)
def test_make_word_groups(word, expected):
    actual_result = strings.make_word_groups(word)
    err_msg = (f'Called make_word_groups({word}). '
               f'The function returned {actual_result} as the value of the {word}, '
               f'but the test expected {expected} as {word} value.')
    assert actual_result == expected, err_msg


data_test_suffix_ness = [
    ("Happiness", "Happy"),
    ("Kindness", "Kind"),
    ("Darkness", "Dark"),
    ("Weakness", "Weak"),
    ("Sadness", "Sad"),
    ("Cleanliness", "Cleanly"),
    ("Illness", "Ill"),
    ("Quietness", "Quiet"),
    ("Fairness", "Fair"),
    ("Laziness", "Lazy"),
    ("Test", "Test")
]


@pytest.mark.parametrize("word, expected", data_test_suffix_ness)
def test_remove_suffix_ness(word, expected):
    actual_result = strings.remove_suffix_ness(word)
    err_msg = (f'Called remove_suffix_ness({word}). '
               f'The function returned {actual_result} as the value of the {word}, '
               f'but the test expected {expected} as {word} value.')
    assert actual_result == expected, err_msg


data_test_adjective_to_verb = [
    (('I need to make that bright.', -1), 'brighten'),
    (('It got dark as the sun set.', 2), 'darken')
]


@pytest.mark.parametrize("data, expected", data_test_adjective_to_verb)
def test_adjective_to_verb(data, expected):
    sentence, index  = data
    words = sentence.split(" ")
    word = words[index]

    actual_result = strings.adjective_to_verb(sentence, index)
    err_msg = (f'Called adjective_to_verb({sentence}, {index}). '
               f'The function returned {actual_result} as the value of the {word}, '
               f'but the test expected {expected} as {word} value.')
    assert actual_result == expected, err_msg
