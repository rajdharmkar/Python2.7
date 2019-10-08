my_str = input("Enter a string: ")  
# breakdown the string into a list of words  
words = my_str.split()# here separator is a space between words
print words
# sort the list  
words.sort()  
# display the sorted words  
for word in words:  
   print(word)  
my_str = input("Enter a string with words separated by semicolon: ")
words = my_str.split(';')# here separator is a semicolon between words
print words
# sort the list  
words.sort()  
# display the sorted words  
for word in words:  
   print(word) 
