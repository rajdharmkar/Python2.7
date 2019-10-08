#Example of multiple inheritance
class Base1:  
    pass  
  
class Base2:  
    pass  
  
class MultiDerived(Base1, Base2):  
    pass
class First(object):  
  def __init__(self):  
    super(First, self).__init__()  
    print("first")  
  
class Second(object):  
  def __init__(self):  
    super(Second, self).__init__()  
    print("second")  
  
class Third(Second, First):  
  def __init__(self):  
    super(Third, self).__init__()  
    print("third")  
  
Third();
#output below
#first  
#second  
#third  
