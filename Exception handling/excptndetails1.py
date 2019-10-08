import sys
try:
    foo.execute()
except: # catch *all* exceptions
    e = sys.exc_info()[0]
    print( "Error: %s" % e )
