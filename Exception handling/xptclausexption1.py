import sys
try:
    a = john
except:
    try:
        4/0
    except:
        print (sys.exc_info())


