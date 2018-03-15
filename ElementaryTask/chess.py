''' Print the chess board'''


class Chess:
    def __init__(self, width, height, char):
        self.width = width
        self.height = height
        self.char = char

    def __showChess(self):
        '''Print the chess board '''
        i = 0
        output = ''
        while i < int(self.height):
            j = 0
            while j < int(self.width):
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
        validation = self.__checkChessValue(chess)
        if validation['valid'] == 5:
            return self.__showChess()
        else:
            return validation['msg']

    def __checkChessValue(self, chess):
        valid = 0
        msg = ''
        for key, value in chess.items():
            if self.__checkEmptyValue(value):
                if key != 'char':
                    if self.__checkPositiveNumbers(value):
                        valid += 1
                    else:
                        msg += 'The ' + key + ' is not a positive integer: '
                        msg += value + '\n'
                valid += 1
            else:
                msg += 'The ' + key + ' of the chess can not be empty \n'
        output = {'valid': valid, 'msg': msg}
        return output

    def __checkEmptyValue(self, value):
        '''Check that input value isn't empty'''
        validation = False
        if value:
            validation = True
        return validation

    def __checkPositiveNumbers(self, value):
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