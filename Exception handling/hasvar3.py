x =10
class foo:
    g = 'rt'
    def bar(self):
        m=6
        print (locals())
        if 'm' in locals():
            print ('m is local variable')
        else:
            print ('m is not a local variable')

f = foo()
f.bar()
print (globals())
f = foo()

if hasattr(f, 'g'):
    print ('g is an attribute')
else:
    print ("g is not an attribute")
if 'x' in globals():
    print ('x is a global variable')
