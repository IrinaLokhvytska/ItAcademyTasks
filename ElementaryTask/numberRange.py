'''Print the list of numders, if sqrt of them less than input number'''
import math


class NumberRange:
    def __init__(self, number):
        self.number = number

    def __calculate_range(self):
        min_num = 1
        output = list()
        while math.sqrt(min_num) < int(self.number):
            output.append(str(min_num))
            min_num += 1
        return ', '.join(output)

    def validation(self):
        msg = ''
        if self.__check_empty_value():
            if self.__check_positive_numbers():
                return self.__calculate_range()
            else:
                msg += 'The ' + self.number + ' is not positive integer \n'
        else:
            msg += 'The ' + self.number + ' can not be empty \n'
        return msg

    def __check_empty_value(self):
        '''Check that input value isn't empty'''
        validation = False
        if self.number:
            validation = True
        return validation

    def __check_positive_numbers(self):
        '''Check that input value can be converted to integer'''
        validation = False
        try:
            int(self.number)
        except ValueError:
            return validation
        if int(self.number) > 0:
            validation = True
        return validation

n = input('Enter the number: ')
number_range = NumberRange(n)
print(number_range.validation())
