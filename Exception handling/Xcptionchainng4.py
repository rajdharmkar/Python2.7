import sys
try:
    v = {}['a']
except KeyError as e:
    print (e,sys.exc_info())
    raise