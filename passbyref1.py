def try_to_change_list_contents(the_list):
    print 'got', the_list
    the_list.append('four')
    print 'changed to', the_list

outer_list = ['one', 'two', 'three']

print 'before, outer_list =', outer_list

try_to_change_list_contents(outer_list)
print 'after, outer_list =', outer_list
''' Since the parameter passed in is a reference to outer_list, not a copy of
it, we can use the mutating list methods
to change it and have the changes reflected in the outer scope.'''
