import unittest
from ElementaryTask import numberConverter


class TestNumberConverter(unittest.TestCase):
    def test_validate_number_negative(self):
        expected = 'The number can not be empty \n'
        result = numberConverter.validate_number('')
        self.assertEqual(result, expected)

    def test_zero(self):
        expected = 'ноль'
        result = numberConverter.validate_number('0')
        self.assertEqual(result, expected)

    def test_simple_number(self):
        expected = 'семь'
        result = numberConverter.validate_number('0007')
        self.assertEqual(result, expected)

    def test_dozen_for_one(self):
        expected = 'пятнадцать'
        result = numberConverter.validate_number('15')
        self.assertEqual(result, expected)

    def test_dozen(self):
        expected = 'сорок два'
        result = numberConverter.validate_number('00042')
        self.assertEqual(result, expected)

    def test_hundred(self):
        expected = 'сто три'
        result = numberConverter.validate_number('000103')
        self.assertEqual(result, expected)

    def test_number_clarification(self):
        expected = 'один миллион двести три тысячи четыреста пятьдесят шесть'
        result = numberConverter.validate_number('1203456')
        self.assertEqual(result, expected)

    def test_max_number(self):
        expected = 'девятьсот девяносто девять гуголов '
        expected += 'девятьсот девяносто девять антригинтиллионов девятьсот девяносто девять тригинтиллионов '
        expected += 'девятьсот девяносто девять новемвигинтиллионов девятьсот девяносто девять октовигинтиллионов '
        expected += 'девятьсот девяносто девять септемвигинтиллионов девятьсот девяносто девять сексвигинтиллионов '
        expected += 'девятьсот девяносто девять квинвигинтиллионов девятьсот девяносто девять кватторвигинтиллионов '
        expected += 'девятьсот девяносто девять тревигинтиллионов девятьсот девяносто девять дуовигинтиллионов '
        expected += 'девятьсот девяносто девять анвигинтиллионов девятьсот девяносто девять вигинтиллионов '
        expected += 'девятьсот девяносто девять ундевигинтиллионов девятьсот девяносто девять дуодевигинтиллионов '
        expected += 'девятьсот девяносто девять септдециллионов девятьсот девяносто девять cедециллионов '
        expected += 'девятьсот девяносто девять квиндециллионов девятьсот девяносто девять кваттуордециллионов '
        expected += 'девятьсот девяносто девять тредециллионов девятьсот девяносто девять додециллионов '
        expected += 'девятьсот девяносто девять ундециллионов девятьсот девяносто девять дециллионов '
        expected += 'девятьсот девяносто девять нониллионов девятьсот девяносто девять октиллионов '
        expected += 'девятьсот девяносто девять септиллионов девятьсот девяносто девять секстиллионов '
        expected += 'девятьсот девяносто девять квинтиллионов девятьсот девяносто девять квадриллионов '
        expected += 'девятьсот девяносто девять триллионов девятьсот девяносто девять миллиардов '
        expected += 'девятьсот девяносто девять миллионов '
        expected += 'девятьсот девяносто девять тысяч девятьсот девяносто девять'
        number = '99999999999999999999999999999999999999999999999999999999'
        number += '9999999999999999999999999999999999999999999999'
        result = numberConverter.validate_number(number)
        self.assertEqual(result, expected)

    def test_out_of_the_rage(self):
        number = '99999999999999999999999999999999999999999999999999999999'
        number += '99999999999999999999999999999999999999999999999'
        expected = 'The number ' + number + ' too big'
        result = numberConverter.validate_number(number)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
