import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestTriangleFunction(unittest.TestCase):

    # Позитивные тесты

    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(3, 4, 3), "isosceles")

    def test_scalene(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")


    # Негативные тесты

    def test_invalid_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_negative(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)

    def test_zero(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 2, 3)

    def test_string_input(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 2, 3)


if __name__ == "__main__":
    unittest.main()