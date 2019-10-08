def wrapper1(func, *args): # with star
    func(*args)

def wrapper2(func, args): # without star
    func(*args)
'''     func(*args)
The * next to args here means "take this list called
args and 'unwrap' it into the rest of the parameters.'''
def func2(x, y, z):
    print x+y+z

wrapper1(func2, 1, 2, 3)
wrapper2(func2, [1, 2, 3])
