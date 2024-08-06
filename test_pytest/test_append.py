# # contents of test_append.py
# import pytest
#
#
# # Arrange
# @pytest.fixture
# def first_entry():
#     return "a"
#
#
# # Arrange
# @pytest.fixture
# def second_entry():
#     return 2
#
#
# # Arrange
# @pytest.fixture
# def order(first_entry, second_entry):
#     return [first_entry, second_entry]
#
#
# # Arrange
# @pytest.fixture
# def expected_list():
#     return ["a", 2, 3.0]
#
#
# def test_string(order, expected_list):
#     # Act
#     order.append(3.0)
#
#     # Assert
#     assert order == expected_list


import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]
