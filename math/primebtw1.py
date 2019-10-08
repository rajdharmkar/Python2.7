#prints all the prime numbers between the lower and upper numbers inputed
lower = int(raw_input("Enter a number:"))
upper = int(raw_input("Enter a number:"))
for num in range(lower+1,upper):
    if num > 1:
        for i in range(2,num): 
    
            if (num % i)==0:
                break

        else:
            print(num)


    
