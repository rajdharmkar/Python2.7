#program to write numerals upto 999 into words
i = input("Enter a numeral:")
a = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
b = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
c = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
d = ['hundred','thousand']

def foo(i):
    if i in a.iterkeys():
        print a.get(i)
    else:
        if i in b.iterkeys():
          print b.get(i)
a.pop(0)
if i/100 in a.iterkeys():
    print a.get(i/100)+' '+d[0],
p= {0:''}
a.update(p)
if 0<=i%100 <=19:
   foo(i%100)
else:
    if ((i%100)/10) in c.iterkeys() and ((i%100)%10) in a.iterkeys():
        print c.get((i%100)/10), a.get((i%100)%10)


