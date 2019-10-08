import re

# Get user's name
number = raw_input ( "Please enter a number: " )

# While name has incorrect characters
while re.search ( '[^0-9\n]', number):
    # Print out an error
    print("illegal number - Please use only digits 0-9. No letters allowed")

    # Ask for the name again (if it's incorrect, while loop starts again)
    name = raw_input ( "Please enter name: " )