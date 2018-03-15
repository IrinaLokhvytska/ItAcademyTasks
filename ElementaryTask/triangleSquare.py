'''Check that triangle exists and return its square'''
import math


class TriangleSquare:
    def __init__(self, name, side1, side2, side3):
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __get_square(self):
        '''Get square of the triangle'''
        side1, side2, side3 = map(float, (self.side1, self.side2, self.side3))
        p = 0.5*(side1 + side2 + side3)
        square = math.sqrt((p*(p-side1)*(p-side2)*(p-side3)))
        return {'name': name,  'square': square}

    def __check_that_triangle_exists(self):
        '''Check side of the triangle for existence'''
        exist = False
        side1, side2, side3 = map(float, (self.side1, self.side2, self.side3))
        if (side1 + side2 >= side3) and (side1 + side3 >= side2) and (side3 + side2 >= side1):
            exist = True
        return exist

    def validation(self):
        '''Validate values'''
        triangle = {'name': name, 'side1': side1, 'side2': side2, 'side3': side3}
        validation = self.__check_triangle_values(triangle)
        if validation['valid'] == 7:
            if self.__check_that_triangle_exists():
                return self.__get_square()
            else:
                return 'The triangle ' + name + ' does not exist'
        else:
            return validation['msg']

    def __check_triangle_values(self, triangle):
        valid = 0
        msg = ''
        for key, value in triangle.items():
            if self.__check_empty_value(value):
                if key != 'name':
                    if self.__check_positive_numbers(value):
                        valid += 1
                    else:
                        msg += 'The ' + key + ' of the triangle ' + triangle['name']
                        msg += ' is not a positive integer: ' + value + '\n'
                valid += 1
            else:
                msg += 'The ' + key + ' of the triangle can not be empty \n'
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
            float(value)
        except ValueError:
            return validation
        if float(value) > 0:
            validation = True
        return validation

add_triangle = True
result = list()


def sort_by_square_key(result):
    return result['square']
while add_triangle:
    name, side1, side2, side3 = input('Enter the name and sides of the triangle: ').split(',')
    triangle = TriangleSquare(name, side1, side2, side3)
    result.append(triangle.validation())
    answer = input('Do you want to add more triangle? ').strip().upper()
    if answer == 'Y' or answer == 'YES':
        continue
    else:
        try:
            a = sorted(result, key=sort_by_square_key)
        except:
            print (result)
        else:
            add_triangle = False
            print(a)
