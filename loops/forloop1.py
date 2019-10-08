#for loop example and count letters in a word
#string = str(input("Enter any string:"))
string = raw_input("Enter any string:")
print len(string)
count = 0
for i in string:
    count +=1
    print i,
print "\n",count    
