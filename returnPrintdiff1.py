def function_that_prints():  # function with print statement,
    # prints whatever is there but returns None
    print "I printed"


def function_that_returns():  # function with return st does not
    # print the result until print statement is used explicitly
    return "I returned"


f1 = function_that_prints()
f2 = function_that_returns()
f1
print f2
