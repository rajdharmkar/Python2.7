X = [[1,2,3],[4,5,6],[7,8,9]]
#X matrix is of order 3x3, a list of three lists each of which is a row
print(len(X))#gives the number of items in list
print(len(X[0]))#gives the number of items in the first row of matrix
print(X[0])#prints the first row of matrix X
print(X[1])#prints the second row of matrix X
print(X[2])#prints the third row of matrix X
#below are listed the various elements of matrix as per row and column number 
print(X[0][0])
print(X[0][1])
print(X[0][2])
print(X[1][0])
print(X[1][1])
print(X[1][2])
print(X[2][0])
print(X[2][1])
print(X[2][2])
Y = [[1,2,3],[4,5,6],[7,8,9]]
sum = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
	for j in range(len(X[0])):
		sum[i][j]=X[i][j]+Y[i][j]
for r in sum:
    print r
