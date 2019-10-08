import sys
try:
     d = 8
     d = d + '5'
except(TypeError, SyntaxError)as e:
   print sys.exc_info()

