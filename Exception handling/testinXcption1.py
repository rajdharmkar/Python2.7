import mymod

# class MyTestCase(unittest.TestCase):
#     def test1(self):
#         self.assertRaises(SomeCoolException, mymod.myfunc)
import unittest
def broken_function():
    raise Exception('This is broken')
class MyTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(Exception) as context:
            broken_function()

        self.assertTrue('This is broken' in context.exception)

if __name__ == '__main__':
    unittest.main()
