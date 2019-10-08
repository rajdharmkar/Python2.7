# import sys
# import logging
#
# logger = logging.Logger('catch_all')
#
# def catchEverythingInLog():
#     try:
#         a = 'sequel'
#         b = 0.8
#         print a + b
#        # ... do something ...
#     except Exception as e:
#         logger.error(e, sys.exc_info())
#         #... exception handling ...
# catchEverythingInLog()
# This is now the old way (though still works):
#
import sys, traceback

def catchEverything():
    try:
        a = 'sequel'
        b = 0.8
        print a + b
    except Exception as e:
        print sys.exc_info()
       # exc_type, exc_value, exc_traceback = sys.exc_info()
catchEverything()
        #... exception handling ...
#exc_value is the error message.