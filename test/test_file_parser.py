import unittest
import os
from ElementaryTask import fileParser


class TestFileParser(unittest.TestCase):
    file = 'file_parser.txt'

    def setUp(self):
        content = '''Python is an easy to learn, powerful programming language. 
        Python’s elegant syntax and dynamic typing. 
        The Python interpreter and the extensive standard library are freely available 
        in source.'''
        with open(self.file, 'w') as file:
            file.write(content)

    def test_count_str_method(self):
        count_class = fileParser.CountStrInText(self.file, 'Python')
        result = count_class.count_str_method()
        expected = 2
        self.assertEqual(result, expected)

    def test_replace_str_method(self):
        replace_class = fileParser.ReplaceStrInText(self.file, 'Python', 'Test')
        replace_class.replace_str_method()
        expected = 'Test is an easy to learn, powerful programming language. '
        expected += 'Python’s elegant syntax and dynamic typing. '
        expected += 'The Test interpreter and the extensive standard library '
        expected += 'are freely available in source. '
        with open(self.file, 'r') as file:
            result = file.read()
        self.assertEqual(result, expected)

    def tearDown(self):
        os.remove('file_parser.txt')
