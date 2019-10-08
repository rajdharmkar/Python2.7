# There is exceptions moodule but no exception module but there is Exception class which is the base call for many other exceptions

import sys
try:
    from exception import myexception

except Exception as e:
    print e
    print sys.exc_type