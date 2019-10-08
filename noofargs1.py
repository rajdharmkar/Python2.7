import inspect
def aMethod(arg1, arg2):
     pass
def aMethod1(neelam, manogna):
     pass
x=inspect.getargspec(aMethod1)
aMethod(5, 'manogna')
print(x)
print(x[0])
print(len(x[0]))
print(len(x))
#ArgSpec(args=['arg1', 'arg2'], varargs=None, keywords=None, defaults=None)
#def foo(fvar, *varargs, **kwargs):
#    pass
