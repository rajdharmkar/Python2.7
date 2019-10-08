# use of non-keyworded variable number of arguments *args and there is
#  no normal/required variable here
def multiply(*args):
    # type: (object) -> object
    #  this is example of annotation but what is it?
    """

    :rtype: object       rtype means return type?
    """
    #  above is an example of doc string having annotation?
    z = 1
    for i in args:
        z *= i #  same as z = z*i
    print z # print statement does not need to have a parentheses around a variable or identifier

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)
