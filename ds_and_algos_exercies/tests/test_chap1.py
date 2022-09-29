from unittest import TestCase
import chap1

class ChapterOneTestCase(TestCase):

    def test_is_multiple_returns_true_given_an_appropriate_factor(self):
        """Confirms that the is_multiple function returns True
        when given an appropriate factor
        """
        self.assertTrue(chap1.is_multiple(7, 21))
        self.assertTrue(chap1.is_multiple(3, 21))
    
    def test_is_multiple_returns_false_given_an_invalid_factor(self):
        """Confirms that the is_multiple function return False
        when given an invalid factor
        """
        self.assertFalse(chap1.is_multiple(10, 21))
        self.assertFalse(chap1.is_multiple(13, 21))
    
    def test_is_even_returns_true_when_passed_an_even_number(self):
        """Ensure that is_even would return True when passed
        an even number
        """
        self.assertTrue(chap1.is_even(2))
    
    def test_is_even_returns_false_when_passed_an_odd_number(self):
        """Ensure that is_even would return False when passed
        an odd number
        """
        self.assertFalse(chap1.is_even(1))
    
    def test_minmax_returns_minimum_and_maximum_value_in_a_sorted_list(self):
        """Ensures minmax returns the minimum and maximum list
        element from a sorted list
        """
        self.assertEqual(chap1.minmax([1, 2, 3]), (1, 3))
    
    def test_minmax_returns_minimum_and_maximum_value_in_an_unsorted_list(self):
        """Ensures minmax returns the minimum and maximum list
        element from an unsorted list
        """
        self.assertEqual(chap1.minmax([3, 1, 4, 2]), (1, 4))
    
    def test_minmax_returns_minimum_and_maximum_value_in_a_sorted_negative_integer_list(self):
        """Ensures minmax returns the minimum and maximum list
        element from a sorted negative integer list
        """
        self.assertEqual(chap1.minmax([-3, -2, -1, 0]), (-3, 0))
    
    def test_minmax_returns_minimum_and_maximum_value_in_an_unsorted_negative_integer_list(self):
        """Ensures minmax returns the minimum and maximum list
        element from a sorted negative integer list
        """
        self.assertEqual(chap1.minmax([ -1, -2, 0, -3 ]), (-3, 0))
    
    def test_minmax_returns_the_first_element_as_the_minimum_and_maximum_for_a_single_list(self):
        """Ensure minmax retuns the first element as the minimum
        and maximum in the list
        """
        self.assertEqual(chap1.minmax([-3]), (-3, -3))
        self.assertEqual(chap1.minmax([3]), (3, 3))
        
    




