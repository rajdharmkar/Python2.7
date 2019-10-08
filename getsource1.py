#getting source code of an object
#getsource(object) wrong command
import inspect#import statement has to be there even if the function is called at prompt
class foo:
      def bar():
          print 'Hello'
#inspect.getsourcelines(foo); working at py prompt
#inspect.getsourcelines(bar); cannot get code at function level only at class or module level?
#inspectgetsource(foo); working at py prompt
#inspect.getsource(bar); not working at py prompt also
