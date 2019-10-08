x = "hello"
class Foobar:
    def __init__(self, who):
        self.i = who
    def welcome(self):
        y = "%s, %s" % (x, self.i)
        return y

foo = Foobar("world")
print foo.welcome()
print foo.i
