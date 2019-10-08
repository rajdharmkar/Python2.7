#itermethods of dict examples
numnames = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eiight',9:'nine'}
for k in numnames.iterkeys():
    print k
for v in numnames.itervalues():
   print v
for k,v in numnames.iteritems():
    print k,v
