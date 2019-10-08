def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)

outer_list = ['we', 'like', 'proper', 'English']

print('before, outer_list =', outer_list)
try_to_change_list_reference(outer_list)
print('after, outer_list =', outer_list)
'''Since the the_list parameter was passed by value, assigning a new list
to it had no effect that the code outside the method could see. The the_list
was a copy of the outer_list reference, and we had the_list point
to a new list, but there was no way to change where outer_list pointed. '''
