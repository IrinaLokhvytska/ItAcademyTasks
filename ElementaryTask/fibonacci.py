'''Fibonacci Numbers'''
from ElementaryTask import validation


class FibonacciNumbers:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def fib(self):
        minRange = self.__min_fib()
        first, second = minRange[0], minRange[1]
        result = [first]
        while first < int(self.max):
            first, second = second, first+second
            result.append(first)
        result.pop()
        return result

    def __min_fib(self):
        first, second = 0, 1
        while first < int(self.min):
            first, second = second, first + second
        return (first, second)


def check_fibonacci_value(min, max):
    fibonacci = {'min': min, 'max': max}
    check_functions = {
       validation.check_empty_value: 2,
       validation.check_integer: 2,
       validation.check_number_more_zero: 2,
       validation.check_min_max_value: 1
    }
    for function, expect in check_functions.items():
        valid, msg = function(fibonacci)
        if valid != expect:
            return msg
    fibonacci_class = FibonacciNumbers(min, max)
    return fibonacci_class.fib()

if __name__ == '__main__':
    msg = 'Enter the min, max value separated by commas'
    try:
        min, max = input(msg, ).split(',')
    except Exception as e:
        print(e, msg)
    else:
        print(check_fibonacci_value(min, max))
