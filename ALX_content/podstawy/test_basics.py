import unittest


def power(a, exp):
    return a ** exp


class Vector:
    def __int__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)



class TestMath(unittest.TestCase):
    def test_adding(self):
        a = 1 + 1
        b = 2
        self.assertEqual(a, b)
    def test_power(self):
        x = power(2, 10)
        self.assertEqual(x, 1024)


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.vector00 = Vector(0, 0)
        self.vector10 = Vector(1, 0)
        self.vector01 = Vector(0, 1)


    def test_simple_add(self):
        v = self.vector10 + self.vector01
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 1)
