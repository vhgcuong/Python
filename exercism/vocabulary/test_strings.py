import pytest
import strings


input_data = ['happy', 'manageable', 'fold', 'eaten', 'avoidable', 'usual']
result_data = [f'un{item}' for item in input_data]
data_test_prefix = list(zip(input_data, result_data))


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


input_data = ['heaviness', 'sadness', 'softness', 'crabbiness', 'lightness', 'artiness', 'edginess']
result_data = ['heavy', 'sad', 'soft', 'crabby', 'light', 'arty', 'edgy']
data_test_suffix_ness = list(zip(input_data, result_data))


@pytest.mark.parametrize("word, expected", data_test_suffix_ness)
def test_remove_suffix_ness(word, expected):
    actual_result = strings.remove_suffix_ness(word)
    err_msg = (f'Called remove_suffix_ness({word}). '
               f'The function returned {actual_result} as the value of the {word}, '
               f'but the test expected {expected} as {word} value.')
    assert actual_result == expected, err_msg


input_data = ['Look at the bright sky.',
              'His expression went dark.',
              'The bread got hard after sitting out.',
              'The butter got soft in the sun.',
              'Her eyes were light blue.',
              'The morning fog made everything damp with mist.',
              'He cut the fence pickets short by mistake.',
              'Charles made weak crying noises.',
              'The black oil got on the white dog.']
index_data = [-2, -1, 3, 3, -2, -3, 5, 2, 1]
result_data = ['brighten', 'darken', 'harden', 'soften',
               'lighten', 'dampen', 'shorten', 'weaken', 'blacken']
data_test_adjective_to_verb = list(zip(input_data, index_data, result_data))


@pytest.mark.parametrize("sentence, index, expected", data_test_adjective_to_verb)
def test_adjective_to_verb(sentence, index, expected):
    words = sentence.split(" ")
    word = words[index]

    actual_result = strings.adjective_to_verb(sentence, index)
    err_msg = (f'Called adjective_to_verb({sentence}, {index}). '
               f'The function returned {actual_result} as the value of the {word}, '
               f'but the test expected {expected} as {word} value.')
    assert actual_result == expected, err_msg
