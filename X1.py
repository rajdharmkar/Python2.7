#Class MyClass:# has to be class not Class keyword
#class MyClass:
    #*Raj programs* error
#    ''' doc string'''#doc string
#    a = 50
#    def func(self):
#    def func(self):
#        print("Hello Raj!")

#MyClass.a

#MyClass.func(); showing Typeerror unbound method func()
#MyClass.func(); # Typeerror unbound method func() raj not defined
#func(MyClass) error func not defined
class MyClass:
    ''' doc string'''#doc string
    a = 50
    def func(self):#class bound method
        print("Hello Raj!")
obj = MyClass()#creating an obj instance of the class
#obj.a; working at interpreter prompt
#obj.func; working at interpreter prompt...showing mem location
#obj.func(); working at interpreter prompt and printing Hello Raj
#Here, attributes may be data or method. Method of an object is corresponding functions of that class.
#For example: MyClass.func is a function object and ob.func is a method object.
