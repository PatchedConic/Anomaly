import anomaly.stack
import unittest

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


if __name__ == "__main__":
    unittest.main()