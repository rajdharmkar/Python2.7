# This function has a variable with
# name same as s.
def f(): 
	s = "Me too."
	k = 43
	print s, k 

# Global scope
s = "I love Geeksforgeeks"
k = 12
f()
print s
