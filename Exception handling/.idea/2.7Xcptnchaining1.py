#Here is an example to illustrate the __context__ attribute:

def compute(a, b):
    try:
        a/b
    except Exception, exc:
        log(exc)

def log(exc):
    file = open('logfile.txt')  # oops, forgot the 'w'
    print >>file, exc
    file.close()