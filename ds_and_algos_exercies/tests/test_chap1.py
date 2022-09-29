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



