def add(x, y):
        z = float(x)+ float(y)
        print "The required Sum is:  {}".format(z)
        return z

add (5, 8)
#If a & b are strings 

def add(x, y):
    try:
        a = float(x)  
        b = float(y)
    except ValueError:
        return None
    else:
        return True
#By the way, No need to check the datatype in python, making it much simpler

def addSum(x,y):
    return x+y

addSum(2.2, 5.6)
7.8
addSum(float(2), float(5))
7.0
addSum(2, 5)
7
addSum("Hello ", "World!!")
'Hello World'
