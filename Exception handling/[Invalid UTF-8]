import sys, traceback

def main():
    try:
        9/0
    except ZeroDivisionError:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()