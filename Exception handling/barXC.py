import fooXC

class BarException(Exception):
    pass

def a():
    b()

def b():
    c()

def c():
    try:
        fooXC.d()
    except fooXC.FooException as e:
        raise BarException(e)