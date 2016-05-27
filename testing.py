#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import unittest
import calc

class CalcTest(unittest.TestCase):
    # TODO implement tests here to verify that your functions work!
    def testAddition(self):
        self.assertEqual(calc.calc('10+1'), 11)

    def testSubtraction(self):
        self.assertEqual(calc.calc('1-1'), 0)

    def testMultiplciation(self):
        self.assertEqual(calc.calc('1*2'), 2)
 
    def testDivision(self):
        self.assertEqual(calc.calc('10/5'), 2)

if __name__ == '__main__':
    unittest.main()

