import sys
try :
    ny = 'Statue of Liberty'
    my_list = [3, 4, 5, 8, 9]
    print  my_list + ny
except TypeError as e:
    print e
    print sys.exc_type