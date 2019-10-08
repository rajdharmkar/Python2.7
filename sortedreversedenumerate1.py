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