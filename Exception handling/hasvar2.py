x =10
class foo:
    g = 'rt'
    def sum(a,b):
        print (locals())
        if 'c' in locals ():
            print (' is local variable')
        else:
            print (' is not a local variable')
        return (a+b)
foo.sum(2,3)
print (globals())
f = foo()
if hasattr(f, 'g'):
    print ('is an attribute')
else:
    print ("is not an attribute")
if 'x' in globals ():
    print ('x is a global variable')