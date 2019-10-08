import sys
def baz():
    try: 1/0
    except ZeroDivisionError, e:
        type, value, traceback = sys.exc_info()
        raise ValueError("You did something wrong!", type, value), traceback
baz()
#except Exception as e -> raise type(e), type(e)(e.message + custom_message), sys.exc_info()[2]-
