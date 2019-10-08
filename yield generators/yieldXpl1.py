def f1():
    a = range(10000)
    return a
"""
    :rtype: object
"""
def f2():
    # type: () -> object
    b = range(10000)
    for i in range(10):
        yield b[1000*i : 1000*(i+1)]
f1()
f2()
#id(a) error