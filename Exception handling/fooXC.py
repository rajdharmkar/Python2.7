class FooException(Exception):
    pass

def d():
    e()

def e():
    f()

def f():
    raise FooException("There's some problem ...")