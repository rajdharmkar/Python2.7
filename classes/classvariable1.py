class MyClass:
    variable1 = 1# class variables declared inside the class
    variable2 = 2# do

    def foo(self):     # class bound method of MyClass and self is placeholder of object
        print("Hello from function foo")

my_object1 = MyClass()# instantiating MyClass as objects
my_object2 = MyClass()# do

my_object2.variable2 = 3   # changes value stored in variable2 this assignment makes it an instance variable that
# overrides the value of the class variable

print(my_object1.variable2)
print(my_object2.variable2)

my_object1.foo()   # call method foo() of object my_object1
my_object2.foo()   # call method foo() of object my_object2
print(my_object1.variable1)
print(my_object2.variable1)
my_object1.foo()
