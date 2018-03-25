'''Count str in text and replace'''
import re
from sys import argv


class FileParser:
    def __init__(self, path, count_str, replace_str=''):
        self.path = path.strip()
        self.count_str = count_str.strip()
        self.replace_str = replace_str.strip()

    def count_str_method(self):
        try:
            with open(self.path, 'r') as file:
                content = file.read()
                search = re.findall(self.count_str, content)
            return len(search)
        except Exception as e:
            return e

    def replace_str_method(self):
        try:
            with open(self.path, 'r') as file:
                content = file.read()
                new_content = re.sub(self.count_str, self.replace_str, content)
                self.__write_to_file(new_content)
        except Exception as e:
            print(e)

    def __write_to_file(self, new_content):
        try:
            with open(self.path, 'w') as file:
                file.write(new_content)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    msg = 'Enter the path to the file and the string to count through a space'
    try:
        path, count_str = argv[1], argv[2]
    except Exception as e:
        print(e, msg)
    else:
        count_str = FileParser(path, count_str)
        print(count_str.count_str_method())

    msg = 'Enter the path to the file, the search string '
    msg += 'and the string to replace with a space'
    try:
        path2, search_str, replace_str = argv[1], argv[2], arg[3]
    except Exception as e:
        print(e, msg)
    else:
        replace_str = FileParser(path2, search_str, replace_str)
        replace_str.replace_str_method()
