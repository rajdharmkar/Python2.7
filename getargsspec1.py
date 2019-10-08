#example of how to extract names and numbers of args/params of a given function
import inspect# importing inspect module
def aMethod(arg1, arg2):
    pass
def foo(a,b,c=4, *arglist, **keywords):
    pass
#def main(arg1, arg2): no effect    
    pass
#inspect.getargspec(main); no effect
#inspect.getargspec(aMethod)#how to execute this here rather than at prompt
'''
output
(['arg1', 'arg2'], None, None, None)
'''
