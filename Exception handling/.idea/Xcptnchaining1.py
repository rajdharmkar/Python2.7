try:
    v = {}['a']
except KeyError as e:
    raise ValueError('failed') from e