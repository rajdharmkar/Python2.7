#A test that fails only if a function doesn't throw an expected exception
import unittest
class MyTestCase(unittest.TestCase):
    def test1(self): # test with context manager
        with self.assertRaises(TypeError):
            1 + 2
    # def test2(self):
    #     import operator
    #     self.assertRaises(TypeError, operator.add, 4, 1)
unittest.main(exit=False)