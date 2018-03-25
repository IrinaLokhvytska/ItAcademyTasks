'''Get the lucky tickets by 2 ways'''
import re
from ElementaryTask import validation


class LuckyTickets:
    def __init__(self, min, max, method):
        self.min = min
        self.max = max
        self.method = method

    @staticmethod
    def addZero(n):
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
            ticket_num = self.addZero(n)
            number_list = list(map(int, list(ticket_num)))
            first = sum(number_list[:3])
            second = sum(number_list[3:])
            if first == second:
                result += 1
            n = int(ticket_num) + 1
        return result

    def __piter_way(self):
        n = int(self.min)
        result = 0
        while n <= int(self.max):
            ticket_num = self.addZero(n)
            number_list = list(map(int, list(ticket_num)))
            result += self.__helper(number_list)
            n = int(ticket_num) + 1
        return result

    def __helper(self, number_list):
        result = odd = even = num_range = 0
        numbers = [even, odd]
        for i in number_list:
            numbers[num_range % 2] += i
            num_range += 1
        if numbers[0] == numbers[1]:
            result = 1
        return result

    def lucky_tickets(self):
        if self.method == 'Moskow':
            return self.__moskow_way()
        else:
            return self.__piter_way()


class ReadMethodFromFile():
    methods = ('Moskow', 'Piter')

    def __init__(self, path):
        self.path = path.strip()

    def __read_method(self):
        try:
            with open(self.path, 'r') as file:
                content = file.read().strip()
                for method in self.methods:
                    if re.fullmatch(method, content):
                        return method
                return 'The path of file does not contain method'
        except:
            return 'The path is not correct'

    def validation(self):
        msg = ''
        if self.path:
            return self.__read_method()
        else:
            msg += 'The path can not be empty'
        return msg


def check_tickets_range(dict_value):
    valid = 0
    msg = ''
    for key, value in dict_value.items():
        if int(value) >= 0 and int(value) < 1000000:
            valid += 1
        else:
            msg += 'The ' + key + ' is not in range [0:1000000]: '
            msg += value + '\n'
    return valid, msg


def check_tickets_value(min, max, method):
    tickets = {'min': min, 'max': max}
    check_functions = {
       validation.check_empty_value: 2,
       validation.check_integer: 2,
       validation.check_min_max_value: 1,
       check_tickets_range: 2
    }
    for function, expect in check_functions.items():
        valid, msg = function(tickets)
        if valid != expect:
            return msg
    lucky_tickets = LuckyTickets(min, max, method)
    return lucky_tickets.lucky_tickets()


if __name__ == '__main__':
    path = input('Enter the path to file with method: ')
    read_method = ReadMethodFromFile(path)
    method = read_method.validation()
    if 'The path' in method:
        print(method)
    else:
        min = input('Enter the min value: ')
        max = input('Enter the max value: ')
        print(check_tickets_value(min, max, method))
