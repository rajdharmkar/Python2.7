# program to show that two arguments declared in definition of function are REQUIRED ARGUMENTS. If one or more of these not passed, error is shown
def requiredArg(str, num):
    print str, num
requiredArg('Hello')
# Traceback (most recent call last):
#   File "C:/Users/TutorialsPoint1/PycharmProjects/TProg/rqurd_args2.py", line 3, in <module>
#     requiredArg('Hello')
# TypeError: requiredArg() takes exactly 2 arguments (1 given)
# Process finished with exit code 1