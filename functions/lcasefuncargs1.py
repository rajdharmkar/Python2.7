#program to print lowercase of the list of function arguments
import inspect
def foo(ARG1, ARG2):
    pass
list1 = inspect.getargspec(foo)[0]
list1 =[item.lower() for item in list1]
print list1
'''if __name__ == '__main__':
    import sys
    lcasefuncargs1.py = sys.argv[1]'''
