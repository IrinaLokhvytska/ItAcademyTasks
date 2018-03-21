'''Check that triangle exists and return its square'''
import math
import validation


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


class TriangleFactory:
    triangles = list()
    squares = list()

    def add_triangle(self, name, side1, side2, side3):
        triangle = Triangle(name, side1, side2, side3)
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


def check_that_triangle_exists(dict_value):
    '''Check side of the triangle for existence'''
    valid = 0
    msg = ''
    side1, side2, side3 = map(float, (dict_value['side1'], dict_value['side2'], dict_value['side3']))
    if (side1 + side2 >= side3) and (side1 + side3 >= side2) and (side3 + side2 >= side1):
        valid += 1
    else:
        msg += 'The triangle does not exist'
    return valid, msg


def check_triangle_value(name, side1, side2, side3):
    triangle = {
        'name': name,
        'side1': side1,
        'side2': side2,
        'side3': side3
        }
    check_functions = {
       validation.check_empty_value: 4,
       validation.check_float: 3,
       validation.check_number_more_zero: 3,
       check_that_triangle_exists: 1
    }
    i = 0
    for function, expect in check_functions.items():
        if i == 1:
            del triangle['name']
        valid, msg = function(triangle)
        if valid != expect:
            print(msg)
            return False
        i += 1
    return True

add_triangle = True
triangle_factory = TriangleFactory()
while add_triangle:
    msg = 'Enter the name and sides of the triangle separated by commas:'
    try:
        name, side1, side2, side3 = input(msg, ).split(',')
    except Exception as e:
        print(e, msg)
    else:
        if check_triangle_value(name, side1, side2, side3):
            triangle_factory.add_triangle(name, side1, side2, side3)
    answer = input('Do you want to add more triangle? ').strip().upper()
    if answer == 'Y' or answer == 'YES':
        continue
    else:
        print(triangle_factory.show_result())
        add_triangle = False
