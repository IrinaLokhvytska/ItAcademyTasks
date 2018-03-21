'''Validate values'''


def check_empty_value(dict_value):
    '''Check that value isn't empty'''
    valid = 0
    msg = ''
    for key, value in dict_value.items():
        if value:
            valid += 1
        else:
            msg += 'The ' + key + ' can not be empty \n'
    return valid, msg


def check_integer(dict_value):
    '''Check that value can be converted to integer'''
    valid = 0
    msg = ''
    for key, value in dict_value.items():
        try:
            int(value)
        except ValueError:
            msg += 'The ' + key + ' can not be converted to integer: '
            msg += value + '\n'
        else:
            valid += 1
    return valid, msg


def check_number_more_zero(dict_value):
    '''Check that value more than zero'''
    valid = 0
    msg = ''
    for key, value in dict_value.items():
        if float(value) > 0:
            valid += 1
        else:
            msg += 'The ' + key + ' must be greater than 0: ' + value + '\n'
    return valid, msg


def check_positive_number(dict_value):
    '''Check that value is positive integer'''
    valid = 0
    msg = ''
    for key, value in dict_value.items():
        if int(value) >= 0:
            valid += 1
        else:
            msg += 'The ' + key + ' must be positive integer: ' + value + '\n'
    return valid, msg


def check_min_max_value(dict_value):
    valid = 0
    msg = ''
    min = dict_value['min']
    max = dict_value['max']
    if int(max) > int(min):
        valid += 1
    else:
        msg += 'The min value: ' + min
        msg += ' can not be greater than max value: ' + max
    return valid, msg


def check_float(dict_value):
    '''Check that value can be converted to float'''
    valid = 0
    msg = ''
    for key, value in dict_value.items():
        try:
            float(value)
        except ValueError:
            msg += 'The ' + key + ' can not be converted to float: '
            msg += value + '\n'
        else:
            valid += 1
    return valid, msg
