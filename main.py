import unittest
import math

import rectangle
import circle
import square
import triangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter_equal_sides(self):
        res = rectangle.perimeter(4, 4)
        self.assertEqual(res, 16)

    def test_perimeter_different_sides(self):
        res = rectangle.perimeter(3, 5)
        self.assertEqual(res, 16)


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_regular(self):
        res = circle.area(3)
        self.assertAlmostEqual(res, math.pi * 9)

    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_regular(self):
        res = circle.perimeter(2)
        self.assertAlmostEqual(res, 2 * math.pi * 2)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_regular(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_regular(self):
        res = square.perimeter(4)
        self.assertEqual(res, 16)


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_height(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_regular(self):
        res = triangle.area(6, 4)
        self.assertEqual(res, 12)

    def test_perimeter_equal_sides(self):
        res = triangle.perimeter(3, 3, 3)
        self.assertEqual(res, 9)

    def test_perimeter_scalene(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)