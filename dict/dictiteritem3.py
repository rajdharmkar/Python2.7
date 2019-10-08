d = {'a' : 1, 'b' : 2, 'c' : 3}

def f(x):
    for k, v in x.iteritems(): #  this also works
        print k, 2*v

f(d)
