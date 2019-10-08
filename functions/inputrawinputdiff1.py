s = raw_input('Enter a string:') # raw_input always returns a string whatever input / whether 'foo'/foo/78/'78' are inputed
print s
print (type(s))
t = raw_input('Enter a int number:') # raw_input always returns a string whatever input / whether 'foo'/foo/78/'78' are inputed
print t
print (type(t))
u = raw_input('Enter a float number:') # raw_input always returns a string whatever input / whether 'foo'/foo/78/'78' are inputed
print u
print (type(u))
# n =int(raw_input(prompt))); returns an integer whatever input / this converts the input to an integer
m = input('Enter a string:')
print m
print (type(m))
n = input("Enter a int number':")# this takes only numbers and 'strings'; srings throw errors ..it also evaluates if any numeric expression is given
print n
print (type(n))
o = input("Enter a float number':")# this takes only numbers and 'strings'; srings throw errors ..it also evaluates if any numeric expression is given
print o
print (type(o))
p = input('Enter any numeric expression:')# if you enter for example 3+7*6 on prompt, input returns 45
print p
print (type (p))
#>>>type(raw_input('Enter a number:'))
#Enter a number:45
#<type 'str'>
#>>> type(input('Enter a number:'))
#Enter a number:yu
#Traceback (most recent call last):
#  File "<pyshell#3>", line 1, in <module>
#    type(input('Enter a number:'))
#  File "<string>", line 1, in <module>
#NameError: name 'yu' is not defined
#>>> type(input('Enter a number:'))
#Enter a number:56
#<type 'int'>
print(type(raw_input('Enter a string:')))
print(type(raw_input('Enter a integer number:')))
print(type(raw_input('Enter a float number')))
print(type(input('Enter a string:')))
print(type(input('Enter a int number')))
print(type(input('Enter a float number')))
