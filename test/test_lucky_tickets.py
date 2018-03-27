import unittest
from ElementaryTask import luckyTickets


class TestLuckyTickets(unittest.TestCase):
    def test_check_tickets_value_negative(self):
        expected = 'The max can not be empty \n'
        result = luckyTickets.check_tickets_value('5', '', 'Piter')
        self.assertEqual(result, expected)

    def test_check_tickets_value_positive(self):
        expected = 55252
        result = luckyTickets.check_tickets_value('0', '999999', 'Piter')
        self.assertEqual(result, expected)

    def test_check_Moskow_method(self):
        expected = 55252
        result = luckyTickets.check_tickets_value('0', '999999', 'Moskow')
        self.assertEqual(result, expected)

    def test_addZero(self):
        expected = '000005'
        tickets_class = luckyTickets.LuckyTickets('5', '10', 'Moskow')
        result = tickets_class.addZero('5')
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
