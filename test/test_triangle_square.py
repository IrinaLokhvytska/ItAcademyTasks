import unittest
from ElementaryTask import triangleSquare


class TestTriangleSquare(unittest.TestCase):
    def test_check_triangle_value_negative(self):
        result = triangleSquare.check_triangle_value('ABC', '10', '10.5', '')
        self.assertFalse(result)

    def test_check_triangle_value_positive(self):
        result = triangleSquare.check_triangle_value('ABC', '10', '10.5', '10.5')
        self.assertTrue(result)

    def test_check_that_triangle_exists_negative(self):
        triangle = {
            'side1': '10',
            'side2': '10.5',
            'side3': '30'
        }
        expected = 0, 'The triangle does not exist'
        result = triangleSquare.check_that_triangle_exists(triangle)
        self.assertEqual(result, expected)

    def test_check_that_triangle_exists_positive(self):
        triangle = {
            'side1': '10',
            'side2': '10.5',
            'side3': '10.5'
        }
        expected = 1, ''
        result = triangleSquare.check_that_triangle_exists(triangle)
        self.assertEqual(result, expected)

    def test_get_square(self):
        triangle = triangleSquare.Triangle('ABC', '10', '10', '10')
        expected = {'name': 'ABC', 'square': 43.3}
        result = triangle.get_square()
        self.assertEqual(result, expected)

    def test_show_result(self):
        triangle_factory = triangleSquare.TriangleFactory()
        triangle_factory.add_triangle('ABC', '10', '10', '10')
        expected = 'Triangles list'.center(30, '=') + '\n'
        expected += 'Triangle [ABC]: 43.3 cm\n'
        result = triangle_factory.show_result()
        del triangle_factory
        self.assertEqual(result, expected)

    def test_add_triangle(self):
        triangle_factory = triangleSquare.TriangleFactory()
        self.assertEqual(0, len(triangle_factory.triangles))


if __name__ == '__main__':
    unittest.main()
