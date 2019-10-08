import sys
try:
     def foo():
         print manogna
     foo()

except NameError as e:
    print e
    print sys.exc_type
