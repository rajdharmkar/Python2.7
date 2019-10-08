import sys
try:

   class Super(object):

        @property
        def example(self):
            raise NotImplementedError("Subclasses should implement this!")
   s = Super()
   print s.example
except Exception as e:
    print e
    print sys.exc_type