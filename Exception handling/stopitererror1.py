import sys
try:
   z =[5, 9, 7]
   i = iter(z)
   print i
   print i.next()
   print i.next()
   print i.next()
   print i.next()
except Exception as e:
    print e
    print sys.exc_type