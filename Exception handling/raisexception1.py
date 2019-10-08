# Raise an Exception:
# # You can explicitly throw an exception in Python using ?raise? statement. raise will cause an exception
# to occur and thus execution control will stop in case it is not handled.
# # Syntax:
# # raise Exception_class,<value>
# eg:
# # try:
#     a=10
#     print a
#     raise NameError("Hello")
# except NameError as e:
#         print "An exception occurred"
#         print e
# Output:
#  10
# An exception occurred
# Hello
# >>>
# Explanation:
# # i) To raise an exception, raise statement is used. It is followed by exception class name.
# # ii) Exception can be provided with a value that can be given in the parenthesis. (here, Hello)
# # iii)	To access the value "as" keyword is used. "e" is used as a reference variable which stores the value of
#  the exception.
try:
    a=10
    print a
    raise NameError("Hello")
except NameError as e:
        print "An exception occurred"
        print e