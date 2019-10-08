import sys
def catchEverything():
    try:
        a = 'sequel'
        b = 0.8
        print a + b
    except Exception as e:
        print sys.exc_value
catchEverything()
