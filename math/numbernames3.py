#program to write numerals upto 999 into words
i = input("Enter a numeral:")
numnames1 = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
numnames2 = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
numnames3 = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
foo = ['hundred','thousand']

if i<20:
    if i in numnames1.iterkeys():
        print numnames1.get(i)
    else:
        if i in numnames2.iterkeys():
          print numnames2.get(i)
elif 20<=i<=99:
        if (i / 10) in numnames3.iterkeys() and (i % 10) in numnames1.iterkeys():
            print numnames3.get(i / 10), numnames1.get(i % 10)
elif 100<=i<120:
        if (i/100) in numnames1.iterkeys()and (i%100) in numnames2.iterkeys():
            print numnames1.get(i/100)+ ' '+foo[0], 'and' , numnames2.get((i%100))
elif 120<=i<=1000:
        if (i/100) in numnames1.iterkeys()and (i%100)/10 in numnames3.iterkeys()and (i%100)%10 in numnames1.iterkeys():
            print numnames1.get(i/100)+ ' '+foo[0], numnames3.get((i%100)/10), numnames1.get((i%100)%10)

