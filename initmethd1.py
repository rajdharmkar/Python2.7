class Human:
    # def __init__(self): pass #  init method initializing instance variables
    #
    # def __str__(): pass # ??
    #
    # def __del__(self): pass # ??...these three def statements commented out using code>> comment with line comment..toggles

    def __init__(self, name, age, gender):  # self means object in the init method inline comment example
        # type: (object, object, object) -> object
        self.name = name  # creating and assigning new variable
        self.age = age
        self.gender = gender

    def speak_name(self):  # a method defined here with a print statement to execute as well
        print "my name is %s" % self.name

    def speak(self, text):
        # def speak(text):; without self, we get nameerror...speaks take exactly one argument given two given; gave one arg but self is implied so two counted as given
        print text

    def perform_math(self, operation, *args):
        print "%s performed math and the result was %f" % (self.name, operation(*args))

def add(a, b):#this is an example of function not an object method and is callable everywhere
    return a + b


rhea = Human('Rhea', 20, 'female')
bill = Human('William', '24',
             'male')  # creating new object 'bill' which is an instance of class Human with variables assignment as well
#  getting saying bill is not defined
print bill.name
print bill.age
print bill.gender
bill.speak_name()
bill.speak("Love")
rhea.perform_math(add, 34,45)
# method speak_name belongs to object 'bill' here; a method call?
#  method diff from function and it can be called only from the object and it bound to the class
