A = ['a', 1, 'b', 2, 'c', 3]
B = {'a': 1, 'b': 2, 'c': 3}
x = [ ]


def f(list):
    for i in list:
        print i,
        x.append ( i )


f(A)
print "\n",x
x = [ ]
f(B)
#print "\n"
#print x
print "\n",x
