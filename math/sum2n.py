#Write a program to find the sum of first n natural numbers
num = a = int(raw_input("Enter a number:"))

if num < 0:
    print{"Enter a positive integer"}
else:
    sum = 0
    while (num > 0):
        sum += num
        num -= 1
    print("The sum upto %d is",a,sum)
        
