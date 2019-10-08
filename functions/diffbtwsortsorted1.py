#sort() is a list method, doesnot take an argument; syntax: list.sort()
#list.sort() returns a sorted list(but doesnot print)
#sorted(list)is a builtin function that returns a sorted list(does not print)
a = ['c','a','d','b']
b = [3,2,1,4]
print ('before sort(), the value of a = {}'.format(a))
print ('before sort(), the value of b = {}'.format(b))
a.sort()#sorts but doesnot print
print ('after sort(), the value of a = {}'.format(a))#prints sorted list
b.sort()#sorts but doesnot print
print ('after sort(), the value of b = {}'.format(b))#prints sorted list
#print (a.sort())-returns only None
#print(b.sort()): returns only None
c = ['d','a','c','b']
d = [5,2,3,4]
print ('before sorted(), the value of c = {}'.format(c))
c = sorted(c)
print ('after sorted(), the value of c = {}'.format(c))
e = [6,0,3]
print(sorted(e))
f = ['w','c','s','e']
print (sorted(f))