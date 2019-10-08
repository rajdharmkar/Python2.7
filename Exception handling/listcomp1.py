foo = (5,7,1,0,9)
def bar(self):
    try:
        return [1/i for i in foo]
    except ZeroDivisionError as e:
               print e
bar(foo)
