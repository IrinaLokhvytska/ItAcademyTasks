'''Comparison Envelopes'''
import validation


class ComparisonEnvelopes:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def comparison_envelopes(self):
        msg = ''
        a, b, c, d = map(int, (self.a, self.b, self.c, self.d))
        multi_check = lambda x, y, z, f: x*y > z*f
        sum_check = lambda x, y, z, f: x + y > z + f
        pow_check = lambda x, y, z, f: (x**2 + y**2) > (z**2 + f**2)
        min_check = lambda x, y, z, f: min([x, y]) > min([z, f])
        check_methods = (
            multi_check,
            sum_check,
            pow_check,
            min_check
          )
        result_first = []
        result_second = []
        for method in check_methods:
            result_first.append(method(a, b, c, d))
            result_second.append(method(c, d, a, b))
        if all(result_first):
            msg = 'The second envelope is placed in the first.'
        elif all(result_second):
            msg = 'The first envelope is placed in the second.'
        else:
            msg = 'Envelopes can not be placed in each other.'
        return msg


def check_envelopes_value(a, b, c, d):
    envelopes = {
        'The first side of the first envelope': a,
        'The second side of the first envelope': b,
        'The first side of the second envelope': c,
        'The second side of the second envelope': d
    }
    check_functions = {
       validation.check_empty_value: 4,
       validation.check_integer: 4,
       validation.check_number_more_zero: 4
    }
    for function, expect in check_functions.items():
        valid, msg = function(envelopes)
        if valid != expect:
            return msg
    comparison = ComparisonEnvelopes(a, b, c, d)
    return comparison.comparison_envelopes()

continue_comparison = True
while continue_comparison:
    a = input('Enter the first side of the first envelope: ')
    b = input('Enter the second side of the first envelope: ')
    c = input('Enter the first side of the second envelope: ')
    d = input('Enter the second side of the second envelope: ')
    print(check_envelopes_value(a, b, c, d))
    answer = input('Do you want to continue? ').strip().upper()
    if answer == 'Y' or answer == 'YES':
        continue
    else:
        continue_comparison = False
