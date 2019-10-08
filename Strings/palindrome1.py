#from __future__ import print_function
wordinput = input('Enter a word to check if it is a palindrome:')
def palindrome(x):
    if x == x[::-1]:#reverses the string iterable
        print ('The word entered is a palindrome')
    else:
        print ('It is NOT a palindrome')
palindrome(wordinput)
'''def palindrome2(x):
    s = list(x)
    s.reverse()
    s1 = s
    print s
    print s1
    if s == s1:
        print'yes'
    else:
        print'no'
palindrome2(wordinput)'''
def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    print ('original string = {}; reversed string is = {}'.format(s,s1),)
    if s == s1:
        print ('\n')
        print ('yes it is a palindrome')
    else:
        print ('no it is NOT a palindrome')
reverse_for_loop(wordinput)
def reverse_while_loop(s):
    s1 = ''
    i = len(s) - 1
    while i >=0:
        s1 = s1 + s[i]
        i -= 1
    print ('reversed string is {}'.format(s1,))
    if s == s1:
       print ('it is a palindrome')
    else:
        print ('it is not a palindrome')
reverse_while_loop(wordinput)
def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    print (s1)
reverse_join_reversed_iter(wordinput)
#print (reversed(wordinput))#printing memory address of reversed object without import of print function from the future
print (''.join(reversed(wordinput)))

#if you pass the name of a function (or any other reference to a function) to the Python print statement (old Python) or the print() function (Python3 and Python2 after any from future import print function has been processed) if you do this then youll see the object ID of that function (its address in the reference C implemntation of the language).

#This is because that is the default string representation for all objects under Python.

#To get a value from any Python function (or method) you need to invoke the function by passing it an argument list (in parentheses). This is true even if your function takes no arguments. So for example a function such as:

#def foo():
#    return 42
#would be invoked as foo(). Youd print the value returned by that function using print(foo()) (under Python3 or after importing the print function from the future  module in older versions of Python).

#Understand this distinction, between reference and invocation, is one of the most fundamental skills which much be mastered by programmers in just about any programming language. Its specially important in using Python, Ruby, Javascript, and any modern scripting or programming languages which support function references as first class objects (values which can be passed around like data).
