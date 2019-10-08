class P:
    def __init__(self, x): # init method
        self._x = x # could be equal to None

    @property # property is a special attribute of a class
    def x(self): # property method and setter method have same name ; example of method overloading
        return self._x

    @x.setter
    def x(self, x):
        #self._x = x
        if x < 0:
            self.__x = 0
        elif 0< x < 100:
            self.__x = 100
        else:
            self.__x = 1000
    @x.deleter
    def x(self):
        del self_x
p1 = P(1000)
p2 = P(-4)
p3 = P(67)
#p2 = P(_x, -7)# error
p1._x = 89
p2._x= -7
p3._x=101

print p1.x
print p2.x
print p3.x
print p1._x
print p2._x
print p3._x

#print p.x(); method not callable




