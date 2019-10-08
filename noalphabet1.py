# define alphabet
alphabets = ['a','b','r','m']
# take input from the user
my_str = raw_input("Enter a alphanumeric string: ")
# remove alphabets from the string
no_alpha = ""
for i in my_str:
   if i not in alphabets:
       no_alpha = no_alpha + i
# display the numeric string
print(no_alpha)
