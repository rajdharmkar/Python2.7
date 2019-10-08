s = raw_input('Enter a string:') # raw_input always returns a string whether 'foo'/foo/78/'78'
# n =int(raw_input(prompt))); this converts the input to an integer
n = input("Enter a number/'string':")# this takes only numbers and 'strings'; srings throw errors ..it also evaluates if any numeric expression is given
p = input('Enter any numeric expression:')# if you enter for example 3+7*6 on prompt, input returns 45
print s
print n
print p
print (type(s))
print (type(n))
print(type(n))
# getting NameError if in n we input a string without quotes /
#  wont get ValueError in this script which is getting type right but its value wrong for integer type if we input float