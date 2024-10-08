from darts import (
    score,
)

def test_missed_target():
    assert score(-9, 9) == 0
def test_on_the_outer_circle():
    assert score(0, 10) == 1
def test_on_the_middle_circle():
    assert score(-5, 0) == 5
def test_on_the_inner_circle():
    assert score(0, -1) == 10
def test_exactly_on_center():
    assert score(0, 0) == 10
def test_near_the_center():
    assert score(-0.1, -0.1) == 10
def test_just_within_the_inner_circle():
    assert score(0.7, 0.7) == 10
def test_just_outside_the_inner_circle():
    assert score(0.8, -0.8) == 5
def test_just_within_the_middle_circle():
    assert score(-3.5, 3.5) == 5
def test_just_outside_the_middle_circle():
    assert score(-3.6, -3.6) == 1
def test_just_within_the_outer_circle():
    assert score(-7.0, 7.0) == 1
def test_just_outside_the_outer_circle():
    assert score(7.1, -7.1) == 0
def test_asymmetric_position_between_the_inner_and_middle_circles():
    assert score(0.5, -4) == 5
