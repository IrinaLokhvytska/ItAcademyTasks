'''Comparison Envelopes'''
from ElementaryTask import validation


class ComparisonEnvelopes:
    def __init__(self, length_env1, width_env1, length_env2, width_env2):
        self.length_env1 = length_env1
        self.width_env1 = width_env1
        self.length_env2 = length_env2
        self.width_env2 = width_env2

    def comparison_envelopes(self):
        a, b, c, d = map(int, (self.length_env1, self.width_env1, self.length_env2, self.width_env2))
        check_methods = (
            lambda x, y, z, f: x*y > z*f,
            lambda x, y, z, f: x + y > z + f,
            lambda x, y, z, f: (x**2 + y**2) > (z**2 + f**2),
            lambda x, y, z, f: min([x, y]) > min([z, f])
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


def check_envelopes_value(length_env1, width_env1, length_env2, width_env2):
    envelopes = {
        'first side of the first envelope': length_env1,
        'second side of the first envelope': width_env1,
        'first side of the second envelope': length_env2,
        'second side of the second envelope': width_env2
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
    comparison = ComparisonEnvelopes(length_env1, width_env1, length_env2, width_env2)
    return comparison.comparison_envelopes()


if __name__ == '__main__':
    continue_comparison = True
    while continue_comparison:
        length_env1 = input('Enter the first side of the first envelope: ')
        width_env1 = input('Enter the second side of the first envelope: ')
        length_env2 = input('Enter the first side of the second envelope: ')
        width_env2 = input('Enter the second side of the second envelope: ')
        print(check_envelopes_value(length_env1, width_env1, length_env2, width_env2))
        answer = input('Do you want to continue? ').strip().upper()
        if answer == 'Y' or answer == 'YES':
            continue
        else:
            continue_comparison = False
