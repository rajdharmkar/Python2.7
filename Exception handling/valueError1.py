import sys
try:
    f = float('Tutorialspoint')
    print f
    raise ValueError
except ValueError, e:
       print sys.exc_info()







