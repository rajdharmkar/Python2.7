# reverse() is a list method, doesnot take an argument; syntax: list.reverse()
# list.reverse() returns a reverseed list(but doesnot print)
# reverseed(list)is a builtin function that returns a reverseed list(does not print)
a = ['c', 'a', 'd', 'b']
b = [3, 2, 1, 4]
print('before reverse(), the value of a = {}'.format(a))
print('before reverse(), the value of b = {}'.format(b))
#a.reverse();#Nonetype object
type(a.reverse())#returns None
a.reverse()  # reverses but doesnot print
print('after reverse(), the value of a = {}'.format(a))  # prints reverseed list
b.reverse()  # reverses but doesnot print
print('after reverse(), the value of b = {}'.format(b))  # prints reverseed list
print(a.reverse())  # returns only None
# print(b.reverse()): returns only None;unprintable object
c = ['d', 'a', 'c', 'b']
d = [5, 2, 3, 4]
print('before reversed(), the value of c = {}'.format(c))
# print(reversed(c))#list_iterator object showing memory address, doesnot print
print('after reversed(), the value of c = {}'.format(list(reversed(c))))
e = list(reversed(c))
print('after reversed(), the value of c = {}'.format(e))
f = [6, 0, 3]
print(reversed(f))#only print mem address of obj; prints only list(reversed(obj))
g = ['w', 'c', 's', 'e']
print('before reversed(), the value of g = {}'.format(g))
print('after reversed(), the value of c = {}'.format(list(reversed(g))))
h = list(reversed(g))
print('after reversed(), the value of g = {}'.format(h))
