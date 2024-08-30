import random
import string
import pytest

import pangram


class TestDataPerfect:
    def test_uppercase(self):
        sentence = string.ascii_uppercase
        assert pangram.is_pangram(sentence) == True


    def test_lower_case(self):
        sentence = string.ascii_lowercase
        assert pangram.is_pangram(sentence) == True


    def test_letters(self):
        sentence = string.ascii_letters
        assert pangram.is_pangram(sentence) == True


    def test_with_underscores(self):
        assert pangram.is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == True


    def test_with_numbers(self):
        assert pangram.is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs") == True


    def test_mixed_case_and_punctuation(self):
        assert pangram.is_pangram('"Five quacking Zephyrs jolt my wax bed."') == True


# Generate test data for uppercase and lowercase strings
data_test_uppercase = [
    (' '.join(random.choices(string.ascii_uppercase, k=random.randint(1, 25))), False)
    for _ in range(100)
]

data_test_lowercase = [
    (' '.join(random.choices(string.ascii_lowercase, k=random.randint(1, 25))), False)
    for _ in range(100)
]


class TestDataNoPerfect:

    def test_empty(self):
        assert pangram.is_pangram('') == False


    @pytest.mark.parametrize("sentence, expected", data_test_uppercase)
    def test_uppercase(self, sentence, expected):
        actual_result = pangram.is_pangram(sentence)
        err_msg = (f'Called is_pangram({sentence}). '
                   f'The function returned {actual_result} as the value of the {sentence}, '
                   f'but the test expected {expected} as {sentence} value.')
        assert actual_result == expected, err_msg


    @pytest.mark.parametrize("sentence, expected", data_test_lowercase)
    def test_lower_case(self, sentence, expected):
        actual_result = pangram.is_pangram(sentence)
        err_msg = (f'Called is_pangram({sentence}). '
                   f'The function returned {actual_result} as the value of the {sentence}, '
                   f'but the test expected {expected} as {sentence} value.')
        assert actual_result == expected, err_msg



    def test_with_special_and_no_perfect(self):
        sentence = ('This script creates a% random string# composed!@!@!@!@!@ of upper#%$(%&)#$&'
                    '(#//\case and lowe=-0rcase letters, as well as digits. '
                    'You can change the length variable to generate a string of a different length.')
        assert pangram.is_pangram(sentence) == False


    def test_missing_a(self):
        sentence = 'qwertyUiopsDfghjklzxcvbnM'
        assert pangram.is_pangram(sentence) == False

    def test_with_number_and_no_perfect(self):
        sentence = 'qwertyUiopsDfghjklz1234567890xcvbnM'
        assert pangram.is_pangram(sentence) == False
