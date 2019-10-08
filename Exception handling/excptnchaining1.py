try:
    s = {'a':1,"b":2}['c']
except KeyError as e:
    raise ValueError('failed') from e

