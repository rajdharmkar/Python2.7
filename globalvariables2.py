''' What happened? Why is the value of x 123 for the second print statement? It
turns out that when we assigned the value 321 to x inside foo we actually declared a
new variable called x in the local scope of that function. That x has absolutely no
relation to the x in global scope. When the function ends, that variable with the value
of 321 does not exist anymore.To get the desired effect, we have to use the global keyword. '''
x = 123
 
def foo():
    x = 321
    print(x)
 
foo()
print(x)
