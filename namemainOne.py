# file namemainOne.py
#print("top-level in namemainOne.py")

def func(x):
    #print("func() in namemainOne.py")
    return 2*x
print func(5)

if __name__ == "__main__":
    print("namemainOne.py is being run directly")
    import sys
 #   b = sys.argv[1] # the argument is being taken as a string and error is being shown
    print (func(int(sys.argv[1])))
else:
    print("namemainOne.py is being imported into another module")
