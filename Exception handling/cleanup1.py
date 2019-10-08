import sys

def throws():
    print 'Starting throws()'
    raise RuntimeError('this is the error message')

def main():
    try:
        try:
            throws()
            return 0
        except Exception, err:
            print 'Caught an exception'
            return 1
    finally:
        print 'In finally block for cleanup'

if __name__ == '__main__':
    sys.exit(main())