# How to pass an argument to an exception when rsised  and retrieve it when excepted
#Give its constructor an argument, store that as an attribute, then retrieve it in the except clause
class FooException(Exception):
    def __init__(self, foo):
        self.foo = foo

try:
    raise FooException("Foo!")
except FooException as e:
    print e.foo