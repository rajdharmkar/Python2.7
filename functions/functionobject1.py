class Huluhulu:
    def __init__(self, age, name, gender):
            self.name = name
            self.age = age
            self.gender = gender
    def foo(self):
        print self.age, self.name, self.gender
h1 = Huluhulu(23, 'Joe', 'Male')
h2 = Huluhulu(27, 'Jane', "Female")

print h1.age
print h2.gender
print h1.foo()
print h2.foo()


