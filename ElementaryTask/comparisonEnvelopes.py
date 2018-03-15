'''Comparison Envelopes'''


class ComparisonEnvelopes:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __comparison_envelopes(self):
        msg = ''
        a, b, c, d = map(int, (self.a, self.b, self.c, self.d))
        if (a*b >= c*d) and ((a**2 + b**2) >= (c**2 + d**2)) and (a + b >= c + d) and (min([a, b]) >= min([c, d])):
            msg = 'The second envelope is placed in the first.'
        elif (c*d >= a*b) and ((c**2 + d**2) >= (a**2 + b**2)) and (c + d >= a + b) and (min([c, d]) >= min([a, b])):
            msg = 'The first envelope is placed in the second.'
        else:
            msg = 'Envelopes can not be placed in each other.'
        return msg

    def validation(self):
        '''Validate values'''
        envelopes = {
            'The first side of the first envelope': self.a,
            'The second side of the first envelope': self.b,
            'The first side of the second envelope': self.c,
            'The second side of the second envelope': self.d
            }
        validation = self.__check_envelopes_value(envelopes)
        if validation['valid'] == 4:
            return self.__comparison_envelopes()
        else:
            return validation['msg']

    def __check_envelopes_value(self, envelopes):
        valid = 0
        msg = ''
        for key, value in envelopes.items():
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

continue_comparison = True
while continue_comparison:
    a = input('Enter the first side of the first envelope: ')
    b = input('Enter the second side of the first envelope: ')
    c = input('Enter the first side of the second envelope: ')
    d = input('Enter the second side of the second envelope: ')
    comparison = ComparisonEnvelopes(a, b, c, d)
    print(comparison.validation())
    answer = input('Do you want to continue? ').strip().upper()
    if answer == 'Y' or answer == 'YES':
        continue
    else:
        continue_comparison = False
