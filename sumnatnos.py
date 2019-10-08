#sum of first n natural numbers using recursive method
def sum_n(n):
    if n== 0:
        return 0
    else:
        return n + sum_n(n-1)
#sum of first n natural numbers using for loop method
def sum_n1(n):
    j=0
    for i in range(n+1):
        j +=i
    return j
y=input("Enter an positive integer:")
print sum_n(y)
print sum_n1(y)
