import sys
print "Lets fix the previous code with exception handling"
try:
    number = int(raw_input("Enter a number between 1 - 12"))
except ValueError:
    print "Error.. enter numbers only"
    sys.exit()
print "you entered number", number
