# In case if there is any code which the user want to be executed, whether exception occurs or not then that code can be
#  placed inside the finally block. Finally block will always be executed irrespective of the exception.
# # Syntax:
# # try:
#     Code
# finally:
#     code which is must to be executed.
try:
    a=10/0;
    print "Exception occurred" # IS IMPORTANT TO NOTE THAT EXCEPTION WAS NOT HANDLED AND EXECUTION STOPPED HERE
finally:
    print "Code to be executed"

# Code to be executed
# Traceback (most recent call last):
#   File "C:/Python27/noexception.py", line 2, in <module>
#     a=10/0;
# ZeroDivisionError: integer division or modulo by zero
# >>>
# In the above example finally block is executed. Since exception is not handled therefore exception occurred and execution
# is stopped.