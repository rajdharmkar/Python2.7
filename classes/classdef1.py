class MyClass:
    var = 45 # class variable

    def foo(self):  # bound class method of MyClass that returns None cos there is no return statement in this method  # print("Hello from function foo")
        print("Hello from function foo")
    def bar(self):# is this a bound class method of MyClass?
        return 10


my_object = MyClass()  # variable "my_object" holds an object of the class "MyClass" that contains the variable 'var' and the "foo" function
print (my_object.var)# class variable accessed through the object using dot notation
#print (my_object.foo)#  a function call without parentheses that doesnot execute the print statement
print (my_object.foo())#  this is a function call thet executes the print statement and returns None as there is no return statement
print (my_object.bar())
