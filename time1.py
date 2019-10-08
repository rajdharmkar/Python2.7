#!/usr/bin/python
import time#time module's methods t.ctime(),t.sleep(seconds) example

print "Start : %s" % time.ctime()
time.sleep( 5 )
print "End : %s" % time.ctime()
print "Start :{}".format(time.ctime())
time.sleep( 10 )
print "End :{}".format(time.ctime())