# -*- coding: utf-8 -*-
"""
make changes to TestTriangle.py
HW2a 
Feb, 3, 2020

@author: Cheng Tian
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(1000,2,3),'InvalidInput','1000,2,3 is a InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(1,-2,3),'InvalidInput','1,-2,3 is a InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(1,2.0,3),'InvalidInput','1,-2,3 is a InvalidInput')

    def testTrianglesA(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is a NotATriangle')
    
    def testTrianglesB(self):
        self.assertEqual(classifyTriangle(199,100,3),'NotATriangle','199,100,3 is a NotATriangle')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classifyTriangle(3,5,6),'Scalene','3,5,6 should be Scalene')

    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(5,6,3),'Scalene','5,6,3 should be Scalene')

    def testScaleneTrianglesC(self): 
        self.assertEqual(classifyTriangle(200,199,198),'Scalene','200,199,198 should be Scalene')

    def testIsocelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(3,3,4),'Isoceles','3,3,4 should be Isoceles')
    
    def testIsocelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(4,3,3),'Isoceles','4,3,3 should be Isoceles')
    
    def testIsocelesTrianglesC(self): 
        self.assertEqual(classifyTriangle(3,4,3),'Isoceles','3,4,3 should be Isoceles')
    
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

