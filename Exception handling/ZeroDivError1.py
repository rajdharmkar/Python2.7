import sys
try:
   x = 11/0
   print x
except Exception as e:
    print sys.exc_type
    print e
