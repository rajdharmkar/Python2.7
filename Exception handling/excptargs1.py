try:
    raise ValueError('foo', 23)
except ValueError, e:
     print e.args
