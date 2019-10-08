class Student:  
   def __init__(self, rollno, name):  
      self.rollno = rollno  
      self.name = name  
   def displayStudent(self):  
      print "rollno : ", self.rollno,  ", name: ", self.name  
stud1 = Student(121, "Ajeet")#creating class object with two parameters/attributes  
stud2 = Student(122, "Sonoo")#do  
stud1.displayStudent()#calling function of object  
stud2.displayStudent()#do  
