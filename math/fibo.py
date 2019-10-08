
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b, # comma in print statement acts like NOT newline , all numbers are printed in one line..a row of numbers
        #  without comma or anything everytime there is a new line; we get a column of numbers
        a, b = b, a+ b



def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result



# Executing modules as scripts
# ----------------------------
#
# When you run a Python module with ::
#
#    python fibo.py <arguments>
#
# the code in the module will be executed, just as if you imported it, but with
# the ``__name__`` set to ``"__main__"``.  That means that by adding this code at
# the end of your module::


if __name__ == "__main__":
    import sys

    fib ( int ( sys.argv[ 1 ] ) )

# you can make the file usable as a script as well as an importable module,
# because the code that parses the command line only runs if the module is
# executed as the "main" file::
#
#    $ python fibo.py 50
#    1 1 2 3 5 8 13 21 34

# If the module is imported, the code is not run::
#
#    >>> import fibo
#    >>>