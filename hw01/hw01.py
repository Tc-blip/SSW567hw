import unittest
import math



def classify_triangle(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
            return 'right'
        elif a==b and b==c and c==a:
            return 'equilateral'
        elif a==b or b==c or c==a:
            return 'isosceles'
        else:
            return 'scalene'
    else:
        return 'Not a triangle'
    


class Testclassify_triangle(unittest.TestCase):

    def testRight(self):
        self.assertEqual(classify_triangle(3,4,5),'right')
        self.assertNotEqual(classify_triangle(30,60,50),'right')
        self.assertNotEqual(classify_triangle(1,2,3), 'right')
        self.assertNotEqual(classify_triangle(10,2,3), 'right')

    def testEquilateral(self):
        self.assertEqual(classify_triangle(1,1,1),'equilateral')
        self.assertNotEqual(classify_triangle(0,0,0),'equilateral')
        self.assertNotEqual(classify_triangle(30,60,50),'equilateral')
        self.assertNotEqual(classify_triangle(3,4,5), 'equilateral')

    def testIsoceles(self):
        self.assertEqual(classify_triangle(3,3,4),'isosceles')
        self.assertEqual(classify_triangle(3,4,4),'isosceles')
        self.assertNotEqual(classify_triangle(1,1,6),'isosceles')

    def testScalene(self):
        self.assertEqual(classify_triangle(3,4,6),'scalene')
        self.assertEqual(classify_triangle(4,5,6),'scalene')
        self.assertNotEqual(classify_triangle(3,4,5),'scalene')
        self.assertNotEqual(classify_triangle(1,1,6),'scalene')
    
    def testNotATriangle(self):
        self.assertEqual(classify_triangle(1,2,3),'Not a triangle')
        self.assertEqual(classify_triangle(-1,2,3),'Not a triangle')
        self.assertEqual(classify_triangle(-3,-4,-5),'Not a triangle')
        self.assertEqual(classify_triangle(-1,-1,1),'Not a triangle')
        self.assertNotEqual(classify_triangle(3.5,4.5,5),'Not a triangle')

if __name__ == '__main__':
    unittest.main(verbosity=2)