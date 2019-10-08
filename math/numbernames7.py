#program to write numerals upto 9999 into words
i = input("Enter a numeral:")
a1 = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a2 = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a3 = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
b = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
c = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
d = ['hundred','thousand']

def foo(i):
    if i in a3.iterkeys():
        print a3.get(i)
    else:
        if i in b.iterkeys():
          print b.get(i)


if i < 1000:
        if i/1000 in a1.iterkeys():
            print a1.get(i/1000)+' '+d[1],

else:
    if i/1000 in a2.iterkeys():
        print a2.get(i/1000)+' '+d[1],

if (i%1000)/100 in a1.iterkeys():
    print a1.get((i%1000)/100)+' '+d[0],
if 0<=i%100 <=19:
   foo(i%100)
else:
    if ((i%100)/10) in c.iterkeys() and ((i%100)%10) in a2.iterkeys():
        print c.get((i%100)/10), a2.get((i%100)%10)


'''$ pip install pynum2word
Then use it in the following way

>>> import num2word
>>> num2word.to_card(16)
'sixteen'
>>> num2word.to_card(23)
'twenty-three'
>>> num2word.to_card(1223)
'one thousand, two hundred and twenty-three'''