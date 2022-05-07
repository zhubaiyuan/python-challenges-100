import unittest
from parameterized import parameterized


def input_and_expected():
    return [(1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21)]


class FibonacciTest(unittest.TestCase):
    @parameterized.expand(input_and_expected())
    def test_fib_rec(self, n, expected):
        from challenges.c013_fibonacci import fib_rec
        result = fib_rec(n)
        self.assertEqual(result, expected)

    @parameterized.expand(input_and_expected())
    def test_fib_iterative(self, n, expected):
        from challenges.c013_fibonacci import fib_iterative
        result = fib_iterative(n)
        self.assertEqual(result, expected)

    def test_fib_rec_wrong_input(self):
        from challenges.c013_fibonacci import fib_rec
        with self.assertRaises(Exception) as excinfo:
            fib_rec(0)
        self.assertTrue("n must be >= 1" in str(excinfo.exception))

    def test_fib_iterative_wrong_input(self):
        from challenges.c013_fibonacci import fib_iterative
        with self.assertRaises(Exception) as excinfo:
            fib_iterative(0)
        self.assertTrue("n must be >= 1" in str(excinfo.exception))


if __name__ == '__main__':
    unittest.main()
