class Student:  
   def __init__(self, rollno, name):  
      self.rollno = rollno  
      self.name = name  
   def displayStudent(self):  
      print "rollno : ", self.rollno,  ", name: ", self.name  
emp1 = Student(121, "Ajeet")#creating class object with two parameters/attributes  
emp2 = Student(122, "Sonoo")#do  
emp1.displayStudent()#calling function of object  
emp2.displayStudent()#do  
