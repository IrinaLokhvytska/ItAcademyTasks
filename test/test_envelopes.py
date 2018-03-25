import unittest
from ElementaryTask import comparisonEnvelopes


class TestComparisonEnvelopes(unittest.TestCase):
    def test_check_envelopes_value_negative(self):
        expected = 'The first side of the second envelope can not be empty \n'
        expected += 'The second side of the second envelope can not be empty \n'
        result = comparisonEnvelopes.check_envelopes_value('10', '10', '', '')
        self.assertEqual(result, expected)

    def test_check_envelopes_value_positive(self):
        expected = 'The second envelope is placed in the first.'
        result = comparisonEnvelopes.check_envelopes_value('10', '10', '9', '9')
        self.assertEqual(result, expected)

    def test_not_capacity_of_envelopes(self):
        expected = 'Envelopes can not be placed in each other.'
        result = comparisonEnvelopes.check_envelopes_value('10', '5', '20', '1')
        self.assertEqual(result, expected)

    def test_second_envelope_contains_first(self):
        expected = 'The first envelope is placed in the second.'
        result = comparisonEnvelopes.check_envelopes_value('10', '5', '20', '10')
        self.assertEqual(result, expected)
