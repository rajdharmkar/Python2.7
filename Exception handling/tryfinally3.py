try:
    fob = open('test.txt', 'r')
    try:
        fob.write("It's my test file to verify try-finally in exception handling!!"
                  )
        print 'try block executed'
    finally:
        fob.close()
        print 'finally block executed to close the file'
except IOError:
    print "Error: can\'t find file or read data"

