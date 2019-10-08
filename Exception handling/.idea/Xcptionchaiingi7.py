import sys
class MyException(Exception): pass

try:
    raise TypeError("test")
except TypeError, e:
    raise MyException(str(e)), None, sys.exc_info()[2]