import unittest
from list_range import list_of_numbers

class TestList(unittest.TestCase):
    def test_correct_positive_end(self):
        for i, (n, expected_list) in enumerate(
            [
                (1, [1]),
                (3, [1, 2, 3]),
                (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            ]
        ):
            with self.subTest(i):
                result_list = list_of_numbers(n)
                
                self.assertEqual(result_list, expected_list)

    def test_correct_negative_end(self):
        for i, (n, expected_list) in enumerate(
            [
                (-1, [-1]),
                (-3, [-1, -2, -3]),
                (-10, [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
            ]
        ):
            with self.subTest(i):
                result_list = list_of_numbers(n)

                self.assertEqual(result_list, expected_list)
    
    def test_zero_end(self):
        end = 0
        expected_list = []

        result_list = list_of_numbers(end)

        self.assertEqual(result_list, expected_list)

    def test_not_integer_end(self):
        for i, end in enumerate(
            [
                None,
                True,
                9.4,
                'string',
                {"1": 234},
                {1, 2, 3},
                [1, 2]
            ]
        ):
            with self.subTest(i):
                self.assertRaises(TypeError, list_of_numbers, end)

    