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



test_data = [('A', 'A', ('A', 'A')),
             ('10', 'J', ('10', 'J')),
             ('3', 'A', '3'),
             ('3', '6', '6'),
             ('Q', '10', ('Q', '10')),
             ('4', '4', ('4', '4')),
             ('9',  '10', '10'),
             ('6', '9', '9'),
             ('4', '8', '8')]

