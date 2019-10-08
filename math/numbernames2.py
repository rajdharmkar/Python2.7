#program to write numerals upto 999 into words-not able to write 112,216,815..etc
i = input("Enter a numeral:")
digits = [0,1,2,3,4,5,6,7,8,9]
names = ['one','two','three','four','five','six','seven','eight','nine']
numnames1 = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eiight',9:'nine'}
numnames2 = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
numnames3 = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
foo = ['hundred','thousand']

if i<20:
    if i in numnames1.iterkeys():
        print numnames1.get(i)
    else:
        if i in numnames2.iterkeys():
          print numnames2.get(i)
else:
    if (i/100) in numnames1.iterkeys()and (i%100)/10 in numnames3.iterkeys()and (i%100)%10 in numnames1.iterkeys():
       print numnames1.get(i/100)+ ' '+foo[0], numnames3.get((i%100)/10), numnames1.get((i%100)%10)

