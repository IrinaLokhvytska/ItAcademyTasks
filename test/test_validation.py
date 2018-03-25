import unittest
from ElementaryTask import validation


class TestValidation(unittest.TestCase):
    def test_check_empty_value_positive(self):
        dict_value = {'number': '5'}
        expected = 1, ''
        result = validation.check_empty_value(dict_value)
        self.assertEqual(result, expected)

    def test_check_empty_value_negative(self):
        dict_value = {'number': ''}
        expected = 0, 'The number can not be empty \n'
        result = validation.check_empty_value(dict_value)
        self.assertEqual(result, expected)

    def test_check_integer_positive(self):
        dict_value = {'number': '5'}
        expected = 1, ''
        result = validation.check_integer(dict_value)
        self.assertEqual(result, expected)

    def test_check_integer_negative(self):
        dict_value = {'number': 'abs'}
        msg = 'The number can not be converted to integer: '
        msg += 'abs\n'
        expected = 0, msg
        result = validation.check_integer(dict_value)
        self.assertEqual(result, expected)

    def test_check_number_more_zero_positive(self):
        dict_value = {'number': '5'}
        expected = 1, ''
        result = validation.check_number_more_zero(dict_value)
        self.assertEqual(result, expected)

    def test_check_number_more_zero_negative(self):
        dict_value = {'number': '-5'}
        expected = 0, 'The number must be greater than 0: -5\n'
        result = validation.check_number_more_zero(dict_value)
        self.assertEqual(result, expected)

    def test_check_positive_number_positive(self):
        dict_value = {'number': '0'}
        expected = 1, ''
        result = validation.check_positive_number(dict_value)
        self.assertEqual(result, expected)

    def test_check_positive_number_negative(self):
        dict_value = {'number': '-5'}
        expected = 0, 'The number must be positive integer: -5\n'
        result = validation.check_positive_number(dict_value)
        self.assertEqual(result, expected)

    def test_check_min_max_value_positive(self):
        dict_value = {'min': '10', 'max': '25'}
        expected = 1, ''
        result = validation.check_min_max_value(dict_value)
        self.assertEqual(result, expected)

    def test_check_min_max_value_negative(self):
        dict_value = {'min': '35', 'max': '10'}
        msg = 'The min value: 35'
        msg += ' can not be greater than max value: 10'
        expected = 0, msg
        result = validation.check_min_max_value(dict_value)
        self.assertEqual(result, expected)

    def test_check_float_positive(self):
        dict_value = {'number': '10.589'}
        expected = 1, ''
        result = validation.check_float(dict_value)
        self.assertEqual(result, expected)

    def test_check_float_negative(self):
        dict_value = {'number': 'abc'}
        msg = 'The number can not be converted to float: '
        msg += 'abc\n'
        expected = 0, msg
        result = validation.check_float(dict_value)
        self.assertEqual(result, expected)
