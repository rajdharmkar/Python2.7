import inspect
print "The class hierarchy for built-in exceptions is:"
inspect.getclasstree(inspect.getmro(BaseException))
def classtree(cls, indent=0):
    print '.' * indent, cls.__name__
    for subcls in cls.__subclasses__():
        classtree(subcls, indent + 3)

classtree(BaseException)
