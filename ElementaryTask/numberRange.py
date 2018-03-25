'''Print the list of numders, if sqrt of them less than input number'''
import math
from ElementaryTask import validation


class NumberRange:
    def __init__(self, number):
        self.number = number

    def calculate_range(self):
        min_num = 1
        output = list()
        while math.sqrt(min_num) < int(self.number):
            output.append(str(min_num))
            min_num += 1
        return ', '.join(output)


def validate_number(number):
    check_functions = {
       validation.check_empty_value: 1,
       validation.check_integer: 1,
       validation.check_number_more_zero: 1
    }
    for function, expect in check_functions.items():
        valid, msg = function({'number': number})
        if valid != expect:
            return msg
    number_range = NumberRange(number)
    return number_range.calculate_range()


if __name__ == '__main__':
    number = input('Enter the number: ')
    print(validate_number(number))
