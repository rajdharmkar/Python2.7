def fibo_recur(n):
    if n <= 1:
        return n#return n is necessary as when p=0, output is 0 and when p=1 output =1
    else:    
        return (fibo_recur(n-1) + fibo_recur(n-2))
p = int(input("Enter thenumber of terms:"))
if p<=0:
    print ("Enter a positive number:")
else:    
    for i in range(p):
        print(fibo_recur(i))
