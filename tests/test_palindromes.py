import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_correct_palindromes(self):
        for i, str_in in enumerate(
            [
                "нажал кабан на баклажан",
                "а роза упала на лапу Азора",
                "пуст суп"
            ]
        ):
            with self.subTest(i):
                result = is_palindrome(str_in)

                self.assertIs(result, True)

    def test_incorrect_palindromes(self):
        for i, str_in in enumerate(
            [
                "дом как комод",
                "карман мрак",
                "армаггедон"
            ]
        ):
            with self.subTest(i):
                result = is_palindrome(str_in)

                self.assertIs(result, False)

    def test_incorrect_type(self):
        str_in = True

        self.assertRaises(TypeError, is_palindrome, str_in)
    
    def test_empty_str(self):
        str_in = ""

        self.assertIs(is_palindrome(str_in), True)

