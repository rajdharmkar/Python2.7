class Square:#class name always starts with a uppercase letter
    side =3# class variable valid across all objects of this class
    def __init__(self):    # special method __init__
        self.sides = 4 # assignmemt to instance variable in init method same as obj.sides = 4

square = Square()# class instance/object created...
print(square.sides)# accessing the instance variable value

print (Square.side)#accessing class variable
class Car:
    def __init__(self, color):# color is an instance variable
        self.color = color

car = Car("blue")    # Note: you should not pass self parameter explicitly, only color parameter

print(car.color)
