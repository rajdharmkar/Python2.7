# -*- coding: utf-8 -*-
'''Python Remove Character from String
Using string replace() function
Using string translate() function
Python Remove Character from String using replace()
We can use string replace() function to replace a character with
a new character. If we provide an empty string as the second argument,
then the character will get removed from the string.
Note that the string is immutable in Python, so this function will
return a new string and the original string will remain unchanged.
s = 'abc12321cba'
print(s.replace('a', ''))
Output: bc12321cb
Python Remove Character from String using translate()
Python string translate() function replace each character in the string
using the given translation table. We have to specify the Unicode code
point for the character and None as a replacement to remove it from
the result string. We can use ord() function to get the Unicode code
point of a character.
s = 'abc12321cba'
print(s.translate({ord('a'): None}))
Output: bc12321cb
If you want to replace multiple characters, that can be done easily
using an iterator. Let’s see how to remove characters (‘a’, ‘b’ and ‘c’)
from a string.
s = 'abc12321cba'
print(s.translate({ord(i): None for i in 'abc'}))
Output: 12321
Removing Spaces from a String
s = ' 1 2 3 4 '
print(s.replace(' ', ''))  # 1234
print(s.translate({ord(i): None for i in ' '}))  # 1234
Python Remove newline from String
s = 'ab\ncd\nef'
print(s.replace('\n', ''))
print(s.translate({ord('\n'): None}))
Remove substring from string
String replace() function arguments is string. Let’s see how to remove
a word from a string.
s = 'ab12abc34ba'
print(s.replace('ab', ''))
Output: 12c34ba
Remove specified number of times
We can also pass a third parameter in replace() function to specify the
 number of times replacement should be performed.
s = 'abababab'
print(s.replace('a', 'A', 2))
Output: AbAbabab'''
a=raw_input('Enter a string:')
b=raw_input('Enter a substring or char to remove/replace:')
c=raw_input('Enter a substring or char to replace the old one:')
print(a.replace(b,''))#this command remove the char or substring
print(a.replace(b,c))