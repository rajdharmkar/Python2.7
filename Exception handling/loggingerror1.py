import logging
try:
    print 'toy' + 6
except Exception as e:
    logging.exception("This is an exception log")
