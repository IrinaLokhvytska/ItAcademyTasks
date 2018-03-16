'''Fibonacci Numbers'''


class FibonacciNumbers:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __fib(self):
        minRange = self.__min_fib()
        a, b = minRange[0], minRange[1]
        result = [a]
        while a < int(self.max):
            a, b = b, a+b
            result.append(a)
        result.pop()
        return result

    def __min_fib(self):
        a, b = 0, 1
        while a < int(self.min):
            a, b = b, a + b
        return (a, b)

    def validation(self):
        '''Validate values'''
        fibonacci = {'min': self.min, 'max': self.max}
        validation = self.__check_fibonacci_values(fibonacci)
        if validation['valid'] == 2:
            if int(self.max) > int(self.min):
                return self.__fib()
            else:
                return 'The min value: ' + self.min + ' can not be greater than max value: ' + self.max
        else:
            return validation['msg']

    def __check_fibonacci_values(self, fibonacci):
        valid = 0
        msg = ''
        for key, value in fibonacci.items():
            if self.__check_empty_value(value):
                if self.__check_positive_numbers(value):
                    valid += 1
                else:
                    msg += key + ' is not a positive integer: ' + value + '\n'
            else:
                msg += key + ' can not be empty \n'
        output = {'valid': valid, 'msg': msg}
        return output

    def __check_empty_value(self, value):
        '''Check that input value isn't empty'''
        validation = False
        if value:
            validation = True
        return validation

    def __check_positive_numbers(self, value):
        '''Check that input value can be converted to integer'''
        validation = False
        try:
            int(value)
        except ValueError:
            return validation
        if int(value) > 0:
            validation = True
        return validation

try:
    min, max = input('Enter the min, max value: ').split(',')
except Exception as e:
    print(e)
else:
    fibonacci = FibonacciNumbers(min, max)
    print(fibonacci.validation())
