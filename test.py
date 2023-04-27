import anomaly.stack as stack
import unittest

class stackTest(unittest.TestCase):

    def test_add(self):
        stack.add_digit("123", 4, '.', "567")
        self.assertEqual(stack.stack[-1], "1234.567", "Should be 1234.567")
    
    def test_clear(self):
        stack.clear()
        self.assertEqual(stack.stack[-1], '', "Should be empty")
    
    def test_return(self):
        stack.stack = ['123.456', '789']
        self.assertEqual(stack.return_stack(), '789', "Should be 789")
        self.assertEqual(stack.return_stack(-2), '123.456', "Should be 123.456")
        
    
    def test_clear_all(self):
        stack.clear(True)
        self.assertEqual(stack.stack, [], "Should be blank")
        stack.add_digit(123)
        stack.clear()
        self.assertEqual(stack.stack[-1], '', "Should be an empty string")
    
    def test_push(self):
        stack.clear(True)
        stack.push(123, 78.9)
        self.assertEqual(stack.return_stack(-2), '78.9', "Should be 78.9")
        self.assertEqual(stack.return_stack(-3), '123', "Should be 123")

    def test_delete(self):
        stack.clear(True)
        stack.add_digit("12.34")
        stack.delete()
        self.assertEqual(stack.return_stack(), "12.3", "Should be 12.3")


if __name__ == "__main__":
    unittest.main()