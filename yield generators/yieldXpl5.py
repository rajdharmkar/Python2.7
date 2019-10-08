def f2():
    a = range(100)
    for i in range(10):
        tmp = a[i:i**2]
        yield tmp, id(tmp)

b = f2()
for tmp, id_tmp in b:
        print id_tmp == id(tmp)
