X = [[1,2,3],[4,5,6],[7,8,9]]
#Y = [[1,2,3],[4,5,6],[7,8,9]]
transpose = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):#why len(X[0])taken?
        transpose[j][i]=X[i][j]
for r in transpose:#this is printing sort of matrix format
    print(r)
print transpose#this is printing in list of list(row) form
