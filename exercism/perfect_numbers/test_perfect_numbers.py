from perfect_numbers import classify
import pytest

PERFECT = "perfect"
DEFICIENT = "deficient"
ABUNDANT = "abundant"


def error():
    raise ValueError("Classification is only possible for positive integers.")


class TestInvalidInputs:
    def test_zero_is_rejected_as_it_is_not_a_positive_integer(self):
        with pytest.raises(ValueError, match=r'Classification is only possible for positive integers.') as excinfo:
            classify(0)
        assert excinfo.type is ValueError
        assert "Classification is only possible for positive integers." in str(excinfo.value)

    def test_negative_integer_is_rejected_as_it_is_not_a_positive_integer(self):
        with pytest.raises(ValueError, match=r'Classification is only possible for positive integers.') as excinfo:
            classify(-1)
        assert excinfo.type is ValueError
        assert "Classification is only possible for positive integers." in str(excinfo.value)


class TestPerfectNumbers:
    def test_smallest_perfect_number(self):
        assert classify(6) == PERFECT

    def test_medium_perfect_number(self):
        assert classify(28) == PERFECT

    def test_large_perfect_number(self):
        assert classify(33550336) == PERFECT


class TestDeficientNumbers:
    def test_smallest_deficient_number(self):
        assert classify(8) == DEFICIENT

    def test_medium_deficient_number_is_classified_correctly(self):
        assert classify(32) == DEFICIENT

    def test_large_deficient_number_is_classified_correctly(self):
        assert classify(33550337) == DEFICIENT

    def test_edge_case_no_factors_other_than_itself_is_classified_correctly(self):
        assert classify(1) == DEFICIENT


class AbundantNumbersTest:
    def test_smallest_abundant_number(self):
        assert classify(12) == ABUNDANT

    def test_medium_abundant_number(self):
        assert classify(30) == ABUNDANT

    def test_large_abundant_number(self):
        assert classify(33550335) == ABUNDANT
