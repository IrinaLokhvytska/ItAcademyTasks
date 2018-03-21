''' Print the chess board'''
import validation


class Chess:
    def __init__(self, width, height, char):
        self.width = width
        self.height = height
        self.char = char

    def show_chess(self):
        '''Print the chess board '''
        i = 0
        output = ''
        width, height = map(int, (self.width, self.height))
        helper = (self.char + ' ', ' ' + self.char)
        while i < height:
            j = 0
            while j < width:
                output += helper[i % 2]
                j += 1
            output += '\n'
            i += 1
        return output


def check_chess_value(width, height, char):
    chess = {
        'width': width,
        'height': height,
        'char': char
        }
    check_functions = {
       validation.check_empty_value: 3,
       validation.check_integer: 2,
       validation.check_number_more_zero: 2
    }
    i = 0
    for function, expect in check_functions.items():
        if i == 1:
            del chess['char']
        valid, msg = function(chess)
        if valid != expect:
            return msg
        i += 1
    chess_class = Chess(width, height, char)
    return chess_class.show_chess()

width = input('Enter the width of the chess board: ')
height = input('Enter the height of the chess board: ')
char = input('Enter the char of the chess board: ')
print(check_chess_value(width, height, char))
