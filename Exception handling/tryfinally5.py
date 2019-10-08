try:
    fob = open ( 'test.txt', 'w' )
    fob.write ( "It's my test file to verify try-finally in exception handling!!"
                )
    print 'try block executed'
finally:
    fob.close ()
    print 'finally block executed'
