def foo():
    try:
        raise Exception()
    except Exception as e:
        pass

    print (1)
    raise
    print (2)

if __name__ == '__main__':
    foo()