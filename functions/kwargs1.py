def greet_me(**kwargs):#kwargs is keyword arguments; what is key word here
    if kwargs is not None:
        for k,v in kwargs.iteritems():
            print "%s = %s" % (k, v)
            print "{0} = {1}".format(k,v)

greet_me(name="fmanu")#? what data structure? how dict with equal to
# sign instead of a colon sign

