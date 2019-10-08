lines_seen = set()  # holds lines already seen
outfile = open('new2.txt', "w")
infile = open('new3.txt', "r")
for line in infile:
    print line
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print '______________________________________________'
for line in lines_seen:
    print line
print '_______________________________________________'
a = open('new2.txt','r')
for line in a:
    print line