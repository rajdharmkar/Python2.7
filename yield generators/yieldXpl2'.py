def search(keyword, filename):
    print('generator started')
    f = open(filename, 'r')
    # Looping through the file line by line
    for line in f:
        if keyword in line:
            # If keyword found, return it
            yield line
    f.close()
#search('ram', "new3.txt")
type(search)
the_generator = search ('ram', "new3.txt")
type(the_generator)
print(next(the_generator))
print(next(the_generator))
print(next(the_generator))# there are two occurences of ram in file so after 2 loops there is stopIteration and one more
#execution of the statement shows error as iteration has stopped