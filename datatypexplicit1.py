def add(x, y):
    z = float ( x ) + float ( y )
    print "The required Sum is:  {}".format ( z )
    return z

    def add(x, y):
        z = float ( x ) + float ( y )
        print "The required Sum is:  {}".format ( z )
        return z


print add ( 5, 8 )


# If a & b are strings
def add(x, y):
    try:
        a = float ( x )
        b = float ( y )
    except ValueError:
        return None
    else:
        return True
print add( 'Hi', 'Hello' )

def addSum(x, y):
    return x + y


print addSum ( 2.2, 5.6 )
print addSum ( float ( 2 ), float ( 5 ) )
print addSum ( 2, 5 )
print addSum ( 'Hi', 'Hello' )


