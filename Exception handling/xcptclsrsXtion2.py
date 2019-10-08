def foo():
    try:
        0 / 0
    except:
        pass

try:
    x = bar
except:
    foo()
    raise
# here the error in first code get precedence and the exception in except clause gets ignored  why