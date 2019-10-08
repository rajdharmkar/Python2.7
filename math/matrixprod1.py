X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[1,2,3],[4,5,6],[7,8,9]]
product = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):#why len(Y[0])taken?
        for k in range(len(Y)):
            product[i][j]+=X[i][k]*Y[k][j]
for r in product:
    print(r)
