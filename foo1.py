def foo1(a,b):
    print 'welcome'
if __name__ == "__main__":
    import sys
foo1(3,4)
print sys.argv
print sys.argv[0]
print (len(sys.argv))
print (str(sys.argv))
#  print sys.argv[1]#index out of range
#  foo1(int(sys.argv[0]))
