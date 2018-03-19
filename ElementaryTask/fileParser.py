'''Count str in text and replace'''
import re


class CountStrInText():
    def __init__(self, path, count_str):
        self.path = path.strip()
        self.count_str = count_str.strip()

    def count_str_method(self):
        try:
            with open(self.path, 'r') as file:
                content = file.read()
                search_str = re.findall(self.count_str, content)
            return len(search_str)
        except Exception as e:
            return e


class ReplaceStrInText():
    def __init__(self, path, search_str, replace_str):
        self.path = path.strip()
        self.search_str = search_str.strip()
        self.replace_str = replace_str.strip()

    def replace_str_method(self):
        new_content = ''
        try:
            with open(self.path, 'r') as file:
                content = file.read()
                new_content = re.sub(self.search_str, self.replace_str, content)
        except Exception as e:
            print(e)
        try:
            with open(self.path, 'w') as file:
                file.write(new_content)
        except Exception as e:
            print(e)

try:
    path, count_str = input('Enter the file and str to count', ).split()
except Exception as e:
    print(e, 'Enter the path to the file and the string to count through a space')
else:
    count_str = CountStrInText(path, count_str)
    print(count_str.count_str_method())

try:
    path2, search_str, replace_str = input('Enter the file and strs to replace', ).split()
except Exception as e:
    print(e, 'Enter the path to the file, the search string and the string to replace with a space')
else:
    replace_str = ReplaceStrInText(path2, search_str, replace_str)
    replace_str.replace_str_method()
