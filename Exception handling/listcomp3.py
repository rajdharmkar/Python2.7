foo = [5,7,1,0,9]
a= []
#def bar():
try:
    for i in foo:
      if i==0:
         raise ZeroDivisionError
      else:
        [a.append(1/i) ]
        print a
except ZeroDivisionError as e:
     print e

