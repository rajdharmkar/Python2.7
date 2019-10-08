import sys
try:
    class Foobar:
       def __init__(self):
          self.p = 0

    f = Foobar()
    print(f.p)
    print(f.q)
except Exception as e:
    print e
    print sys.exc_type
    print 'This is an example of StandardError exception'