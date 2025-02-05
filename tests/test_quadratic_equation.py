import unittest
from homework.quadratic_equation import solution


class TestSquareEquation(unittest.TestCase):
    def test_correct_equation_both_roots(self):
        for i, (a, b, c, expected_roots) in enumerate(
            [
                [1, 8, 15, (-3, -5)],
                [1, -13, 12, (12, 1)],
                [1, 9, 15, (-6.79, -2.21)]
            ]
        ):
            with self.subTest(i):
                result_roots = solution(a, b, c)

                # не важен порядок корней
                self.assertEqual(set(expected_roots), set(result_roots))
    
    def test_correct_equation_one_root(self):
        for i, (a, b, c, expected_root) in enumerate(
            [
                [1, 2, 1, -1],
                [-4, 28, -49, 3.5],
                [-1, 16, -64, 8],
                [1, 0, 0, 0],
            ]
        ):
            with self.subTest(i):
                result_root = solution(a, b, c)

                self.assertEqual(expected_root, result_root)
    
    def test_correct_equation_no_roots(self):
        for i, (a, b, c, expected_root) in enumerate(
            [
                [1, 1, 1, None],
                [1, 1, 29, None],
                [12, 13, 121, None],
            ]
        ):
            with self.subTest(i):
                result_root = solution(a, b, c)

                self.assertIs(expected_root, result_root)
    
    def test_non_quadratic_equation_value_error(self):
        a, b, c = 0, 1, 2

        self.assertRaises(ValueError, solution, a, b, c)
    
    def test_a_b_c_not_integers(self):
        a, b, c = 'string', None, True

        self.assertRaises(TypeError, solution, a, b, c)