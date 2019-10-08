import logging
#logger = logging.Logger()
try:
     a = 7/0
     print float(a)
except BaseException as e:
    logging.exception('There is error: ' + str(e))
