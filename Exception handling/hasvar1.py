x =10
class foo:
    g = 'rt'
    def sum(a,b):
        print (locals())# locals() function has to be within the local scope/methods to show the local variables, cant be invoked at top level
        #locals() returns a dictionary of k,v pairs of local_variables, values
        if 'c' in locals ():
            print (' is local variable')
        else:
            print (' is not a local variable')
        return (a+b)

print (globals())# globals(0 function should be invoked at the top level or global scope; it also returns a dictionary of key value pairs
#globals() is writable unlike locals() which is readonly
print (foo.sum(5,9))
print (foo.sum(8,12))
f = foo()
print (f.g)
if hasattr(f, 'b'):
    print ('true')
else:
    print ("false")
if 'x' in globals ():
    print ('x is a global variable')