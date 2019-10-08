#A test is OK only if a function throws an expected exception
import unittest
class MyTestCase(unittest.TestCase):
    def test1(self): # test with context manager
        with self.assertRaises(TypeError):
            1 + '1'
    def test2(self):
        import operator
        self.assertRaises(TypeError, operator.add, 1, '1')
unittest.main(exit=False)