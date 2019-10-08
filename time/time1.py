# example of time.sleep() method
#  time.sleep(t)
# Parameters
# tThis is the number of seconds execution to be suspended.
# Return Value
# This method does not return any value.

import time
print "Start : %s" % time.ctime()
time.sleep( 5 )
print "End : %s" % time.ctime()
