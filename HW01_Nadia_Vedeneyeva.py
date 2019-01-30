"""
Nadia Vedeneyeva
HW01
Testing triangle classification
"""

import unittest



class Classy_Triangle():
   
    def __init__(self, a, b, c):
        """Function takes three parameters as lengths of the sides of a triangle,
        evaluates if it's a valid triangle and raises an error if it's not"""
        self.a = a
        self.b = b
        self.c = c
        if self.a + self.b < self.c or\
            self.a + self.c < self.b or\
            self.b + self.c < self.a:
            raise ValueError('Not a triangle')  #Sum of two sides is smaller than the third side


    def classification(self):
        """Function classifies if triangle is equilateral, isosceles or scalene"""
        if self.a == self.b and self.a == self.c:
            return 'The triangle is equilateral' 
        elif self.a == self.b and self.a != self.c or\
            self.a == self.c and self.a != self.b or\
            self.b == self.c and self.b != self.a:
            return 'The triangle is isosceles'
        else:
            self.a != self.b and self.a != self.c and self.b != self.c
            return 'The triangle is scalene'


    def right(self):
        """Function checks if it's a right triangle"""
        if (self.a ** 2) + (self.b ** 2) == self.c ** 2 or\
            (self.a ** 2) + (self.c ** 2) == self.b ** 2 or\
            (self.b ** 2) + (self.c ** 2) == self.a ** 2:
            return 'It is a right triangle'
        else:
            return 'It is not a right triangle'

        

def main():
    """Function invokes Classy_Triangle with given values"""
    a = 5
    b = 4
    c = 2
    try:
        triangle = Classy_Triangle(a, b, c)
    except ValueError as e:     #Sum of two sides is smaller than the third side
        print(e) 
    sides = triangle.classification()
    right = triangle.right()
    print(sides)
    print(right)


class Classy_TriangleTest(unittest.TestCase):
    """TEST"""

    def test_init(self):
        """Testing if parameters are stored correctly in __init__()"""
        triangle = Classy_Triangle(2, 3, 4)
        self.assertEqual(triangle.a, 2)
        self.assertEqual(triangle.b, 3)
        self.assertEqual(triangle.c, 4)
        self.assertNotEqual(triangle.a, 1)

    def test_valid_triangle(self):
        """Testing ValueError"""
        with self.assertRaises(ValueError):
            Classy_Triangle(2, 3, 6)
        """
        with self.assertRaises(ValueError):
            Classy_Triangle(2, 3, 0)
        with self.assertRaises(ValueError):
            Classy_Triangle(1, 2, 3)
        """

    def test_classification(self):
        """Testing classification function"""
        triangle1 = Classy_Triangle(2, 3, 4)
        triangle2 = Classy_Triangle(3, 3, 4)
        triangle3 = Classy_Triangle(2, 2, 2)
        self.assertEqual(Classy_Triangle.classification(triangle1), 'The triangle is scalene')
        self.assertEqual(Classy_Triangle.classification(triangle2), 'The triangle is isosceles')
        self.assertEqual(Classy_Triangle.classification(triangle3), 'The triangle is equilateral')
        self.assertNotEqual(Classy_Triangle.classification(triangle1), 'The triangle is equilateral')

    def right(self):
        """Testing right function"""
        triangle1 = Classy_Triangle(3, 4, 5)
        triangle2 = Classy_Triangle(2, 4, 5)
        self.assertEqual(Classy_Triangle.right(triangle1), 'It is a right triangle')
        self.assertEqual(Classy_Triangle.right(triangle2), 'It is not a right triangle')
        self.assertNotEqual(Classy_Triangle.right(triangle1), 'It is not a right triangle')


        
        
main()


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
