def test_var_args(f_arg, *varargs):
    # first arg is normal args or required arguments whose order and number is important and they are mandatory
    # Then *argv (as varags in java) with a single asterisk indicates that we can have a list of arguments with variable number, not fixed number
    print "first required arg:", f_arg
    for i in varargs:
        print "another arg through *varargs is:", i
        # inline comment starting with hash should be two spaces short
        #  in print statement  no parentheses vers 2.7 in ver 3 print comes with parentheses it is a function not just a statement

test_var_args('manogna', 'babydoll', 'infatuate', 'neelam')  # in this function call one required arg and three varargs
test_var_args('raj', 'dharmkar', 'tutorialspoint', 'hyderabad', 'telangana',
              'india')  # here using one normal and 5 variable args or varargs
#  can have more than one required arguments as shown below
def test_reqrd_args(r_arg1, r_arg2, r_arg3, *varargs):
    print ' the first required arg is', r_arg1
    print ' the first required arg is', r_arg2
    print ' the first required arg is', r_arg3
    for i in varargs:
        print "another arg through *varargs :", i


test_reqrd_args('raj', 'dharmkar', 'kumar')# here there are no varargs
test_reqrd_args('raj', 'dharmkar', 'kumar', 'hyderabad','telangana',)
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('manumylove', 'python', 'eggs', 'test')
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="manumylove")#is this a dictionary with equal to sign?

