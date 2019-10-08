import sys
def whatever():
    try:
        f = open ( "foo.txt", 'r' )
    except IOError, e:
       print e
       print sys.exc_type
whatever()
