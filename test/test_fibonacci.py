import unittest
from ElementaryTask import fibonacci


class TestFibonacciNumbers(unittest.TestCase):
    def test_check_fibonacci_value_negative(self):
        expected = 'The min value: 10'
        expected += ' can not be greater than max value: 5'
        result = fibonacci.check_fibonacci_value('10', '5')
        self.assertEqual(result, expected)

    def test_check_fibonacci_value_positive(self):
        expected = [13, 21, 34, 55, 89, 144]
        result = fibonacci.check_fibonacci_value('10', '160')
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
