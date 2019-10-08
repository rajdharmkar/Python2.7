class foo:
    def createName(self, name):# this class has three methods createName, displayName, sayName
        self.name = name#method createName has two variables self and name

    def displayName(self):
        return self.name # return statement doesnot print..the value is there for use
        #  but it needs an explicit print statement for display
    def sayName(self):
        print 'say hi to %s' % self.name  # there is no comma in between

a = foo() #instance of class foo with parentheses?
b = foo() #do
a.createName('bucky')#assigning name, a local variable
b.createName('manu')#assignming name, a local variable
print a.displayName()
print b.displayName()

a.sayName()
b.sayName()