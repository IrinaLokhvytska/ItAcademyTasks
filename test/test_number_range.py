import unittest
from ElementaryTask import numberRange


class TestNumberRange(unittest.TestCase):
    def test_validate_number_negative(self):
        expected = 'The number can not be empty \n'
        result = numberRange.validate_number('')
        self.assertEqual(result, expected)

    def test_validate_number_positive(self):
        expected = '1, 2, 3, 4, 5, 6, 7, 8'
        result = numberRange.validate_number('3')
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
