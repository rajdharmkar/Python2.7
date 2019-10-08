def f2():

    for i in range(5):
        yield i*i

#yield creates a generator which is sort of iterable list but has parentheses in
#place of square brackets...not stored in memory...         
    
the_generator = f2()
for i in the_generator:
    print i
