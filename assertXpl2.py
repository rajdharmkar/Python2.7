class B: # class declaration with keyword class, class object B created
    # class object; instance object; function object; method object
      x = 10 # this is a class attribute
      def __init__(self, name): # this is a __init__ method, also called a constructor that initializes default values of instance
          # attributes ;  self refers to the instance object
          self.name = name
      '''B.x is a class attribute'''
      @property # using property decorator...property is a special kind of class attribute?
      def foo(self): # this is a declaration of  instance method?
          """
          B.x is a property
          This is the getter method
          """
          print self.x

       #@bar.setter
      def bar(self, value):
          """
          This is the setter method
          where we can check if it's not assigned a value < 0
          """
          if value < 0:
             raise ValueError("Must be >= 0")
          self.x = value
b = B('harris')# creation or instantiation of class into a instance object with parentheses after classname like function call
print b.name # accessing and printing an instance attribute
print B.x # accessing and printing an class attribute
print b.x # accessing a class attribute from instance?
print B.__dict__ # prints dictionary of class attributes
#print B.__dict()
print b.__dict__# prints dictionary of instance attributes
#print(b.foo()); foo not callable?
print b.foo # no need for parentheses for b.foo prints self.x which is obj.x = 10 and None?
#print b.bar(); parentheses cant be empty and unfilled; takes 1 arg
print b.bar(100)# returning None yes and 100 assigned to self.x or obj.x or b.x so print b.x prints 100
print b.x
#b.bar(-1)# raises valueError
print b.bar(-1) # raises no valueError...print statement without parentheses
print (b.bar(-1))# raises valueError
#b.x = -1
# Traceback (most recent call last):
#   File "C:/Users/TutorialsPoint1/PycharmProjects/TProg/assertXpl2.py", line 22, in <module>
#     b.x = -1
#   File "C:/Users/TutorialsPoint1/PycharmProjects/TProg/assertXpl2.py", line 19, in x
#     raise ValueError("Must be >= 0")
# ValueError: Must be >= 0
