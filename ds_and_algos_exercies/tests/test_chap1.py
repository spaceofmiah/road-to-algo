from unittest import TestCase
from ds_and_algos_exercies import chap1



def test_is_multiple_returns_true_given_an_appropriate_factor():
    """Confirms that the is_multiple function returns True
    when given an appropriate factor
    """
    assert chap1.is_multiple(7, 21) is True
    assert chap1.is_multiple(3, 21) is True

def test_is_multiple_returns_false_given_an_invalid_factor():
    """Confirms that the is_multiple function return False
    when given an invalid factor
    """
    assert chap1.is_multiple(10, 21) is False
    assert chap1.is_multiple(13, 21) is False

def test_is_even_returns_true_when_passed_an_even_number():
    """Ensure that is_even would return True when passed
    an even number
    """
    assert chap1.is_even(2) is True

def test_is_even_returns_false_when_passed_an_odd_number():
    """Ensure that is_even would return False when passed
    an odd number
    """
    assert chap1.is_even(1) is False

def test_minmax_returns_minimum_and_maximum_value_in_a_sorted_list():
    """Ensures minmax returns the minimum and maximum list
    element from a sorted list
    """
    assert chap1.minmax([1, 2, 3]) == (1, 3)

def test_minmax_returns_minimum_and_maximum_value_in_an_unsorted_list():
    """Ensures minmax returns the minimum and maximum list
    element from an unsorted list
    """
    assert chap1.minmax([3, 1, 4, 2]) == (1, 4)

def test_minmax_returns_minimum_and_maximum_value_in_a_sorted_negative_integer_list():
    """Ensures minmax returns the minimum and maximum list
    element from a sorted negative integer list
    """
    assert chap1.minmax([-3, -2, -1, 0]) == (-3, 0)

def test_minmax_returns_minimum_and_maximum_value_in_an_unsorted_negative_integer_list():
    """Ensures minmax returns the minimum and maximum list
    element from a sorted negative integer list
    """
    assert chap1.minmax([ -1, -2, 0, -3 ]) == (-3, 0)

def test_minmax_returns_the_first_element_as_the_minimum_and_maximum_for_a_single_list():
    """Ensure minmax retuns the first element as the minimum
    and maximum in the list
    """
    assert chap1.minmax([-3]) == (-3, -3)
    assert chap1.minmax([3]) == (3, 3)

def test_square_sum_computes_appropriately():
    """Ensures square sum computation is valid"""
    assert chap1.square_sum(3) == 5
    assert chap1.square_sum(4) == 14
    
    




