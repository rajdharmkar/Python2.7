d = {'a' : 1, 'b' : 2, 'c' : 3}

def f(x):
    for values in x.itervalues():
        print values

f(d)
