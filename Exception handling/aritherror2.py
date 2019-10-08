try:
    a = 0 / 19
    print a
except ArithmeticError:
    print "This statement is raising an exception"
else:
    print "Welcome"

#syntax
#
# try:
#     #run code
# except exception/error name1:
#         #run code
# except exception error name2:
#        # run code
# else:
#     # run code