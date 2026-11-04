"""Tests for celsius_to_fahrenheit and letter_grade (function-style tests)."""
import pytest
import sys

from qe_utils import celsius_to_fahrenheit, letter_grade


# ---- WORKED EXAMPLE ----
@pytest.mark.smoke
def test_freezing_point_converts_to_32f():
    assert celsius_to_fahrenheit(0) == 32


# ---- TODO tests ----

def test_boiling_point_converts_to_212f():
    # TODO (Task 3): 100 C -> 212 F. Marker: regression
    # Arrange
    celsius = 100
    # Act
    result = celsius_to_fahrenheit(celsius)
    # Assert
    assert result == 212


def test_body_temperature_uses_approx():
    # TODO (Task 4): 37 C is 98.6 F. Compare with pytest.approx, NOT ==. Marker: regression
    # Arrange
    celsius = 37
    # Act
    result = celsius_to_fahrenheit(celsius)
    # Assert
    assert result == pytest.approx(98.6)

    

def test_minus_40_is_same_in_both_scales():
    # TODO (Task 3): celsius_to_fahrenheit(-40) == -40. Marker: boundary
     # Arrange
    celsius = -40
    # Act
    result = celsius_to_fahrenheit(celsius)
    # Assert
    assert result == -40


def test_grade_90_is_a():
    # TODO (Task 3): boundary 90 -> "A". Markers: boundary, smoke
     # Arrange
    score = 90
    # Act
    result = letter_grade(score)
    # Assert
    assert result == "A"


def test_grade_89_is_b():
    # TODO (Task 3): just below 90 -> "B". Marker: boundary
    score = 89
    # Act
    result = letter_grade(score)
    # Assert
    assert result == "B"

    


def test_grade_0_is_f_and_100_is_a():
    # TODO (Task 3): the two extreme valid scores. Marker: boundary
    lowest_score = 0
    highest_score = 100
    # Act
    lowest_result = letter_grade(lowest_score)
    highest_result = letter_grade(highest_score)
    # Assert
    assert lowest_result == "F"
    assert highest_result == "A"

   


def test_grade_below_zero_raises_value_error():
    # TODO (Task 4): -1 -> ValueError (check message with match=). Marker: regression
     # Arrange
    score = -1
    # Act / Assert
    with pytest.raises(ValueError, match="score must be between 0 and 100"):
        letter_grade(score)




def test_grade_above_100_raises_value_error():
    # TODO (Task 4): 101 -> ValueError. Marker: regression
    score = 101
    # Act / Assert
    with pytest.raises(ValueError, match="score must be between 0 and 100"):
        letter_grade(score)

   


# TODO (Task 5): add ONE test that uses @pytest.mark.skipif on a condition, e.g.
#   @pytest.mark.skipif(sys.version_info < (3, 8), reason="needs Python 3.8+")
# (import sys at the top). Any simple, truthful test is fine. Name it test_..._skipif_example.

@pytest.mark.skipif(
    sys.version_info < (3, 9),
    reason="This lab requires Python 3.9+",
)
def test_grade_80_skipif_example():
    # Arrange
    score = 80
    # Act
    result = letter_grade(score)
    # Assert
    assert result == "B"
