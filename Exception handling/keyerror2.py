try:
    d = {1: 2, 3: 4}
    print d[ 5 ]
except KeyError as e:
    print e
