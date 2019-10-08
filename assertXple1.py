class MyObject(object):
    # This is a normal attribute
    foo = 1
    @property
    def bar(self):
         return self.foo
    @bar.setter
    def bar(self, value):
        self.foo = value
obj = MyObject()
assert obj.foo == 1
assert obj.bar == obj.foo
obj.bar = 2
assert obj.foo == 2
assert obj.bar == obj.foo
