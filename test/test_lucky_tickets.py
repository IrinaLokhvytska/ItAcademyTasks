import unittest
from ElementaryTask import luckyTickets


class TestLuckyTickets(unittest.TestCase):
    def test_check_tickets_value_negative(self):
        expected = 'The max can not be empty \n'
        result = luckyTickets.check_tickets_value('5', '', 'Piter')
        self.assertEqual(result, expected)

    def test_check_tickets_value_positive(self):
        expected = 50413
        result = luckyTickets.check_tickets_value('0', '999999', 'Piter')
        self.assertEqual(result, expected)

    def test_check_Moskow_method(self):
        expected = 50413
        result = luckyTickets.check_tickets_value('0', '999999', 'Moskow')
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
