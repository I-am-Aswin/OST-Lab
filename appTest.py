import unittest
from app import palindrome, add, greet

class AppTest( unittest.TestCase ):

    def test_true_palindrome(self):
        self.assertTrue(palindrome(121))
    
    def test_false_palindrome(self):
        self.assertFalse( palindrome(123) )
    
    def test_add(self):
        self.assertEqual(add(2,3), 5)
    
    def test_greet(self):
        self.assertEqual(greet("python"), "Hello python")

if __name__ == '__main__':
    unittest.main()