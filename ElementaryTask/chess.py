''' Print the chess board'''


class Chess:
    def __init__(self, width, height, char):
        self.width = width
        self.height = height
        self.char = char

    def __show_chess(self):
        '''Print the chess board '''
        i = 0
        output = ''
        width, height = map(int, (self.width, self.height))
        while i < height:
            j = 0
            while j < width:
                if i % 2 == 0:
                    output += (self.char + ' ')
                else:
                    output += (' ' + self.char)
                j += 1
            output += '\n'
            i += 1
        return output

    def validation(self):
        '''Validate values'''
        chess = {
            'width': self.width,
            'height': self.height,
            'char': self.char
            }
        validation = self.__check_chess_value(chess)
        if validation['valid'] == 5:
            return self.__show_chess()
        else:
            return validation['msg']

    def __check_chess_value(self, chess):
        valid = 0
        msg = ''
        for key, value in chess.items():
            if self.__check_empty_value(value):
                if key != 'char':
                    if self.__check_positive_numbers(value):
                        valid += 1
                    else:
                        msg += 'The ' + key + ' is not a positive integer: '
                        msg += value + '\n'
                valid += 1
            else:
                msg += 'The ' + key + ' of the chess can not be empty \n'
        return {'valid': valid, 'msg': msg}

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

width = input('Enter the width of the chess board: ')
height = input('Enter the height of the chess board: ')
char = input('Enter the char of the chess board: ')
chess = Chess(width, height, char)
print(chess.validation())
