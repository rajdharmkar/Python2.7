class Animal:   
    def eat(self):  
      print 'Eating...'  
class Dog(Animal):#declaring the Dog class as child class by passing on Parent class name as parameter in child class parentheses    
   def bark(self):  
      print 'Barking...'  
d=Dog()  
d.eat()#eat is a method of parent Animal class, it is inherited by the child class Dog 
d.bark()  
