#class Complex:
 #   def create(self, real_part, imag_part):
   #     self.r = real_part
  #      self.i = imag_part
import sys
class Calculator:
    current = int(sys.argv[1])# class variable being assigned int value from command line

    def add(self, amount): # class method
        self.amount = amount
        self.current += amount


    def get_current(self): # class method
        return self.current
c = Calculator()# c is an instance of class
c.add(int(sys.argv[2]))# calling add method with command line arg
print (c.get_current())
