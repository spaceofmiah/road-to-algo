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

def test_sum_squares_computes_appropriately():
    """Ensures sum squares computation is valid"""
    assert chap1.sum_squares(3) == 5
    assert chap1.sum_squares(4) == 14

def test_sum_odd_squares_computes_appropriately():
    """Ensure sum odd squares computation is valid"""
    assert chap1.sum_odd_squares(2) == 1
    assert chap1.sum_odd_squares(3) == 1
    assert chap1.sum_odd_squares(4) == 10
    assert chap1.sum_odd_squares(5) == 10
    assert chap1.sum_odd_squares(6) == 35
    
def test_data_reverses_accurately_using_custom_reverse():
    """Ensure data are reversed accurately"""
    assert chap1.custom_reverse([1, 2, 3]) == list(reversed([1, 2, 3]))
    # test double reverse
    assert chap1.custom_reverse(
        chap1.custom_reverse([1, 2, 3])
    ) == list(reversed(
            list(reversed([1, 2, 3]))
        )
    )

def test_odd_product_pair_returns_True_when_sequence_contains_pair_whose_product_result_is_odd():
    """Ensure that odd_product_pair returns True when 
    the product of any element pair results to an odd
    value
    """
    assert chap1.odd_product_pair([1, 3]) is True
    assert chap1.odd_product_pair([2, 3, 5]) is True
    assert chap1.odd_product_pair([1, 12, 11, 6]) is True

def test_odd_product_pair_returns_False_when_sequence_doesnt_contains_pair_whose_product_result_is_odd():
    """Ensure that odd_product_pair returns False when 
    the product of any element pair doesn't results to 
    an odd value
    """
    assert chap1.odd_product_pair([1, 2, 4]) is False
    assert chap1.odd_product_pair([2, 3, 4]) is False
    assert chap1.odd_product_pair([1, 12, 4, 6]) is False

def test_all_are_different_when_passed_a_list_with_different_distinct_values_returns_true():
    """Ensures that all_are_different returns True when 
    passed a list of distinct values
    """
    assert chap1.are_all_different([1, 2, 4]) is True
    assert chap1.are_all_different([1, 2, 4, 8, 10, 15, 22, 30]) is True

def test_all_are_different_when_passed_a_list_with_repeating_values_returns_false():
    """Ensures that all_are_different returns False when 
    passed a list of repeating values
    """
    assert chap1.are_all_different([1, 2, 4, 2]) is False
    assert chap1.are_all_different([10, 2, 4, 8, 10, 15, 22, 30]) is False

def test_all_alphabet_are_completely_generated():
    """Ensure that all alphabet are generated on call to 
    generate_the_alphabet
    """
    assert 'a' in chap1.generate_the_alphabet()
    assert 'b' in chap1.generate_the_alphabet()
    assert 'c' in chap1.generate_the_alphabet()
    assert 'd' in chap1.generate_the_alphabet()
    assert 'e' in chap1.generate_the_alphabet()
    assert 'f' in chap1.generate_the_alphabet()
    assert 'g' in chap1.generate_the_alphabet()
    assert 'h' in chap1.generate_the_alphabet()
    assert 'i' in chap1.generate_the_alphabet()
    assert 'j' in chap1.generate_the_alphabet()
    assert 'k' in chap1.generate_the_alphabet()
    assert 'l' in chap1.generate_the_alphabet()
    assert 'm' in chap1.generate_the_alphabet()
    assert 'n' in chap1.generate_the_alphabet()
    assert 'o' in chap1.generate_the_alphabet()
    assert 'p' in chap1.generate_the_alphabet()
    assert 'q' in chap1.generate_the_alphabet()
    assert 'r' in chap1.generate_the_alphabet()
    assert 's' in chap1.generate_the_alphabet()
    assert 't' in chap1.generate_the_alphabet()
    assert 'u' in chap1.generate_the_alphabet()
    assert 'v' in chap1.generate_the_alphabet()
    assert 'w' in chap1.generate_the_alphabet()
    assert 'x' in chap1.generate_the_alphabet()
    assert 'y' in chap1.generate_the_alphabet()
    assert 'z' in chap1.generate_the_alphabet()

def test_generated_alphabet_are_well_positioned():
    """Ensure that generated alphabet are position
    appropriately
    """
    assert 'a' == chap1.generate_the_alphabet()[0]
    assert 'b' == chap1.generate_the_alphabet()[1]
    assert 'c' == chap1.generate_the_alphabet()[2]
    assert 'd' == chap1.generate_the_alphabet()[3]
    assert 'e' == chap1.generate_the_alphabet()[4]
    assert 'f' == chap1.generate_the_alphabet()[5]
    assert 'g' == chap1.generate_the_alphabet()[6]
    assert 'h' == chap1.generate_the_alphabet()[7]
    assert 'i' == chap1.generate_the_alphabet()[8]
    assert 'j' == chap1.generate_the_alphabet()[9]
    assert 'k' == chap1.generate_the_alphabet()[10]
    assert 'l' == chap1.generate_the_alphabet()[11]
    assert 'm' == chap1.generate_the_alphabet()[12]
    assert 'n' == chap1.generate_the_alphabet()[13]
    assert 'o' == chap1.generate_the_alphabet()[14]
    assert 'p' == chap1.generate_the_alphabet()[15]
    assert 'q' == chap1.generate_the_alphabet()[16]
    assert 'r' == chap1.generate_the_alphabet()[17]
    assert 's' == chap1.generate_the_alphabet()[18]
    assert 't' == chap1.generate_the_alphabet()[19]
    assert 'u' == chap1.generate_the_alphabet()[20]
    assert 'v' == chap1.generate_the_alphabet()[21]
    assert 'w' == chap1.generate_the_alphabet()[22]
    assert 'x' == chap1.generate_the_alphabet()[23]
    assert 'y' == chap1.generate_the_alphabet()[24]
    assert 'z' == chap1.generate_the_alphabet()[25]
    
