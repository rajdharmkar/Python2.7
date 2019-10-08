try:
    foo = open ( 'test.txt', 'w' )
    foo.write ( "It's a test file to verify try-finally in exception handling!!")
    print 'try block executed'
finally:
    foo.close ()
    print 'finally block executed'

