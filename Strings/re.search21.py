import re

# Get user's name
name = raw_input ( "Please enter name: " )

# While name has incorrect characters
while re.search ( '[^a-z0-9\n]', name ):
    # Print out an error
    print("illegal name - Please use only small case letters and 0-9 digits; no upper case letters")

    # Ask for the name again (if it's incorrect, while loop starts again)
    name = raw_input ( "Please enter name: " )
else:
    print "perfectly valid name"

