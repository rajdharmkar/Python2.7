import re

# Get user's name
name = raw_input ( "Please enter name: " )

# While name has incorrect characters
while re.search ( '[^a-zA-Z\n]', name ):
   # Print out an error
    print("illegal name - Please use only letters")
    name = raw_input ( "Please enter a valid name: " )
#Ask for the name again (if it's incorrect, while loop starts again)
#   print"Perfectly valid name" 
