def FooObject():
    def test():
        print "bar"
    FooObject.test = test
    return FooObject
x = FooObject()
x.test()

