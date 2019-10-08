class Car:
    color = "" # class attribute or variable
    def description(self): # getter method....bound method of class car
        description_string = "This is a %s car." % self.color    # self is placeholder for object
        return description_string # this is a fruitful method or fn as it returns the description_string

car1 = Car()# declaring object/instance of class car
car2 = Car()# creating object of the class car

car1.color = "blue" # assigning the instance a value or declaring an instance variable
car2.color = 'red'# declaring another instance variable that overrides the class variabel that is an empty string

print(car1.description())
print(car2.description())
