# Program to filter out only the even items from a list
'''The filter() function in Python takes in a function and a list as arguments.
The function is called with all the items in the list and a new list is returned which contains items for which the function evaluats to True.
Here is an example use of filter() function to filter out only even numbers from a list. '''
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

evens_list = list(filter(lambda x: (x%2 == 0) , my_list))

#Output: [4, 6, 8, 12]
print(evens_list)

odds_list = list(filter(lambda x: (x%2 != 0) , my_list))

# Output: [1, 3, 5, 11]
print odds_list
odds_list.sort()
print odds_list
odds_list.reverse()
print odds_list
