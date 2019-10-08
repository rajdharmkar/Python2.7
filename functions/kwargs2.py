def print_kwargs(**kwargs):
           print(kwargs)#the keyworded var pairs are printed as a dictionary of same pairs

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
foo = {'kwargs_1':"Shark", 'kwargs_2':4.5, 'kwargs_3':True}
print_kwargs(**foo)