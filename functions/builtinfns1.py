'''
         BUILT-IN PYTHON FUNCTIONS
abs()	returns absolute value of a number
bin()	converts integer to binary string
bytearray()	returns array of given byte size
bytes()	returns immutable bytes object
callable()	Checks if the Object is Callable
chr()	Returns a Character (a string) from an Integer
classmethod()	returns class method for given function
compile()	Returns a Python code object
complex()	Creates a Complex Number
delattr()	Deletes Attribute From the Object
dict()	Creates a Dictionary
dir()	Tries to Return Attributes of Object
divmod()	Returns a Tuple of Quotient and Remainder
enumerate()	Returns an Enumerate Object
eval()	Runs Python Code Within Program
exec()	Executes Dynamically Created Program
filter()	constructs iterator from elements which are true
float()	returns floating point number from number, string
format()	returns formatted representation of a value
frozenset()	returns immutable frozenset object
getattr()	returns value of named attribute of an object
globals()	returns dictionary of current global symbol table
hasattr()	returns whether object has named attribute
hash()	returns hash value of an object
help()	Invokes the built-in Help System
hex()	Converts to Integer to Hexadecimal
id()	Returns Identify of an Object
input()	reads and returns a line of string
int()	returns integer from a number or string
isinstance()	Checks if a Object is an Instance of Class
issubclass()	Checks if a Object is Subclass of a Class
iter()	returns iterator for an object
len()	Returns Length of an Object
list() Function	creates list in Python
locals()	Returns dictionary of a current local symbol table
map()	Applies Function and Returns a List
memoryview()	returns memory view of an argument
next()	Retrieves Next Element from Iterator
object()	Creates a Featureless Object
oct()	converts integer to octal
open()	Returns a File object
ord()	returns Unicode code point for Unicode character
pow()	returns x to the power of y
print()	Prints the Given Object
property()	returns a property attribute
range()	return sequence of integers between start and stop
repr()	returns printable representation of an object
reversed()	returns reversed iterator of a sequence
round()	rounds a floating point number to ndigits places.
set()	returns a Python set
setattr()	sets value of an attribute of object
slice()	creates a slice object specified by range()
sorted()	returns sorted list from a given iterable
staticmethod()	creates static method from a function
str()	returns informal representation of an object
sum()	Add items of an Iterable
super()	Allow you to Refer Parent Class by super
tuple() Function	Creates a Tuple
type()	Returns Type of an Object
vars()	Returns __dict__ attribute of a class
zip()	Returns an Iterator of Tuples
__import__()	Advanced Function Called by import
int()
str()
float()
list()
any()	Checks if any Element of an Iterable is True
all()	returns true when all elements in iterable is true
ascii()	Returns String Containing Printable Representation
bool()	Converts a Value to Boolean
dict()	Creates a Dictionary
enumerate()	Returns an Enumerate Object; index and corr items of list/iterable
filter()	constructs iterator from elements which are true
iter()	returns iterator for an object
len()	Returns Length of an Object
max()	returns largest element
min()	returns smallest element
map()	Applies Function and Returns a List
sorted()	returns sorted list from a given iterable
sum()	Add items of an Iterable
zip()	Returns an Iterator of Tuples'''
a = ['c',1,'b',3,'a',2]
b = ['c', 'a','b' ]
y = 'sprinkle'
z= [1,2,3,4,5]
#print(a.sorted());  sorted() is a builtin function and not a list method
#print(sorted(a))#TypeError: '<' not supported between instances of 'int' and 'str'
print(sorted(b))
print (a)#list remains unchanged after sorted() operation
#print reversed(a); printing only mem address
#print (reversed(a)); printing only mem address
#b = reversed(a);  printing only mem address
#print b; printing only mem address
for i in sorted(b):
    print (i,end=' ')
    print(list(i),end=' ')
print ('\n')

for i in reversed(a):# reversed() is a builtin function and not a list method
    print (i,end = ' ')
print ('\n')
print (list(reversed(a)))
print ('\n')
print (list(sorted(b)))# both print sorted(a) and print list(sorted()) same result
for i,v in enumerate(a):
    print (i,v,end = " ")
print ('\n')
for i,v in enumerate(y):
    print (i,v)
print('\n')
print (min(z))
print (max(z))
print (sum(z))