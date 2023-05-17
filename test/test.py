import sys
sys.path.append('./')

import anomaly.stack, anomaly.calculator
import unittest
import math

class stackTest(unittest.TestCase):
    stack = anomaly.stack.Stack()

    def test_add(self):
        """This tests the ability of the stack to accept new digits"""
        self.stack.stack = []
        self.stack.add_digit("123", '4', '.', "567")
        self.assertEqual(self.stack.stack[-1], '1234.567', "Should be 1234.567")
    
    def test_clear(self):
        self.stack.stack = []
        self.stack.add_digit('123')
        self.stack.clear()
        self.assertEqual(self.stack.stack[-1], '', "Should be empty")
        self.stack.clear()
        self.assertEqual(self.stack.stack, [], "Should be an empy array")
    
    def test_addNum(self):
        self.stack.clear()
        self.stack.clear()
        self.stack.add_number('123', '78.9')
        self.assertEqual(self.stack.stack[-2], '78.9', "Should be 78.9")
        self.assertEqual(self.stack.stack[-3], '123', "Should be 123")

    def test_delete(self):
        self.stack.clear()
        self.stack.clear()
        self.stack.add_digit('12.34')
        self.stack.delete_digit()
        self.assertEqual(self.stack.stack[-1], '12.3', "Should be 12.3")
    
    def test_pop(self):
        self.stack.clear()
        self.stack.clear()
        self.stack.add_number('12.34', '56', '.78')
        self.assertEqual(self.stack.pop(), '.78', "Should be .78")
        self.assertEqual(self.stack.pop(), '56', "Should be 56")
        self.assertEqual(self.stack.pop(), '12.34', "Should be 12.34")
        self.assertEqual(self.stack.pop(), None, "Stack should be empty")

class calculatorTest(unittest.TestCase):
    calculator = anomaly.calculator.Calculator()

    def test_angular_mode(self):
        self.calculator.set_degrees()
        self.assertEqual(self.calculator.get_angular(), 'deg', "Should be set to degrees, but isn't")
        self.calculator.set_radians()
        self.assertEqual(self.calculator.get_angular(), 'rad', "Should be set to radians")
    
    def test_pi(self):
        self.calculator.pi()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), math.pi, 7, "Should be equal to pi, something is wrong with the pi function")

    def test_napiers(self):
        self.calculator.e()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), math.e, 7, "Should be equal to 2.7182818, something is wrong with the Napier's constant function")

    def test_add(self):
        self.calculator.stack.add_number(1,2)
        self.calculator.add()
        self.assertEqual(self.calculator.stack.pop(), '3.0', "Should be 3")
    
    def test_subtract(self):
        self.calculator.stack.add_number(2,1)
        self.calculator.subtract()
        self.assertEqual(self.calculator.stack.pop(), '1.0', 'Should be 1.0')
    
    def test_multiply(self):
        self.calculator.stack.add_number(2,3)
        self.calculator.multiply()
        self.assertEqual(self.calculator.stack.pop(), '6.0', 'Should be 6.0')

    def test_divide(self):
        self.calculator.stack.add_number(6,1.5)
        self.calculator.divide()
        self.assertEqual(self.calculator.stack.pop(), '4.0', 'Should be 4.0')

    def test_power(self):
        self.calculator.stack.add_number(2,3)
        self.calculator.power()
        self.assertEqual(self.calculator.stack.pop(), '8.0', 'Should be 8.0')
        self.calculator.stack.add_number(8,1/3)
        self.calculator.power()
        self.assertEqual(self.calculator.stack.pop(), '2.0', 'Should be 2.0')

    def test_root(self):
        self.calculator.stack.add_number(25,2)
        self.calculator.root()
        self.assertEqual(self.calculator.stack.pop(), '5.0', 'Should be 5.0')
    
    def test_inverse(self):
        self.calculator.stack.add_number(10)
        self.calculator.inverse()
        self.assertEqual(self.calculator.stack.pop(), '0.1', 'Should be 0.1')
    
    def test_negate(self):
        self.calculator.stack.add_number(-9.341)
        self.calculator.negate()
        self.assertEqual(self.calculator.stack.pop(), '9.341', 'Should be 9.341')
    
    def test_sin(self):
        self.calculator.set_radians()
        self.calculator.stack.add_number(math.pi)
        self.calculator.sin()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), float('0.0'), 7, 'Should be 0.0')
        self.calculator.set_degrees()
        self.calculator.stack.add_number(90)
        self.calculator.sin()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 1, 7, "Should be 1, it seems that deg/rad distinction is broken")

    def test_cos(self):
        self.calculator.set_radians()
        self.calculator.stack.add_number(3*math.pi/2)
        self.calculator.cos()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), float('0.0'), 7, 'Should be 0.0')
        self.calculator.set_degrees()
        self.calculator.stack.add_number(90)
        self.calculator.cos()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 0, 7, "Should be 0, deg/rad seems to be broken")

    def test_tan(self):
        self.calculator.set_radians()
        self.calculator.stack.add_number(math.pi)
        self.calculator.tan()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 0, 7, 'Should be 0.0')
        self.calculator.set_degrees()
        self.calculator.stack.add_number(180)
        self.calculator.tan()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 0, 7, "Should be 0, seems that deg/rad is broken")
    
    def test_asin(self):
        self.calculator.set_radians()
        self.calculator.stack.add_number(1)
        self.calculator.asin()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), math.pi/2, 7, 'Should be pi/2')
        self.calculator.set_degrees()
        self.calculator.stack.add_number(1)
        self.calculator.asin()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 90, 7, "Should be 90, deg/rad seems to be broken")

    def test_acos(self):
        self.calculator.set_radians()
        self.calculator.stack.add_number(0)
        self.calculator.acos()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), math.pi/2, 7, 'Should be pi/2')
        self.calculator.set_degrees()
        self.calculator.stack.add_number(0)
        self.calculator.acos()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 90, 7, "Should be 90, deg/rad seems to be broken")

    def test_atan(self):
        self.calculator.set_radians()
        self.calculator.stack.add_number(1)
        self.calculator.atan()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), math.pi/4, 7, 'Should be pi/4')
        self.calculator.set_degrees()
        self.calculator.stack.add_number(1)
        self.calculator.atan()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 45, 7, "Should be 45, deg/rad seems to be broken")

    def test_naturals(self):
        self.calculator.stack.add_number(1)
        self.calculator.ln()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 0, 7, "Should be 0, it looks like the natural log is broken")
        self.calculator.stack.add_number(1)
        self.calculator.nat_exp()
        self.calculator.ln()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 1, 7, "Should be 1. It looks like the natural exponent function is broken")
    
    def test_log(self):
        self.calculator.stack.add_number(1)
        self.calculator.log()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 0, 7, "It should be 0, it looks like the log function is broken")
        self.calculator.e()
        self.calculator.log()
        self.calculator.e()
        self.calculator.log()
        self.calculator.divide()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 1, 7, "Should be 1, something is wrong with the Napier's constant function")

    def test_squares(self):
        self.calculator.stack.add_number(169)
        self.calculator.sqrt()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 13, 1, "Should be equal to 13, something is wrong with the square root function")
        self.calculator.stack.add_number(4)
        self.calculator.squared()
        self.assertAlmostEqual(float(self.calculator.stack.pop()), 16, 1, "Should be equal to 16, something is wrong with the square function")

        
if __name__ == "__main__":
    unittest.main()