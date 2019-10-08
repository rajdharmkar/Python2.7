# define punctuation  
#numerals = '[0-9]'
numerals = '0,1,2,3,4,5,6,7,8,9'
# take input from the user  
my_str = raw_input("Enter a alphanumeric string: ")
# remove numerals from the string
no_numer = ""
for i in my_str:
   if i not in numerals:
       no_numer = no_numer + i
# display the alphabet string
print(no_numer)
