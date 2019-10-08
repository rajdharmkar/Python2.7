import sys

def throws():
    raise RuntimeError('this is the error message')

def main():
    try:
        throws()
        return 0
    except Exception, err:
        sys.stderr.write('ERROR: %sn' % str(err))
        return 1

if __name__ == '__main__':
    sys.exit(main())