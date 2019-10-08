import sys
try:
    s = {'a':5, 'b':7}['c']

except:
    print (sys.exc_info())

