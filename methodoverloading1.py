class Human:
     def sayHello(self, name=None):
         if name is not None:
            print 'Hello ' + name
         else:
            print 'Hello '
 # Create instance
obj = Human()
 # Call the method
obj.sayHello()
 # Call the method with a parameter
obj.sayHello('Rambo')
#obj.sayHello('Run', 'Lola');TypeError takes at most 2 args given 3 args
#obj.sayHello('Run', 'Lola', "Run"); TypeError takes at most 2 args given 4 args
'''Output:
Hello 
Hello Rambo
To clarify method overloading, we can now call the method sayHello() in two ways:
obj.sayHello()
obj.sayHello('Rambo')'''
