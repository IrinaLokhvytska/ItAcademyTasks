'''Fibonacci Numbers'''
import validation


class FibonacciNumbers:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def fib(self):
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
