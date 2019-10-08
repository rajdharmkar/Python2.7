#
def square(x):
    return x * x

if __name__ == '__main__':
    print "test: square(42) ==", square(42)
    square(20)# doesnot print as it is an object
    print square(20)  


