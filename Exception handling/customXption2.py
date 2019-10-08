class ExampleException(Exception):
    def __init__(self, foo):
        self.foo = foo

try:
    raise ExampleException("Foo!")
except ExampleException as e:
    print e.foo
