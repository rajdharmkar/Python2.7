class FooException(Exception):
    def __init__(self, text, *args):
        super ( FooException, self ).__init__ ( text, *args )
        self.text = text
try:

     bar = input("Enter a string:")
     print bar
     print (type (bar))
     if not isinstance(bar, basestring):
        raise FooException(bar)
except FooException as r:
       print 'there is an error'
       print type(r)
       print str(r)