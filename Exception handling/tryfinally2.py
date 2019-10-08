try:
     try:
       x = float(raw_input("Your number: "))
       foo = 1.0 / x
     finally:
       print("There may or may not be an exception.")
       print "The reciprocal: \n", foo

except:
    print "Error: Enter only a float number and not a literal"
