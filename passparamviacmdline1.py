# a program to pass parameters via the command line to a script?
# shows value error if the script.py is executed at command line without parameters and should not be run in ide
import sys
from sys import argv
scriptname, first, second, third = argv  # unpacks upto 3 arguments at command line excluding the scriptname
print "The name of the script is :", scriptname
print "The name of the first argument is:", first
print "The name of the second argument is:", second
print "The name of the third argument is:", third
sys.version