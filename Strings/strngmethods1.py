'''
capitalize()	Converts the only first character of the string with/without space to upper case
title() capitalizes the first letter of the string with space and substrings w
casefold()	not in py 2.x Converts string into lower case.Not there python 2.x only in py 3.x?
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	not in py 2.x Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''
a = 'manogna neelam'
b = raw_input('Enter any string:')
c = raw_input('Enter any char or substring1:')
d = raw_input('Enter any char or substring2:')
e = raw_input('Enter any separator:')
1#s.capitalize
z = a.capitalize()
print a.capitalize()#does not work
print '#1'+' '+(a.capitalize())# with parentheses this statement works
print '#2'+' '+ z#this ofcourse works
print '#3'+' '+(b.capitalize())
2#s.title()
print'#4'+' '+(a.title())
print '#5'+' '+(b.title())
#s.upper()
print'#6'+' '+(a.upper())
print'#7'+' '+(b.upper())
#s.upper()
print'#8'+' '+(a.lower())
print'#9'+' '+(b.lower())
#s.isupper()
print '#10',
print (a.isupper())
print '#11',
print (b.isupper())
#s.islow er()
print '#12',
print (a.islower())
print '#13',
print (b.islower())
#s.count()
print '#14',
print (a.count('o'))
print '#15',
print (a.count('n'))
print '#16',
print (a.count('e'))
print '#17',
print (b.count(c))
print '#18',
print (b.count(d))
#s.casefold()
#print(a.casefold())#not there in py 2.x only in py 3.x
#print(b.casefold())#not there in py 2.x only in py 3.x
#s.startswith()
print '#19',
print (a.startswith('m'))
print '#20',
print (a.startswith('o'))
print '#21',
print (b.startswith('c'))
print '#22',
print (b.startswith('d'))
#s.endswith()
print '#23',
print (a.endswith('a'))
print '#24',
print (a.endswith('m'))
print '#25',
print (b.endswith('c'))
print '#26',
print (b.endswith('d'))
#s.split()
print '#27',
print (a.split(' '))
print (b.split(e))
#s.strip()
print '#28',
#s.index()
print '#29',
#s.find()
print '#30',
#s.join()
print '#31',
print(' '.join('rama'))
print (e.join(b))
#s.swapcase()
print '#32',
#s.format()
print '#33',
#s.replace()
print '#34',
#s.isdigit()
print '#35',
#s.isnumeric()
print '#36',
#s.isalpha()
print '#37',
#s.isalnum()
print '#38',
#s.isdecimal()
print '#39',
#s.isspace()
print '#40',
#s.isidentifier()
