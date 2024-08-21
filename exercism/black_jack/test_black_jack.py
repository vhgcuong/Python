import black_jack
import pytest


card_value_test_data = [('2', 2), ('5', 5), ('8', 8),
             ('A', 1), ('10', 10), ('J', 10),
             ('Q', 10), ('K', 10)]

@pytest.mark.parametrize("card, expected", card_value_test_data)
def test_convert_card_value(card, expected):
    actual_result = black_jack.value_of_card(card)
    error_msg = (f'Called value_of_card({card}). '
                 f'The function returned {actual_result} as the value of the {card} card, '
                 f'but the test expected {expected} as the {card} card value.')
    assert actual_result == expected, error_msg



higher_card_test_data = [('A', 'A', ('A', 'A')),
             ('10', 'J', ('10', 'J')),
             ('3', 'A', '3'),
             ('3', '6', '6'),
             ('Q', '10', ('Q', '10')),
             ('4', '4', ('4', '4')),
             ('9',  '10', '10'),
             ('6', '9', '9'),
             ('4', '8', '8')]

@pytest.mark.parametrize("card_one, card_two, expected", higher_card_test_data)
def test_higher_card(card_one, card_two, expected):
    actual_result = black_jack.higher_card(card_one, card_two)
    error_msg = (f'Called higher_card({card_one}, {card_two}). '
                 f'The function returned {actual_result}, '
                 f'but the test expected {expected} as the result for the cards {card_one, card_two}.')
    assert actual_result == expected, error_msg


value_of_ace_test_data = [('2', '3', 11), ('3', '6', 11), ('5', '2', 11),
             ('8', '2', 11), ('5', '5', 11), ('Q', 'A', 1),
             ('10', '2', 1), ('7', '8', 1), ('J', '9', 1),
             ('K', 'K', 1), ('2', 'A', 1), ('A', '2', 1)]

@pytest.mark.parametrize("card_one, card_two, expected", value_of_ace_test_data)
def test_value_of_ace(card_one, card_two, expected):
    actual_result = black_jack.value_of_ace(card_one, card_two)
    error_msg = (f'Called value_of_ace({card_one}, {card_two}). '
                 f'The function returned {actual_result}, '
                 f'but the test expected {expected} as the value of an ace card '
                 f'when the hand includes {card_one, card_two}.')
    assert actual_result == expected, error_msg


black_jack_test_data = [(('A', 'K'), True), (('10', 'A'), True),
             (('10', '9'), False), (('A', 'A'), False),
             (('4', '7'), False), (('9', '2'), False),
             (('Q', 'K'), False)]

@pytest.mark.parametrize("hand, expected", black_jack_test_data)
def test_is_black_jack(hand, expected):
    card_one, card_two = hand
    actual_result = black_jack.is_blackjack(card_one, card_two)
    error_msg = (f'Called is_blackjack({hand[0]}, {hand[1]}). '
                 f'The function returned {actual_result}, '
                 f'but hand {hand} {"is" if expected else "is not"} a blackjack.')
    assert actual_result == expected, error_msg


split_pairs_test_data = [(('Q', 'K'), True), (('6', '6'), True),
             (('A', 'A'), True),(('10', 'A'), False),
             (('10', '9'), False)]

@pytest.mark.parametrize("hand, expected", split_pairs_test_data)
def test_can_split_pairs(hand, expected):
    card_one, card_two = hand
    actual_result = black_jack.can_split_pairs(card_one, card_two)
    error_msg = (f'Called can_split_pairs({hand[0]}, {hand[1]}). '
                     f'The function returned {actual_result}, '
                     f'but hand {hand} {"can" if expected else "cannot"} be split into pairs.')
    assert actual_result == expected, error_msg


double_down_test_data = [(('A', '9'), True), (('K', 'A'), True),
             (('4', '5'), True),(('A', 'A'), False),
             (('10', '2'), False), (('10', '9'), False)]

@pytest.mark.parametrize("hand, expected", double_down_test_data)
def test_can_double_down(hand, expected):
    card_one, card_two = hand
    actual_result = black_jack.can_double_down(card_one, card_two)
    error_msg = (f'Called can_double_down({hand[0]}, {hand[1]}). '
                 f'The function returned {actual_result}, '
                 f'but hand {hand} {"can" if expected else "cannot"} be doubled down.')
    assert actual_result == expected, error_msg
