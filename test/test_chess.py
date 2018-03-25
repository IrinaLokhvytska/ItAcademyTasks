import unittest
from ElementaryTask import chess


class TestChess(unittest.TestCase):
    def test_check_chess_value_negative(self):
        expected = 'The char can not be empty \n'
        result = chess.check_chess_value('5', '2', '')
        self.assertEqual(result, expected)

    def test_check_chess_value_positive(self):
        expected = '* * * * * \n'
        expected += ' * * * * *\n'
        result = chess.check_chess_value('5', '2', '*')
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
