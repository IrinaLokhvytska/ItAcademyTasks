'''Count str in text and replace'''
import re


class RemovePunctuation:
    punctuation_marks = (
        '.',
        ',',
        '?',
        '!',
        ':',
        ';',
        '-',
        '...',
        '(',
        ')',
        '"',
        '\''
    )

    def _remove_punctuation(self, word):
        for mark in self.punctuation_marks:
            if mark in word:
                word = word.replace(mark, '')
        return word


class CountStrInText(RemovePunctuation):
    def __init__(self, path, count_str):
        self.path = path.strip()
        self.count_str = count_str.strip()

    def count_str_method(self):
        try:
            with open(self.path, 'r') as file:
                content = file.read().split()
                result = 0
                for word in content:
                    helper = self._remove_punctuation(word)
                    if re.fullmatch(self.count_str, helper):
                        result += 1
            return result
        except Exception as e:
            return e


class ReplaceStrInText(RemovePunctuation):
    def __init__(self, path, search_str, replace_str):
        self.path = path.strip()
        self.search_str = search_str.strip()
        self.replace_str = replace_str.strip()

    def replace_str_method(self):
        new_content = ''
        try:
            with open(self.path, 'r') as file:
                content = file.read().split()
                for word in content:
                    helper = self._remove_punctuation(word)
                    if re.fullmatch(self.search_str, helper):
                        new_content += re.sub(helper, self.replace_str, word)
                        new_content += ' '
                    else:
                        new_content += word + ' '
                self.__wtite_to_file(new_content)
        except Exception as e:
            print(e)

    def __wtite_to_file(self, new_content):
        try:
            with open(self.path, 'w') as file:
                file.write(new_content)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    msg = 'Enter the path to the file and the string to count through a space'
    try:
        path, count_str = input(msg, ).split()
    except Exception as e:
        print(e, msg)
    else:
        count_str = CountStrInText(path, count_str)
        print(count_str.count_str_method())

    msg = 'Enter the path to the file, the search string '
    msg += 'and the string to replace with a space'
    try:
        path2, search_str, replace_str = input(msg, ).split()
    except Exception as e:
        print(e, msg)
    else:
        replace_str = ReplaceStrInText(path2, search_str, replace_str)
        replace_str.replace_str_method()
