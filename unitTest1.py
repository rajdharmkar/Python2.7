import unittest
class MyTestCase(unittest.TestCase):
    def test_1_cannot_add_int_and_str(self):
        with self.assertRaises(TypeError):
            1 + '1'
    def test_2_cannot_add_int_and_str(self):
        import operator
        self.assertRaises(TypeError, operator.add, 1, '1')
unittest.main(exit=False)