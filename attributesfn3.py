def foo():
    name = 'bar'
    print name
foo()
setattr(foo, 'age', 23 )
print(foo.age)
print(getattr(foo,'age'))
foo.gender ='male'
print(foo.gender)

