try:
    i = input( "Enter a string: " )
    if not isinstance(i, basestring):
       raise ValueError ( "This is not a string" )

except ValueError as e:
    print(e)
