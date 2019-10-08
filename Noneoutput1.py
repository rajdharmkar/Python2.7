#Example of void function as no return statement print lyrics() prints None
def lyrics():
    print "First line"
lyrics()#prints First line..function call
lyrics#without parentheses...still prints First line..function call without parentheses
print lyrics()#prints None why? because no return statement
print lyrics#this prints the memory address of lyrics
a = lyrics()# prints First line
print a# for a void function print lyrics() gives None while as obj 'a' created
         # for lyrics(), print a works gives None as well
