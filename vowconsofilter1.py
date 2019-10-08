alphabets =['a','b','c','d','f','j','k','i','m','n','p']
vowels = ['a','e','i','o','u']

def filtervowels1(x):
    for i in vowels:
        if i in x:
            print i,

def filtervowels2(z):
    for i in vowels:
        if i not in z:
            print i,
filtervowels1(alphabets)
print '\n'
filtervowels2(alphabets)
print'\n'

def filterconsonants(y):
    for i in y:
        if i not in vowels:
           print i,
filterconsonants(alphabets)
print '\n'
foo = raw_input('Enter a string to filter out consonants:')

filterconsonants(foo)
print '\n'
filtervowels1(foo)
        
