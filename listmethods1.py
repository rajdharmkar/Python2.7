foo = ['a',1,2, 'b', 'c',3]
#list methods are append(o),count(o), extend(iterable), sort(),insert(i,o),remove(o),
# reverse(),index(o), pop(i)
#l.append(o), appends the object to the list
#l.extend(iterable);o.pop(i)-returns the obj at the index
#l.count(o)counts the number of times the object occurs in the list;l.sort();l.reverse();
#l.insert(i,o) inserts the object at the index;l.remove(o), removes the object from the list
#l.index(o) gives the index of the object in the list
foo.append(5)
print foo
foo.append('e')
print foo
foo.extend([1,2])
print foo
foo.sort()
print foo
print(foo.count(2))
print(foo.count('c'))
foo.reverse()
print foo
print(foo.index(5))
foo.insert(0,7)
print foo
print(foo.pop(1))
foo.remove(7)
print foo

