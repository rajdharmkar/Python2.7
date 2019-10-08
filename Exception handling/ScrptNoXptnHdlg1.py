number = int(raw_input("Enter a number between 1 - 12:"))
print " The number entered:", number
# This program works perfectly as long as we enter a number, but let us see what happens if we put in something else like a string.
# Enter a number between 1 ? 12:
# ?hello?
# We see that the program throws us an error when we enter a string.
# Traceback (most recent call last):
#   File "enter_number.py", line 1, in
#     number = int(raw_input("Enter a number between 1 - 12
# "))
