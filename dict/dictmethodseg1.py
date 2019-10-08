#examples of dict methods; d.clear() clears the list of all keys and values; d.copy() creates a shallow
#copy of the dict; d.get(k) gets the value corresponding to the key in the dict.
'''Method	Description
d['k'] fetches the corr value of the key of the dict d
d.has_key(k) returns true of false - this method removed from python 3.x....deprecated
k in d is better code to above returns true or false
d.clear()	Removes all Items
d.copy()	Returns Shallow Copy of a Dictionary
dict.fromkeys(l)	creates dictionary from given sequence/list l with all values as None
dict.fromkeys(l,v)	creates dictionary from given sequence/list l with all values as v
d.get(k)	Returns Value corr to The Key k
d.items()	returns view of dictionary's (key, value) pairs
d.keys()	Returns View Object of All Keys
d.popitem()	Returns & Removes an arbitrary element or(k,v) pair from the dictionary and takes no argument.
d.setdefault(k)	If key present returns corr value/Inserts Key With a None Value if Key is not Present
d.setdefault(k,v)If key is not present, inserts key with the value v
d.pop(k)	removes and returns element having given key; after this op the k,v pair are removed from d
d.pop(key[, default]) default is value which is returned when the key is not in the dictionary
d.values()	returns view of all values in dictionary
d.update()takes either a dictionary or an iterable object of key/value pairs (generally tuples)
It adds element(s) to the dictionary if the key is not in the dictionary. If the key is in the dictionary,
it updates the key with the new value..
any()	Checks if any Element of an Iterable is True
all()	returns true when all elements in iterable is true
ascii()	Returns String Containing Printable Representation
bool()	Converts a Value to Boolean
dict()	Creates a Dictionary
enumerate()	Returns an Enumerate Object
filter()	constructs iterator from elements which are true
iter()	returns iterator for an object
len()	Returns Length of an Object
max()	returns largest element
min()	returns smallest element
map()	Applies Function and Returns a List
sorted()	returns sorted list from a given iterable
sum()	Add items of an Iterable
zip()	Returns an Iterator of Tuples'''
d = {'a':1,'b':2}
d1 = {'a':1,'b':2}
#d.clear
d1.clear()
print d1
#d.copy()
d2 = d.copy()
print d2
#dict.fromkeys(l)
l= [1,'c',2,'d']
d3 = dict.fromkeys(l)
print d3
#dict.fromkeys(l,v)
d4 = dict.fromkeys(l, 6)
print d4
#d.items()
print d2.items()
#d.keys()
print d2.keys()
#d.values
print d2.values()
#d.get(k)
print d2.get('b')
#d[k]
print d2['a']
#d.has_key(k)
print d2.has_key('a')
# print(k in d)
print('a' in d2)
print('c' in d2)
#d.pop(k)
print d2.pop('a')
print d2
#d.update('a':1)
d2.update({'a':1,'c':3})
print d2
#d.popitem()
d2.popitem()
print d2
#d.setdefault(k) key is there
print d2.setdefault('c')
#d.setdefault(k);key is not there, inserts key with value None
print d2.setdefault('d')
print d2
#d.setdefault(k,v); key is not there, inserts key with value v
print d2.setdefault('e',5)
print d2