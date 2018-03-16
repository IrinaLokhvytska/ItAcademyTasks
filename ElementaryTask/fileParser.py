'''Count str in text and replace'''


class CountStrInText():
    def __init__(self, path, count_str):
        self.path = path
        self.count_str = count_str

    def __count_str(self):
        with open(self.path, 'r') as file:
            content = file.read().split()
            n_str = content.count(self.count_str.strip())
        return n_str

    def validation(self):
        param = {
            'path': self.path,
            'string to count': self.count_str
            }
        validation = self.__check_value(param)
        if validation['valid'] == 4:
            return self.__count_str()
        else:
            return validation['msg']

    def __check_value(self, param):
        valid = 0
        msg = ''
        for key, value in param.items():
            if self.__check_empty_value(value):
                if self.__check_str(value):
                    valid += 1
                else:
                    msg += 'The ' + key + ' should be a string \n'
                valid += 1
            else:
                msg += 'The ' + key + ' can not be empty \n'
        output = {'valid': valid, 'msg': msg}
        return output

    def __check_empty_value(self, value):
        '''Check that input value isn't empty'''
        validation = False
        if value:
            validation = True
        return validation

    def __check_str(self, value):
        '''Check that input value can be converted to string'''
        validation = False
        try:
            str(value)
        except ValueError:
            return validation
        else:
            return True


class ReplaceStrInText():
    def __init__(self, path, search_str, replace_str):
        self.path = path
        self.search_str = search_str
        self.replace_str = replace_str

    def __replace_str(self):
        new_content = ''
        with open(self.path, 'r') as file:
            content = file.read().split()
            for word in content:
                if word == self.search_str.strip():
                    new_content += self.replace_str.strip() + ' '
                else:
                    new_content += word + ' '
            with open(self.path, 'w') as wfile:
                wfile.write(new_content)

    def validation(self):
        param = {
            'path': self.path,
            'string to find': self.search_str,
            'string to replace': self.replace_str
            }
        validation = self.__check_value(param)
        if validation['valid'] == 6:
            self.__replace_str()
        else:
            return validation['msg']

    def __check_value(self, param):
        valid = 0
        msg = ''
        for key, value in param.items():
            if self.__check_empty_value(value):
                if self.__check_str(value):
                    valid += 1
                else:
                    msg += 'The ' + key + ' should be a string \n'
                valid += 1
            else:
                msg += 'The ' + key + ' can not be empty \n'
        output = {'valid': valid, 'msg': msg}
        return output

    def __check_empty_value(self, value):
        '''Check that input value isn't empty'''
        validation = False
        if value:
            validation = True
        return validation

    def __check_str(self, value):
        '''Check that input value can be converted to string'''
        validation = False
        try:
            str(value)
        except ValueError:
            return validation
        else:
            return True

path, count_str = input('Enter the file and str to count', ).split()
path2, search_str, replace_str = input('Enter the file and strs to replace', ).split()
count_str = CountStrInText(path, count_str)
replace_str = ReplaceStrInText(path2, search_str, replace_str)
print(count_str.validation())
