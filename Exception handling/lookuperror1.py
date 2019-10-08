import sys
try:
    f = open ( "JohnDoe.txt", 'r' )

except Exception as e:
    print e
    print sys.exc_type