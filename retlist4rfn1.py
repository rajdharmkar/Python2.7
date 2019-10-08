#passing parameters to a function by value
def changeList(list1):
    print('have', list1)
    list1 = ['and', 'we', 'can', 'not', 'lie']
    print('set to', list2)

list2 = ['we', 'like', 'proper', 'English']

print('before, list2 =', list2)
changeList(list2)
print('after, list2 =', list2)
