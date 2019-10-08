a = [11, 8, 9, 2]
try:
    foo = a[3]
except:
    print "index out of range"
else:
     print "index well within range"