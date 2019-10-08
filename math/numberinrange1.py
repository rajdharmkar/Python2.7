#program to find if input number is between 1 and 100
number = input('Enter any number:')
if number in range(2,101):
   print 'The input number {} lies between 1 and 100'.format(number)
else:
   print 'The input number {} is out of range'.format(number)
    
    
