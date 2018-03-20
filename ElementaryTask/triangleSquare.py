'''Check that triangle exists and return its square'''
import math


class Triangle:
    def __init__(self, name, side1, side2, side3):
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_square(self):
        '''Get square of the triangle'''
        side1, side2, side3 = map(float, (self.side1, self.side2, self.side3))
        p = 0.5*(side1 + side2 + side3)
        square = math.sqrt((p*(p-side1)*(p-side2)*(p-side3)))
        return {'name': self.name,  'square': round(square, 2)}

    def __check_that_triangle_exists(self):
        '''Check side of the triangle for existence'''
        exist = False
        side1, side2, side3 = map(float, (self.side1, self.side2, self.side3))
        if (side1 + side2 >= side3) and (side1 + side3 >= side2) and (side3 + side2 >= side1):
            exist = True
        return exist

    def is_valid(self):
        valid = self.__validation()
        if valid[0]:
            return True
        else:
            print(valid[1])

    def __validation(self):
        '''Validate values'''
        triangle = {
            'name': self.name,
            'side1': self.side1,
            'side2': self.side2,
            'side3': self.side3
            }
        validation = self.__check_triangle_values(triangle)
        if validation['valid'] == 7:
            if self.__check_that_triangle_exists():
                return True, ''
            else:
                msg = 'The triangle ' + self.name + ' does not exist'
                return False, msg
        else:
            return False, validation['msg']

    def __check_triangle_values(self, triangle):
        valid = 0
        msg = ''
        for key, value in triangle.items():
            if self.__check_empty_value(value):
                if key != 'name':
                    if self.__check_positive_numbers(value):
                        valid += 1
                    else:
                        msg += 'The ' + key + ' of ' + triangle['name']
                        msg += ' is not a positive integer: '
                        msg += value + '\n'
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


class TriangleFactory:
    triangles = list()
    squares = list()

    def add_triangle(self, name, side1, side2, side3):
        triangle = Triangle(name, side1, side2, side3)
        if triangle.is_valid():
            self.triangles.append(triangle)

    def __calculate_squares(self):
        for triangle in self.triangles:
            self.squares.append(triangle.get_square())

    def __sort_squares(self):
        self.__calculate_squares()
        return sorted(self.squares, key=lambda x: x['square'], reverse=True)

    def show_result(self):
        output = 'Triangles list'.center(30, '=') + '\n'
        triangle_squares = self.__sort_squares()
        for triangle in triangle_squares:
            output += 'Triangle [{}]: '.format(triangle['name'])
            output += '{} cm'.format(triangle['square']) + '\n'
        return output

add_triangle = True
triangle_factory = TriangleFactory()
while add_triangle:
    msg = 'Enter the name and sides of the triangle separated by commas:'
    try:
        name, side1, side2, side3 = input(msg, ).split(',')
    except Exception as e:
        print(e, msg)
    else:
        triangle_factory.add_triangle(name, side1, side2, side3)
    answer = input('Do you want to add more triangle? ').strip().upper()
    if answer == 'Y' or answer == 'YES':
        continue
    else:
        print(triangle_factory.show_result())
        add_triangle = False
