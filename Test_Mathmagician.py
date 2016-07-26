import unittest

from mathmagician import *

class TestMathmagician(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(5003))
        self.assertFalse(is_prime(5004))

    def test_generate_integers(self):
        expected = [1, 2, 3, 4, 5]
        nums = [i for i in range(len(expected) + 1)[1:]]
        self.assertEqual(expected, nums)

    def test_generate_fibonacci(self):
        expected = [0, 1, 1, 2, 3, 5, 8]
        nums = [i for i in fibs(len(expected))]
        self.assertEqual(expected, nums)

    def test_generate_primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17]
        nums = [i for i in primes(len(expected))]
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
