'''Get the lucky tickets by 2 ways'''


class LuckyTickets:
    def __init__(self, min, max, method):
        self.min = min
        self.max = max
        self.method = method

    def __addZero(self, n):
        ticketsRange = {
            '00000': [0, 10],
            '0000': [10, 100],
            '000': [100, 1000],
            '00': [1000, 10000],
            '0': [10000, 100000],
            '': [100000, 1000000]
        }
        for key, value in ticketsRange.items():
            if int(n) in range(value[0], value[1]):
                n = str(n) + key
        return n

    def __moskow_way(self):
        n = int(self.min)
        result = 0
        while n <= int(self.max):
            first = second = 0
            n = self.__addZero(n)
            for i in list(n[:3]):
                first += int(i)
            for i in list(n[3:]):
                second += int(i)
            if (first == second):
                result += 1
            n = int(n) + 1
        return result

    def __piter_way(self):
        n = int(self.min)
        result = 0
        while n <= int(self.max):
            n = self.__addZero(n)
            arr = list(n)
            result += self.__helper(arr)
            n = int(n) + 1
        return result

    def __helper(self, arr):
        result = odd = even = sum = 0
        num_range = 0
        for i in arr:
            if num_range % 2 == 0:
                even += int(i)
            else:
                odd += int(i)
            num_range += 1
        if odd == even:
            result = 1
        return result

    def __lucky_tickets(self):
        if self.method == 'Moskow':
            return self.__moskow_way()
        else:
            return self.__piter_way()

    def __check_empty_value(self, value):
        '''Check that input value isn't empty'''
        validation = False
        if value:
            validation = True
        return validation

    def __check_numbers(self, value):
        '''Check that input value can be converted to integer'''
        try:
            int(value)
        except ValueError:
            return False
        return True

    def __check_tickets_range(self, value):
        validation = False
        if int(value) >= 0 and int(value) < 1000000:
            validation = True
        return validation

    def validation(self):
        '''Validate values'''
        tickets = {'min': self.min, 'max': self.max}
        validation = self.__check_tickets_values(tickets)
        if validation['valid'] == 2:
            if int(self.max) > int(self.min):
                return self.__lucky_tickets()
            else:
                return 'The max value: ' + self.max + ' should be greater than min value: ' + self.min
        else:
            return validation['msg']

    def __check_tickets_values(self, tickets):
        valid = 0
        msg = ''
        for key, value in tickets.items():
            if self.__check_empty_value(value):
                if self.__check_numbers(value):
                    if self.__check_tickets_range(value):
                        valid += 1
                    else:
                        msg += 'The ' + key + ' is not in range [0:1000000]: ' + value + '\n'
                else:
                    msg += 'The ' + key + ' is not a positive integer: ' + value + '\n'
            else:
                msg += 'The ' + key + ' can not be empty \n'
        output = {'valid': valid, 'msg': msg}
        return output


class ReadMethodFromFile():
    def __init__(self, path):
        self.path = path

    def __read_method(self):
        try:
            open(self.path, 'r')
        except:
            return 'The path is not correct'
        with open(self.path, 'r') as file:
            content = file.read().split()
            if 'Moskow' in content:
                return 'Moskow'
            elif 'Piter' in content:
                return 'Piter'
            else:
                return 'The path of file does not contain method'

    def __check_empty_value(self):
        '''Check that input value isn't empty'''
        if self.path:
            return True
        return False

    def __check_str(self):
        '''Check that input value can be converted to string'''
        validation = False
        try:
            str(self.path)
        except ValueError:
            return validation
        else:
            return True

    def validation(self):
        msg = ''
        if self.__check_empty_value():
            if self.__check_str():
                return self.__read_method()
            else:
                msg += 'The path' + self.path + 'should be a string'
        else:
            msg += 'The path can not be empty'
        return msg


path = input('Enter the path to file with method: ')
read_method = ReadMethodFromFile(path)
method = read_method.validation()
if 'The path' in method:
    print(method)
else:
    min = input('Enter the min value: ')
    max = input('Enter the max value: ')
    lucky_tickets = LuckyTickets(min, max, method)
    print(lucky_tickets.validation())

